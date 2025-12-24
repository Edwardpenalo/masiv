import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

# Datos
df = pd.read_excel("lista_correos.xlsx")  # tu lista
cv_file = "edward_penalo_cv.pdf"
certificados_file = "certificados_edward.pdf"
link_portafolio = "https://edwardpenalo.netlify.app"

# Configura tu correo
from_email = "epenalo42@gmail.com"
password = "mbns vwgb cxpo mwcl"  # mejor clave de aplicación

# Conexión al servidor Gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(from_email, password)

for correo in df["Correo"]:
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = correo
    msg["Subject"] = "Vacantes Ciberseguridad"

    cuerpo = f"""
    Me dirijo a usted para expresar mi interés en la vacante de TI en su empresa. Con sólidos conocimientos  técnicos y una pasión por la resolución de problemas, estoy seguro de que puedo contribuir positivamente a su equipo.

Mi objetivo es aplicar mis habilidades técnicas para brindar un servicio eficiente y efectivo a los usuarios, asegurando el funcionamiento óptimo de los sistemas informáticos de la empresa.

Estoy disponible para una entrevista en cualquier momento que le resulte conveniente y quedo a su disposición para proporcionar cualquier información adicional que pueda necesitar.                                  

 Nota de enfoque: estimados/as me interesa destacar que mantengo mi apertura para adaptarme en una posición, según sea
considerada mi perfil.
    """

    msg.attach(MIMEText(cuerpo, "plain"))

    for file in [cv_file, certificados_file]:
        with open(file, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={file}")
            msg.attach(part)

    server.sendmail(from_email, correo, msg.as_string())

server.quit()
