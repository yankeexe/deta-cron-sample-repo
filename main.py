import os
import smtplib

from deta import app
from dotenv import load_dotenv


load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")


@app.lib.run(action="water")
@app.lib.cron()
def water_notify(event):
    """
    Send notification to drink water.
    """
    email_body = "Drink water. Keep yourself hydrated."
    email = f"Subject: Drink water!! \n\n {email_body}"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, email)
    server.quit()

    return email_body
