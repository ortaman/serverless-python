
import csv
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def validate_csv_transactions(csv_dir, customer_id) -> tuple:

    with open(csv_dir, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_transactions = ()

        for row in csv_reader:
            try:
                transaction_id = int(row.get('Id'))
                transaction_date = datetime.datetime.strptime(row.get('Date'), '%Y-%m-%d')
                transaction_amount = float(row.get("Transaction"))

            except Exception as exception:
                logger.error(exception)
                # TODO: Save incorrect transactions

            data_transactions += ((transaction_id, transaction_date, transaction_amount, customer_id),)

        return data_transactions
