import os


class PSQLConfig:

    POSTGRES_USER = os.environ['DB_USER']
    POSTGRES_PASSWORD = os.environ['DB_PASS']

    POSTGRES_DB = os.environ['DB_NAME']
    POSTGRES_HOST = os.environ['DB_HOST']
    POSTGRES_PORT = os.environ['DB_PORT']


class SMTPConfig:
    STMP_TEMPLATE_DIR = "txns_template.html"
    STMP_FILE_LOADER = "utils/templates"

    EMAIL_SUBJECT = 'STORI CHALLENGE'

    EMAIL_FROM = os.environ['SMTP_FROM']
    EMAIL_USER = os.environ['SMTP_USER']
    EMAIL_CODE = os.environ['SMTP_CODE']

    EMAIL_HOST = os.environ['SMTP_HOST']
    EMAIL_PORT = os.environ['SMTP_PORT']
