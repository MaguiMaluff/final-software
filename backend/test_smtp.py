import smtplib

server = "smtp.gmail.com"
port = 587
username = "maguimalu4@gmail.com"
password = "atcu seqg orqm dwea"

try:
    with smtplib.SMTP(server, port) as smtp:
        smtp.starttls()
        smtp.login(username, password)
        print("SMTP connection successful!")
except Exception as e:
    print(f"SMTP connection failed: {e}")
