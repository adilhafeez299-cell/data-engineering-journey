from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path


html_template = Template(Path('Templates/Template_html_file.html').read_text())
# print(html_template)
# print(html_template.is_valid())


html_content = html_template.substitute({'name': 'Adil', 'date': 'tomorrow'})

my_email = EmailMessage()
my_email['From'] = 'Adil <Adil@example.com>'
my_email['To'] = 'test@test.com'
my_email['Subject'] = 'Hello from Python'
my_email.set_content(html_content, 'html')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    smtp_server.send_message(my_email)
    print("email was sent")