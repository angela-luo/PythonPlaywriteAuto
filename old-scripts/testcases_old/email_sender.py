"""
Utility for sending email reports
utilities/email_sender.py
Author:  Angel
Created Date: 2025-06-05
"""

import smtplib
import os
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from utils_old.testcases_old import email_config
from config.config import Config


def send_email():
    """
    发送测试报告邮件
    """
    # Email configuration
    sender = email_config.EMAIL_SENDER
    password = email_config.EMAIL_PASSWORD
    receivers = email_config.EMAIL_RECEIVERS
    smtp_server = email_config.SMTP_SERVER
    smtp_port = email_config.SMTP_PORT

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ", ".join(receivers)
    msg['Subject'] = "PetStore Automation Test Report"

    # Email body
    body = """
    <html>
    <body>
        <h2>PetStore自动化测试报告</h2>
        <p>本次测试已完成，请查收附件中的测试报告。</p>
        <p>报告包含详细的测试结果、日志和截图。</p>
        <p>自动化测试团队</p>
    </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))

    # 压缩报告目录
    zip_filename = "allure-report.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(Config.ALLURE_REPORT_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, Config.ALLURE_REPORT_DIR))

    # 添加报告附件
    print("添加报告附件")
    with open(zip_filename, 'rb') as f:
        part = MIMEApplication(f.read(), Name=os.path.basename(zip_filename))
    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_filename)}"'
    msg.attach(part)

    # 发送邮件
    print("准备发送邮件")
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receivers, msg.as_string())
        print("邮件发送成功!")
    except Exception as e:
        print(f"邮件发送失败: {e}")
    # finally:
    #     # 清理临时文件
    #     if os.path.exists(zip_filename):
    #         os.remove(zip_filename)