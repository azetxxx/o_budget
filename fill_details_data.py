# fill_details_data.py
import os
import csv
import django
from datetime import datetime

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'o_budget.settings')
django.setup()

from contracts.models import Contract, ContractDetails  # Adjusted import for ContractDetails
from django.db import transaction

def import_contract_details_from_csv(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        details_to_create = []
        for row in reader:
            # You need to find the associated Contract instance or create it if it doesn't exist.
            # I'm assuming you have a way to retrieve or create a Contract instance from the CSV row.
            # Replace 'get_or_create_contract_instance' with your actual logic to get or create a Contract instance.
            contract_instance = get_or_create_contract_instance(row)

            details = ContractDetails(
                contract=contract_instance,
                customer_id=row['customer_id'] if row['customer_id'] else None,
                tariff=row['tariff'],
                start_date=datetime.strptime(row['start_date'], '%Y-%m-%d').date() if row['start_date'] else None,
                end_date=datetime.strptime(row['end_date'], '%Y-%m-%d').date() if row['end_date'] else None,
                min_months=int(row['min_months']) if row['min_months'] else None,
                fixed_price_term=int(row['fixed_price_term']) if row['fixed_price_term'] else None,
                cancellation_period=int(row['cancellation_period']) if row['cancellation_period'] else None,
                notes=row['notes'] if row['notes'] else '',
                contract_id=int(row['contract_id']) if row['contract_id'] else None,
            )
            details_to_create.append(details)

        # Use atomic transaction to ensure all contract details are created or none at all
        with transaction.atomic():
            ContractDetails.objects.bulk_create(details_to_create)

# Replace this with your actual logic for retrieving or creating a Contract instance
def get_or_create_contract_instance(csv_row):
    # Placeholder function - this needs to be implemented based on your CSV structure and logic
    # For example, you might look up a Contract based on a recipient name or create a new one
    contract, created = Contract.objects.get_or_create(id=int(csv_row['contract_id']))
    return contract

if __name__ == '__main__':
    # Provide the correct path to your CSV file
    import_contract_details_from_csv('static/contract_details.csv')
