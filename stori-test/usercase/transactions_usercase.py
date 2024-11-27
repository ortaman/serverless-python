from adapters import db_adapters

class TnxsResume:
    def __init__(self, db, smtp_email):
        self.db = db
        self.smtp_email = smtp_email

    def calculate_transactions_resume(self, data_transactions: tuple[tuple]) -> tuple[dict, dict]:

        total_balance = 0
        debit_average = 0
        debit_transactions_number = 0
        credit_average = 0
        credit_transactions_number = 0
        transactions_by_month = {}

        for data_transaction in data_transactions:

            month_name = data_transaction[1].strftime("%B")

            transactions_by_month[month_name] = transactions_by_month.get(month_name, 0) + 1
            total_balance += data_transaction[2]

            transaction_amount = data_transaction[2]

            if transaction_amount < 0:
                debit_average += data_transaction[2]
                debit_transactions_number += 1
            else:
                credit_average += data_transaction[2]
                credit_transactions_number += 1

        transactions_resume = {
            'average_debit': debit_average / debit_transactions_number,
            'average_credit': credit_average / credit_transactions_number,
            'total_balance': total_balance,
        }

        return transactions_by_month, transactions_resume

    def send_transactions_email(self, email_to_send: str, data_transactions: tuple[tuple]) -> None:
        transactions_by_month, transactions_resume = self.calculate_transactions_resume(data_transactions)
        self.smtp_email.send_email_smtp(email_to_send, transactions_by_month, transactions_resume)

    def save_transactions(self, data_transactions: tuple[tuple]) -> None:
        db_adapters.save_transactions(self.db, data_transactions)
