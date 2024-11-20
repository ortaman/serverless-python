

def save_or_get_customer_by_email(db, email):
    customer = db.get(f"SELECT * FROM customer WHERE email='{email}'")

    if not customer:
        query = "INSERT INTO customer(email) VALUES (%s) RETURNING customer_id"
        data = (email,)

        customer = db.save(query, data)

    return customer[0]


def save_transactions(db, data):

    query = b"INSERT INTO transactions(id, trans_date, amount, customer_id) VALUES "
    db.save_many(query, data)
