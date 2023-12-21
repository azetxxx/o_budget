import os
import csv
import django
from decimal import Decimal

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'o_budget.settings')
django.setup()

from contracts.models import Contract, ContractCategory  # noqa: E402
from django.db import transaction  # noqa: E402

def import_contracts_from_csv(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        contracts_to_create = []
        for row in reader:
            category_name = row['category']  # Assumes 'category' is a column in your CSV
            # Get or create the ContractCategory instance
            category, created = ContractCategory.objects.get_or_create(name=category_name)

            contract = Contract(
                recipient=row['recipient'],
                category=category,
                payment_day=int(row['payment_day']) if row['payment_day'] else None,
                payment_monthly=Decimal(row['payment_monthly']) if row['payment_monthly'] else None,
                payment_period=int(row['payment_period']) if row['payment_period'] else None,
                payment_sum=Decimal(row['payment_sum']) if row['payment_sum'] else None,
            )
            contracts_to_create.append(contract)

        # Use atomic transaction to ensure all contracts are created or none at all
        with transaction.atomic():
            Contract.objects.bulk_create(contracts_to_create)


if __name__ == '__main__':
    # Provide the correct path to your CSV file
    import_contracts_from_csv('static/contracts_overview.csv')
