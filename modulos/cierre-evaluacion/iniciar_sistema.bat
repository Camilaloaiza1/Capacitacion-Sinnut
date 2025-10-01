@echo off@echo off

echo 🚀 Sistema de Certificación Sinnut ERP - Envío Directo con Mailgunecho 🚀 Iniciando Sistema de Certificación Sinnut ERP con Mailgun

echo.echo.



echo 📁 Cambiando al directorio del proyecto...echo 📁 Cambiando al directorio del proyecto...

cd /d "%~dp0"cd /d "%~dp0"



echo 📦 Verificando dependencias...echo 📦 Instalando dependencias de Python...

python -c "import dotenv, requests" 2>nulpip install -r requirements.txt

if errorlevel 1 (

    echo 📦 Instalando dependencias...echo 🌐 Iniciando servidor web para archivos estáticos (puerto 8080)...

    pip install -r requirements.txtstart "Servidor Web" python -m http.server 8080

)

echo ⏳ Esperando que el servidor web inicie...

echo ✅ Sistema listo para enviar certificadostimeout /t 2 /nobreak > nul

echo.

echo 📋 Uso: python send_certificate.py "Nombre Completo" "email@dominio.com" "123456789" "certificado.pdf"echo 📧 Iniciando servidor de certificados con Mailgun (puerto 5000)...

echo.python server.py

echo 💡 El sistema enviará automáticamente:

echo    • Certificado al estudianteecho.

echo    • Notificación a gestión humanaecho ✅ Sistema iniciado correctamente!

echo    • Adjunto el archivo PDFecho.

echo.echo 🌐 Aplicación web: http://localhost:8080/evaluacion-final.html

pauseecho 📧 API de certificados: http://localhost:5000
echo.
echo Presiona Ctrl+C para detener los servidores
pause