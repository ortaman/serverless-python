import os


class PSQLConfig:

    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

    POSTGRES_DB = os.environ['POSTGRES_DB']
    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_PORT = os.environ['POSTGRES_PORT']


class SMTPConfig:
    STMP_TEMPLATE_DIR = "txns_template.html"
    STMP_FILE_LOADER = "utils/templates"

    EMAIL_SUBJECT = 'STORI CHALLENGE'

    EMAIL_USER = os.environ['EMAIL_USER']
    EMAIL_CODE = os.environ['EMAIL_CODE']

    EMAIL_FROM = os.environ['EMAIL_FROM']
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_PORT = os.environ['EMAIL_PORT']
