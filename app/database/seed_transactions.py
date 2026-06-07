from faker import Faker

from app.database.connection import SessionLocal
from app.models.transaction import Transaction, TransactionStatus

from datetime import datetime, timedelta

import random

fake = Faker()

COMPANIES = ["Reliance Retail", "TCS", "Infosys", "Wipro", "HCL Technologies", "Tech Mahindra", "ABC Electronics", "Global Traders", "Metro Retail",
             "Prime Distributors", "National Supplies", "Future Enterprises", "Vertex Solutions", "Smart Distribution Pvt Ltd", "United Retail", "NextGen Technologies"]

def get_status(invoice_sequence):

    if invoice_sequence <= 30:
        return TransactionStatus.COMPLETED

    elif invoice_sequence <= 35:
        return TransactionStatus.FAILED

    elif invoice_sequence <= 45:
        return TransactionStatus.VALIDATED

    else:
        return TransactionStatus.PENDING


def seed_transactions(count=50):

    db = SessionLocal()

    try:

        transactions = []

        base_date = datetime.now() - timedelta(days=3)

        for invoice_sequence in range(1, count + 1):

            created_at = base_date + timedelta(minutes=invoice_sequence * 60)

            transaction = Transaction(customer_name=random.choice(COMPANIES), invoice_number=f"INV-2026-{invoice_sequence:06}", amount=random.randint(5000, 500000),
                                      status=get_status(invoice_sequence), created_at=created_at)

            transactions.append(transaction)

        db.add_all(transactions)

        db.commit()

        print(f"{count} transactions inserted successfully!")

    except Exception as error:

        db.rollback()

        print(f"Seeding failed: {error}")

    finally:

        db.close()

if __name__ == "__main__":

    seed_transactions()