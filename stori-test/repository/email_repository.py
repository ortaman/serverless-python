
import email.message
import smtplib

from jinja2 import Environment, FileSystemLoader


class SmtpEmail:

    def __init__(self, smtp_config):
        self.smtp_config = smtp_config

    def _generate_body(self, transactions_by_month, transactions_resume) -> str:

        environment = Environment(loader=FileSystemLoader(self.smtp_config.STMP_FILE_LOADER))
        template = environment.get_template(self.smtp_config.STMP_TEMPLATE_DIR)

        template_render = template.render(
            transactions_by_month=transactions_by_month,
            transactions_resume=transactions_resume
        )
        return template_render

    def send_email_smtp(self, email_to_send: str, transactions_by_month: dict, transactions_resume: dict) -> None:
        msg = email.message.Message()

        msg['Subject'] = self.smtp_config.EMAIL_SUBJECT
        msg['From'] = self.smtp_config.EMAIL_FROM
        msg['To'] = email_to_send

        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(self._generate_body(transactions_by_month, transactions_resume))

        with smtplib.SMTP(host=self.smtp_config.EMAIL_HOST, port=int(self.smtp_config.EMAIL_PORT)) as server:

            server.starttls()
            server.login(user=self.smtp_config.EMAIL_USER, password=self.smtp_config.EMAIL_CODE)

            server.sendmail(
                from_addr=self.smtp_config.EMAIL_FROM,
                to_addrs=email_to_send,
                msg=msg.as_string()
            )