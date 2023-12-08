import smtplib, ssl, mimetypes
from email.message import EmailMessage

## Dados do email
password = open("password", "r").read()
from_email = "*****@gmail.com"
to_email = "*****@gmail.com"
subject = "Planilha"
body = """
********
*****
***********
****
******
"""

## Estrutura do email
message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

## Adição de anexos
anexo = "mod_barchart.xlsx"
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    a.read()
    maintype = mime_type
    subtype = mime_subtype
    filename = anexo

## Envio de email
port = 333 ## Exemplo
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
