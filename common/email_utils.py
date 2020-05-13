# encoding : utf-8
# @Author : tiamo Cao
# @Time : 2020/5/10 9:16
# title : 测试结果以邮件形式发送

import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common import zip_utils
from common.config_utils import local_config


class EmailUtils:
    def __init__(self, smtp_subject, smtp_body, smtp_file_path=None):
        self.smtp_server = local_config.smtp_receiver
        self.smtp_sender = local_config.smtp_sender
        self.smtp_senderpassword = local_config.smtp_senderpassword
        self.smtp_receiver = local_config.smtp_receiver
        self.smtp_cc = local_config.smtp_cc  # 抄送
        self.smtp_subject = '自动化测试报告'  # 邮件主题
        self.smtp_body = '来自python邮件测试'  # 邮件正文
        self.smtp_file = smtp_file_path

    def mail_content(self):
        if self.smtp_file != None:
            if self.smtp_file.split('.')[-1].__eq__('zip'):
                return self.__zip_content()
        else:
            return self.__mail_text_content()

    def mail_content_by_zip(self):
        report_zip_path = self.smtp_file + '/../禅道自动化测试报告.zip'
        zip_utils.zip_dir(self.smtp_file, report_zip_path)
        self.smtp_file = report_zip_path  # 更新文件，文件变成 *.zip
        msg = self.mail_content()
        return msg

    def __mail_text_content(self):
        msg = MIMEText(self.smtp_body, 'html', 'utf-8')
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def __zip_content(self):
        msg = MIMEMultipart()
        with open(self.smtp_file, 'rb') as f:
            mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
            mime.add_header('Content-Disposition', 'attachment',
                            filename=('gb2312', '', self.smtp_file.split('/')[-1]))
            mime.add_header('Content-ID', '<0>')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
        msg.attach(MIMEText(self.smtp_body, 'html', 'utf-8'))
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def send_mail(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        mail_contetn = self.mail_content()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split('.') + self.smtp_cc.split('.'),
                          mail_contetn.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()

    def zip_send_mail(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        mail_contetn = self.mail_content()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split('.') + self.smtp_cc.split('.'),
                          mail_contetn.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()