from contracts.models import  Income, IncomeDetails, \
                Contract, ContractDetails, \
                TransferOrder, TransferOrderDetails, \
                Pocket, PocketDetails, \
                Budget, BudgetDetails


def contracts(request):
    return {'incomes': Income.objects.all(),
        'income_details': IncomeDetails.objects.all(),
        'contracts': Contract.objects.all(),
        'contract_details': ContractDetails.objects.all(),
        'transfer_orders': TransferOrder.objects.all(),
        'transfer_order_details': TransferOrderDetails.objects.all(),
        'pockets': Pocket.objects.all(),
        'pocket_details': PocketDetails.objects.all(),
        'budgets': Budget.objects.all(),
        'budget_details': BudgetDetails.objects.all(),
        }
