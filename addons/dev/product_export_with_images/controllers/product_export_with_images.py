# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Ammu Raj(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
import PIL
import base64
import io
import zipfile
from odoo import http
from odoo.http import content_disposition, request
from PIL import Image


class ExcelReportController(http.Controller):
    """This class includes the function to downloads excel report."""
    @http.route(
        [
            '/products_download/image_zip/<model("product.export"):wizards>',
        ],
        type="http",
        auth="public",
        csrf=False,
    )
    def get_product_image_zip(self, wizards=None):
        product_lines = wizards.get_product_lines()        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for idx, line in enumerate(product_lines, 1):
                if line["image"]:
                    image_data = base64.b64decode(line["image"])
                    # Puedes usar el nombre del producto o un índice para el archivo
                    image_name = f'{line["internal_reference"] or "product"}_{idx}.png'
                    zip_file.writestr(image_name, image_data)
        zip_buffer.seek(0)
        return request.make_response(
            zip_buffer.getvalue(),
            headers=[
                ('Content-Type', 'application/zip'),
                ('Content-Disposition', content_disposition('imagenes_productos.zip'))
            ]
        )
    # def get_product_image_zip(self, wizards=None):
        
    #     print(f"Pillow version: {PIL.__version__}")
    #     print(f"WEBP support in Image.SAVE: {'WEBP' in Image.SAVE}")

    #     product_lines = wizards.get_product_lines()
    #     zip_buffer = io.BytesIO()
    #     with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
    #         for idx, line in enumerate(product_lines, 1):
    #             if line["image"]:
    #                 image_data_b64 = line["image"]
    #                 image_data_bytes = base64.b64decode(image_data_b64)
    
    #                 try:
    #                     # Abre la imagen usando Pillow desde los bytes
    #                     img = Image.open(io.BytesIO(image_data_bytes))
    
    #                     # Crea un buffer para guardar la imagen en formato WebP
    #                     webp_buffer = io.BytesIO()
    #                     # Guarda la imagen en formato WebP en el buffer
    #                     img.save(webp_buffer, format="WEBP")
    #                     webp_data = webp_buffer.getvalue()
    
    #                     # Define el nombre del archivo con extensión .webp
    #                     image_name = f'{line["internal_reference"] or "product"}_{idx}.webp'
    
    #                     # Escribe los datos de la imagen WebP en el archivo zip
    #                     zip_file.writestr(image_name, webp_data)
    
    #                 except Exception as e:
    #                     # Manejo de errores si una imagen no se puede procesar
    #                     print(f"Error processing image for product {line.get('internal_reference', 'N/A')}: {e}")
    #                     # Opcional: podrías escribir un archivo de texto en el zip indicando el error
    #                     error_msg = f"Could not process image for product {line.get('internal_reference', 'N/A')}: {e}"
    #                     zip_file.writestr(f'error_{idx}.txt', error_msg)
    
    
    #     zip_buffer.seek(0)
    #     return request.make_response(
    #         zip_buffer.getvalue(),
    #         headers=[
    #             ('Content-Type', 'application/zip'),
    #             ('Content-Disposition', content_disposition('imagenes_productos_webp.zip')) # Cambia el nombre del archivo zip si quieres
    #         ]
    #     )
    