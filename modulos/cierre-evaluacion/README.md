# Sistema de Certificación Sinnut ERP

Sistema automatizado para envío de certificados de capacitación usando Mailgun.

## 🚀 Inicio Rápido

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar Mailgun:**
   - Completa el archivo `.env` con tus credenciales de Mailgun
   - Asegúrate de que el dominio esté verificado en Mailgun

3. **Usar el sistema:**
   - Abre `evaluacion-final.html` en tu navegador
   - Completa el formulario de certificación
   - El PDF se descarga automáticamente
   - Ejecuta el comando mostrado para enviar por correo

## 📧 Envío de Certificados

### Proceso Automático

1. **Generación:** El formulario crea el PDF automáticamente
2. **Descarga:** El certificado se descarga en tu navegador
3. **Datos:** Se crea un archivo JSON con la información
4. **Envío:** Ejecuta el comando Python para enviar por Mailgun

### Comando de Envío

```bash
python send_certificate.py "Juan Pérez" "juan@email.com" "123456789" "certificado_juan.pdf"
```

### ¿Qué hace el script?

- ✅ Envía certificado al estudiante por email
- ✅ Envía notificación a gestión humana
- ✅ Adjunta el PDF del certificado
- ✅ Usa Mailgun para entrega confiable

## ⚙️ Configuración de Mailgun

### 1. Crear cuenta en Mailgun
Ve a [mailgun.com](https://www.mailgun.com) y crea una cuenta.

### 2. Verificar dominio
- Ve a "Sending" → "Domains"
- Agrega y verifica tu dominio
- Copia la API Key desde "Settings" → "API Keys"

### 3. Configurar .env
```env
MAILGUN_API_KEY=key-1234567890abcdef
MAILGUN_DOMAIN=tu-dominio.mailgun.org
MAILGUN_FROM_EMAIL=certificados@tu-dominio.com
MAILGUN_FROM_NAME=Equipo de Capacitación Sinnut ERP
```

## 📋 Archivos del Sistema

- `send_certificate.py` - Script principal para envío de certificados
- `evaluacion-final.html` - Interfaz web para generar certificados
- `requirements.txt` - Dependencias Python
- `.env` - Configuración de Mailgun (no subir a git)
- `.env.example` - Ejemplo de configuración

## 🔧 Solución de Problemas

### Error de credenciales
```
❌ Error: Configuración de Mailgun incompleta
```
**Solución:** Verifica que el archivo `.env` tenga todas las variables requeridas.

### Error de dominio
```
❌ Error enviando correos
```
**Solución:** Asegúrate de que el dominio esté verificado en Mailgun.

### Dependencias faltantes
```bash
pip install python-dotenv requests
```

## 📧 Flujo de Trabajo

1. **Usuario completa formulario** → Genera PDF + JSON
2. **PDF se descarga automáticamente**
3. **Administrador ejecuta comando** → Envía por Mailgun
4. **Correos llegan automáticamente** → Usuario + RRHH

## 🔒 Seguridad

- Credenciales en variables de entorno (`.env`)
- Archivo `.env` excluido del control de versiones
- Comunicación segura con API de Mailgun
- Sin exposición de credenciales en el navegador

¡El sistema está listo para usar! 🎉