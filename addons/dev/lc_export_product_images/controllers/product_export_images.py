# -*- coding: utf-8 -*-

# import PIL
import io
import zipfile
import base64
from odoo import http
from odoo.http import request, content_disposition
# from PIL import Image
import re


class ExportImagesController(http.Controller):
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
        # print(f"Number of product lines: {len(product_lines)}")  # Debugging line to check the number of products       
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for idx, line in enumerate(product_lines, 1):                
                if line.get("image"): # Usar .get() es más seguro                    
                    image_data_b64 = line["image"]
                    image_data_bytes = base64.b64decode(image_data_b64)
                    try:                        
                        final_image_data = image_data_bytes                        
                        image_extension = "jpg"                        
                        # Reemplazamos caracteres problemáticos (como '/', '\', ':', '*', '?', '"', '<', '>', '|')
                        product_name = line.get("name", f"Product_{idx}") # Obtén el nombre, usa un valor por defecto si no existe
                        # Usamos una expresión regular para reemplazar caracteres no permitidos en nombres de archivo/carpeta
                        sanitized_product_name = re.sub(r'[\\/:*?"<>|]', '_', product_name)
                        file_image_name = re.sub(r'[\\/:*?"<>.|]', '-', product_name) 
                        file_image_name = file_image_name.replace(" ", "-")
                        file_image_name = file_image_name.lower() # Convertimos a minúsculas para estandarizar
                        file_image_name = file_image_name[:70]  # Limitar a 50 caracteres para evitar problemas de longitud
                        file_image_name = file_image_name.strip('-')  # Eliminar guiones al inicio o al final
                        file_image_name = file_image_name + f'-{idx}'  # Añadir un sufijo con el índice para evitar colisiones
                        # Usaremos la referencia interna como nombre del archivo dentro de la carpeta del producto
                        
                        # internal_ref_value = line.get("internal_reference")                        
                        # product_ref = (str(internal_ref_value) if internal_ref_value else "imagenoref") + "_" + str(idx)                        
                        # product_ref = sanitized_product_name + "_" + str(idx)
                        # Construye el nombre del archivo dentro de la carpeta del producto
                        # Ejemplo: "Nombre del Producto/REF_1.webp"
                        image_filename = f'{file_image_name}.{image_extension}'
                        full_zip_path = f'{sanitized_product_name}/{image_filename}'
                        # Escribe los datos de la imagen en el archivo zip con la ruta completa
                        zip_file.writestr(full_zip_path, final_image_data)

                    except Exception as e:
                        # Manejo de errores si una imagen no se puede procesar
                        print(f"Error processing image for product {line.get('internal_reference', 'N/A')}: {e}")
                        # Opcional: podrías escribir un archivo de texto en el zip indicando el error
                        error_msg = f"Could not process image for product {line.get('internal_reference', 'N/A')}: {e}"
                        zip_file.writestr(f'error_{idx}.txt', error_msg)

        zip_buffer.seek(0)
        return request.make_response(
            zip_buffer.getvalue(),
            headers=[
                ('Content-Type', 'application/zip'),
                ('Content-Disposition', content_disposition('product_images.zip')) # Cambia el nombre del archivo zip si quieres
            ]
        )
    
    # TODO: Para exportar las imagenes en formato WebP, descomentar el siguiente método y comentar el anterior.
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
    