import json
import logging

from adapters import txns_adapters, db_adapters
from infra import db_infra
from repository import db_repository, email_repository
from usercase import transactions_usercase

logger = logging.getLogger()
CSV_DIR = 'utils/data/transactions.csv'


def lambda_handler(event, context):

    # Validate the body request
    if not event.get('body'):
        return {
            'statusCode': 400,
            'body': 'body empty'
        }

    body = json.loads(event['body'])

    # Validate that email not null
    if not body.get('email'):
        return {
            'statusCode': 400,
            'body': 'email field empty',
        }

    email_to_send = body['email']

    psql_config = db_infra.PSQLConfig()
    db = db_repository.PostgresDb(psql_config)

    email_config = db_infra.SMTPConfig()
    smtp_email = email_repository.SmtpEmail(email_config)

    customer_id = db_adapters.save_or_get_customer_by_email(db, email_to_send)
    data_transactions = txns_adapters.validate_csv_transactions(CSV_DIR, None)

    tnxs_resume = transactions_usercase.TnxsResume(db, smtp_email)
    tnxs_resume.save_transactions(data_transactions)
    tnxs_resume.send_transactions_email(email_to_send, data_transactions)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"email sent to {email_to_send}",
        }),
    }
