#!/usr/bin/env python3
"""
Script para envío de certificados usando Mailgun
Uso: python send_certificate.py "nombre" "email" "documento" "archivo.pdf"
"""

import sys
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def send_certificate_email(full_name, email, document, file_name):
    """Envía el certificado por email usando Mailgun API"""

    # Configuración de Mailgun desde variables de entorno
    MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
    MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
    MAILGUN_FROM_EMAIL = os.getenv('MAILGUN_FROM_EMAIL')
    MAILGUN_FROM_NAME = os.getenv('MAILGUN_FROM_NAME')

    if not all([MAILGUN_API_KEY, MAILGUN_DOMAIN, MAILGUN_FROM_EMAIL]):
        print("❌ Error: Configuración de Mailgun incompleta. Verifica el archivo .env")
        return False

    # URL de la API de Mailgun
    mailgun_url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"

    completion_date = datetime.now().strftime('%d/%m/%Y')

    # Crear mensaje para el usuario
    user_subject = '¡Felicitaciones! Certificado de Capacitación Sinnut ERP'
    user_body = f"""Hola {full_name},

¡Felicitaciones! Has completado exitosamente la capacitación en Sinnut ERP.

Detalles de tu certificación:
- Nombre: {full_name}
- Documento: {document}
- Fecha de finalización: {completion_date}
- Archivo generado: {file_name}

Tu certificado ha sido enviado también al departamento de gestión humana.

Atentamente,
Equipo de Capacitación Sinnut ERP
Oroexpress"""

    # Crear mensaje para gestión humana
    admin_subject = f'Nuevo Certificado Emitido - {full_name}'
    admin_body = f"""Nuevo certificado emitido:

Estudiante: {full_name}
Email: {email}
Documento: {document}
Fecha de finalización: {completion_date}
Fecha de emisión: {datetime.now().strftime('%d/%m/%Y')}

Archivo generado: {file_name}

Por favor, archivar este certificado en los registros de RRHH.

--
Sistema Automático de Certificación
Sinnut ERP"""

    try:
        # Preparar archivos adjuntos si existen
        files = {}
        pdf_path = file_name if file_name.endswith('.pdf') else file_name + '.pdf'
        if os.path.exists(pdf_path):
            files['attachment'] = open(pdf_path, 'rb')

        # Enviar correo al usuario
        print(f"📧 Enviando certificado a {email}...")
        user_data = {
            'from': f'{MAILGUN_FROM_NAME} <{MAILGUN_FROM_EMAIL}>',
            'to': email,
            'subject': user_subject,
            'text': user_body
        }

        user_response = requests.post(
            mailgun_url,
            auth=('api', MAILGUN_API_KEY),
            data=user_data,
            files=files
        )

        if user_response.status_code == 200:
            print("✅ Correo al estudiante enviado exitosamente")
        else:
            print(f"❌ Error enviando correo al estudiante: {user_response.status_code} - {user_response.text}")
            return False

        # Cerrar archivo si fue abierto
        if files.get('attachment'):
            files['attachment'].close()

        # Enviar correo a gestión humana (sin adjunto para evitar duplicación)
        print(f"📧 Enviando notificación a gestión humana...")
        admin_data = {
            'from': f'Sistema de Certificación Sinnut ERP <{MAILGUN_FROM_EMAIL}>',
            'to': MAILGUN_FROM_EMAIL,
            'subject': admin_subject,
            'text': admin_body
        }

        admin_response = requests.post(
            mailgun_url,
            auth=('api', MAILGUN_API_KEY),
            data=admin_data
        )

        if admin_response.status_code == 200:
            print("✅ Notificación a gestión humana enviada exitosamente")
        else:
            print(f"❌ Error enviando notificación a gestión humana: {admin_response.status_code} - {admin_response.text}")
            return False

        print("🎉 ¡Certificado enviado exitosamente!")
        return True

    except Exception as e:
        print(f"❌ Error enviando correos: {str(e)}")
        return False

def main():
    if len(sys.argv) != 5:
        print("Uso: python send_certificate.py \"nombre\" \"email\" \"documento\" \"archivo.pdf\"")
        print("Ejemplo: python send_certificate.py \"Juan Pérez\" \"juan@email.com\" \"123456789\" \"certificado_juan.pdf\"")
        sys.exit(1)

    full_name = sys.argv[1]
    email = sys.argv[2]
    document = sys.argv[3]
    file_name = sys.argv[4]

    success = send_certificate_email(full_name, email, document, file_name)

    if success:
        print("\n✅ Proceso completado exitosamente")
        sys.exit(0)
    else:
        print("\n❌ Error en el proceso de envío")
        sys.exit(1)

if __name__ == '__main__':
    main()