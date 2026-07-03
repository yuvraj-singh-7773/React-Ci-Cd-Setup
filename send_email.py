import os
import smtplib

email = os.getenv("EMAIL")
password = os.getenv("EMAIL_PSWD")
receiver = os.getenv("HR_EMAIL")
workflow = os.getenv("WORKFLOW_NAME")

subject = workflow + " Failed"
message = f"""Subject: {subject}

Hello,

Your {workflow} has failed.

Repository: {os.getenv("GITHUB_REPOSITORY")}

Run Link:
https://github.com/{os.getenv("GITHUB_REPOSITORY")}/actions/runs/{os.getenv("GITHUB_RUN_ID")}
"""

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, receiver, message)
    server.quit()
    print("Email Sent Successfully")
except Exception as e:
    print("Email Failed")
    print(e)