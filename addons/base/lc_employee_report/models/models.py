# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta
from pytz import timezone
import math

class LcEmployeeReport(models.TransientModel):
    _name = 'lc.employee.report'
    _description = 'Attendance Report Employee Wizard'
    
    def _get_employee_id(self):
        employee_rec = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        return employee_rec.id

    from_date = fields.Date('From Date', default=lambda self:fields.Date.to_string(date.today().replace(day=1)),required=True)
    to_date = fields.Date('To Date', default=lambda self: fields.Date.to_string((datetime.now() + relativedelta(months=+1, day=1, days=-1)).date()), required=True)    
    employee_id = fields.Many2one('hr.employee',string="Employee", default=_get_employee_id)
     
    # @api.multi
    def print_report(self):
        datas = []
        domain = []
        employee = ""
        job_title = ""
        wage = 0
        total_additional_hour = 0
        total_discount = 0
        total_hours_late = 0
        total_hours = 0        
        if self.employee_id:
            domain.append(('id', '=', self.employee_id.ids))
        sql_query = """
        SELECT name, dates, job_title, check_in, check_out, COALESCE(hours,0) hours, 
            COALESCE(ROUND((EXTRACT(HOUR FROM additional_hour_exit)+EXTRACT(MINUTE FROM additional_hour_exit)/60)::NUMERIC,2),0) AS additional_hour,
            COALESCE(ROUND((EXTRACT(HOUR FROM discount_check_in_time+discount_check_out_time)+EXTRACT(MINUTE FROM discount_check_in_time+discount_check_out_time)/60)::NUMERIC,2),0) AS discount, 
            COALESCE(hours_late,0) AS hours_late, wage, comment
        FROM
        (SELECT e.id, e.name, dates::DATE FROM generate_series('%s', '%s', '1 day'::INTERVAL) dates, hr_employee e) AS j
        LEFT JOIN
        (
        SELECT id, job_title, check_in, check_out, hours, 
            CASE WHEN check_out_time>time_of_exit THEN check_out_time-time_of_exit ELSE '00:00:00' END AS additional_hour_exit,
            CASE WHEN check_in_time<time_of_entry - INTERVAL '19 MINUTE' THEN time_of_entry-check_in_time ELSE '00:00:00' END AS additional_hour_entry,
            CASE WHEN check_in_time>time_of_entry + INTERVAL '15 MINUTE' THEN 1 ELSE 0 END AS hours_late, 
            CASE WHEN check_in_time>time_of_entry + INTERVAL '25 MINUTE' THEN check_in_time-time_of_entry ELSE '00:00:00' END AS discount_check_in_time,
            CASE WHEN check_out_time<time_of_exit - INTERVAL '25 MINUTE' THEN time_of_exit-check_out_time ELSE '00:00:00' END AS discount_check_out_time,
            wage, comment
        FROM lc_employee_view
            ) AS k ON j.id=k.id AND j.dates=DATE(k.check_in) WHERE j.id=%s ORDER BY j.name, j.dates;
        """ % (self.from_date,self.to_date,self.employee_id.ids[0])
        
        ### CONSULTA TOMANDO EN CUENTA LAS EXTRAS DE LA HORA DE INGRESO
        # sql_query = """
        # SELECT name, dates, job_title, check_in, check_out, COALESCE(hours,0) hours, 
        #     COALESCE(ROUND((EXTRACT(HOUR FROM additional_hour_exit+additional_hour_entry)+EXTRACT(MINUTE FROM additional_hour_exit+additional_hour_entry)/60)::NUMERIC,2),0) AS additional_hour,
        #     COALESCE(ROUND((EXTRACT(HOUR FROM discount_check_in_time+discount_check_out_time)+EXTRACT(MINUTE FROM discount_check_in_time+discount_check_out_time)/60)::NUMERIC,2),0) AS discount, 
        #     COALESCE(hours_late,0) AS hours_late, wage, comment
        # FROM
        # (SELECT e.id, e.name, dates::DATE FROM generate_series('%s', '%s', '1 day'::INTERVAL) dates, hr_employee e) AS j
        # LEFT JOIN
        # (
        # SELECT id, job_title, check_in, check_out, hours, 
        #     CASE WHEN check_out_time>time_of_exit THEN check_out_time-time_of_exit ELSE '00:00:00' END AS additional_hour_exit,
        #     CASE WHEN check_in_time<time_of_entry - INTERVAL '19 MINUTE' THEN time_of_entry-check_in_time ELSE '00:00:00' END AS additional_hour_entry,
        #     CASE WHEN check_in_time>time_of_entry + INTERVAL '15 MINUTE' THEN 1 ELSE 0 END AS hours_late, 
        #     CASE WHEN check_in_time>time_of_entry + INTERVAL '25 MINUTE' THEN check_in_time-time_of_entry ELSE '00:00:00' END AS discount_check_in_time,
        #     CASE WHEN check_out_time<time_of_exit - INTERVAL '25 MINUTE' THEN time_of_exit-check_out_time ELSE '00:00:00' END AS discount_check_out_time,
        #     wage, comment
        # FROM lc_employee_view
        #     ) AS k ON j.id=k.id AND j.dates=DATE(k.check_in) WHERE j.id=%s ORDER BY j.name, j.dates;
        # """ % (self.from_date,self.to_date,self.employee_id.ids[0])
        self.env.cr.execute(sql_query)
        result = self.env.cr.dictfetchall()        
        for reg in result:              
            datas.append({
                'dates':reg['dates'],                
                'check_in':reg['check_in'],
                'check_out':reg['check_out'],
                'additional_hour':reg['additional_hour'],
                'discount':reg['discount'],
                'hours_late':reg['hours_late'],
                'comment':reg['comment'],                                    
            })
            total_hours += reg['hours']
            total_additional_hour += reg['additional_hour']
            total_discount += reg['discount']
            total_hours_late += reg['hours_late']
            if reg['name']: 
                employee = reg['name']
            if reg['job_title']:             
                job_title = reg['job_title']
            if reg['wage']: 
                wage = reg['wage']
        wage_hour = round((wage/30)/8,2)
        wage_extra_hour = round(wage_hour*2,2)
        discount_late_hour = math.floor(total_hours_late/3)*8
        total_additional_value =  round(total_additional_hour*wage_extra_hour,2)
        total_discount_value = round((total_discount + discount_late_hour)*wage_hour,2)
        total = round(total_additional_value - total_discount_value,2)
        total_worked_hours = round(total_hours - total_additional_hour,2);
        res = {
            'attendances':datas,
            'start_date': self.from_date,
            'end_date': self.to_date,
            'employee': employee,
            'job_title': job_title,
            'wage': wage,
            'total_additional_hour': round(total_additional_hour,2),
            'total_discount': round(total_discount,2),
            'total_hours_late': total_hours_late,
            'wage_hour': wage_hour,
            'wage_extra_hour': wage_extra_hour,
            'total_additional_value': total_additional_value,
            'total_discount_value': total_discount_value,
            'total': total,
            'total_worked_hours': total_worked_hours,
        }
        data = {
            'form': res,
        }
        return self.env.ref('lc_employee_report.lc_employee_report_hr_attendance').report_action([],data=data)

    def print_report_detail(self):
        datas = []
        domain = []
        employee = ""
        job_title = ""
        wage = 0
        total_additional_hour = 0
        total_discount = 0
        total_hours_late = 0
        total_hours = 0        
        if self.employee_id:
            domain.append(('id', '=', self.employee_id.ids))
        sql_query = """
        SELECT name, dates, job_title, check_in, check_out, COALESCE(hours,0) hours, 
            COALESCE(ROUND((EXTRACT(HOUR FROM additional_hour_exit+additional_hour_entry)+EXTRACT(MINUTE FROM additional_hour_exit+additional_hour_entry)/60)::NUMERIC,2),0) AS additional_hour,
            COALESCE(ROUND((EXTRACT(HOUR FROM discount_check_in_time+discount_check_out_time)+EXTRACT(MINUTE FROM discount_check_in_time+discount_check_out_time)/60)::NUMERIC,2),0) AS discount, 
            COALESCE(hours_late,0) AS hours_late, wage, comment
        FROM
        (SELECT e.id, e.name, dates::DATE FROM generate_series('%s', '%s', '1 day'::INTERVAL) dates, hr_employee e) AS j
        LEFT JOIN
        (
        SELECT id, job_title, check_in, check_out, hours, 
            CASE WHEN check_out_time>time_of_exit THEN check_out_time-time_of_exit ELSE '00:00:00' END AS additional_hour_exit,
            CASE WHEN check_in_time<time_of_entry - INTERVAL '19 MINUTE' THEN time_of_entry-check_in_time ELSE '00:00:00' END AS additional_hour_entry,
            CASE WHEN check_in_time>time_of_entry + INTERVAL '15 MINUTE' THEN 1 ELSE 0 END AS hours_late, 
            CASE WHEN check_in_time>time_of_entry + INTERVAL '25 MINUTE' THEN check_in_time-time_of_entry ELSE '00:00:00' END AS discount_check_in_time,
            CASE WHEN check_out_time<time_of_exit - INTERVAL '25 MINUTE' THEN time_of_exit-check_out_time ELSE '00:00:00' END AS discount_check_out_time,
            wage, comment
        FROM lc_employee_view
            ) AS k ON j.id=k.id AND j.dates=DATE(k.check_in) WHERE j.id=%s ORDER BY j.name, j.dates;
        """ % (self.from_date,self.to_date,self.employee_id.ids[0])
        self.env.cr.execute(sql_query)
        result = self.env.cr.dictfetchall()        
        for reg in result:              
            datas.append({
                'dates':reg['dates'],                
                'check_in':reg['check_in'],
                'check_out':reg['check_out'],
                'additional_hour':reg['additional_hour'],
                'discount':reg['discount'],
                'hours_late':reg['hours_late'],
                'comment':reg['comment'],                                    
            })
            total_hours += reg['hours']
            total_additional_hour += reg['additional_hour']
            total_discount += reg['discount']
            total_hours_late += reg['hours_late']
            if reg['name']: 
                employee = reg['name']
            if reg['job_title']:             
                job_title = reg['job_title']
            if reg['wage']: 
                wage = reg['wage']
        wage_hour = round((wage/30)/8,2)
        wage_extra_hour = round(wage_hour*2,2)
        discount_late_hour = math.floor(total_hours_late/3)*8
        total_additional_value =  round(total_additional_hour*wage_extra_hour,2)
        total_discount_value = round((total_discount + discount_late_hour)*wage_hour,2)
        total = round(total_additional_value - total_discount_value,2)
        total_worked_hours = round(total_hours - total_additional_hour,2);
        res = {
            'attendances':datas,
            'start_date': self.from_date,
            'end_date': self.to_date,
            'employee': employee,
            'job_title': job_title,
            'wage': wage,
            'total_additional_hour': round(total_additional_hour,2),
            'total_discount': round(total_discount,2),
            'total_hours_late': total_hours_late,
            'wage_hour': wage_hour,
            'wage_extra_hour': wage_extra_hour,
            'total_additional_value': total_additional_value,
            'total_discount_value': total_discount_value,
            'total': total,
            'total_worked_hours': total_worked_hours,
        }
        data = {
            'form': res,
        }
        return self.env.ref('lc_employee_report.lc_employee_report_hr_detail_attendance').report_action([],data=data)

class LcEmployeeView(models.Model):
    _name = "lc.employee.view"
    _auto = False
     
    def init(self):        
        tools.drop_view_if_exists(self._cr, 'lc_employee_view')        
        self._cr.execute("""        
            CREATE or REPLACE VIEW lc_employee_view AS (
                SELECT 
                e.id, 
                e.name AS employee, 
                e.job_title, 
                p.time_of_entry, 
                p.time_of_exit, 
                h.hours, 
                h.check_in, 
                h.check_out, 
                h.check_in_time, 
                h.check_out_time, 
                c.wage, 
                h.comment 
                FROM hr_employee AS e 
                LEFT JOIN
                (SELECT employee_id, check_in::timestamp at time zone 'UTC' AS check_in, check_out::timestamp at time zone 'UTC' AS check_out, worked_hours AS hours, CONCAT(EXTRACT(hour FROM check_in::timestamp at time zone 'UTC'),':',EXTRACT(minute FROM check_in::timestamp at time zone 'UTC'))::time AS check_in_time, CONCAT(COALESCE(EXTRACT(hour FROM check_out::timestamp at time zone 'UTC'),EXTRACT(hour FROM check_in::timestamp at time zone 'UTC')),':',COALESCE(EXTRACT(minute FROM check_out::timestamp at time zone 'UTC'),EXTRACT(minute FROM check_in::timestamp at time zone 'UTC')))::time AS check_out_time, comment FROM hr_attendance)
                AS h ON e.id=h.employee_id 
                LEFT JOIN 
                (SELECT id AS id_horario, MIN(check_in) AS time_of_entry, MAX(check_out) AS time_of_exit FROM (SELECT DISTINCT r.id, r.name, CONCAT(TRUNC(hour_from),':',(hour_from-TRUNC(hour_from))*60)::time AS check_in, CONCAT(TRUNC(hour_to),':',(hour_to-TRUNC(hour_to))*60)::time AS check_out FROM resource_calendar r, resource_calendar_attendance c WHERE r.id=c.calendar_id) AS t GROUP BY id, name)
                AS p ON e.resource_calendar_id=p.id_horario 
                LEFT JOIN
                hr_contract AS c ON e.id=c.employee_id
                WHERE e.active='t' AND  c.active='t' AND c.state='open'                
            )""")