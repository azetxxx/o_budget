from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from common.views import CommonContextMixin
from contracts.models import Income, IncomeDetails, \
                Contract, ContractDetails, \
                TransferOrder, TransferOrderDetails, \
                Pocket, PocketDetails, \
                Budget, BudgetDetails
from contracts.forms import AddIncomeForm, AddContractForm, AddTransferOrderForm, AddPocketForm, AddBudgetForm

from datetime import datetime, timedelta


# INCOMES VIEWS
class IncomeListView(CommonContextMixin, ListView):
    model = Income
    template_name = 'contracts/income_overview.html'
    title = 'Income Overview'


class AddIncomeFormView(CommonContextMixin, FormView):
    template_name = 'contracts/income_add.html'
    form_class = AddIncomeForm
    title = 'Add Income'
    success_url = reverse_lazy('contracts:income_overview')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()  # save the new contract
        return super().form_valid(form)


class IncomeDetailsListView(CommonContextMixin, ListView):
    model = IncomeDetails
    template_name = 'contracts/income_details.html'
    title = 'Income Details'


# SPENDS VIEWS
### SPENDS: Contracts
class ContractsListView(CommonContextMixin, ListView):
    model = Contract
    template_name = 'contracts/contracts_overview.html'
    title = 'Contracts Overview'


class AddContractFormView(CommonContextMixin, FormView):
    template_name = 'contracts/contracts_add.html'
    form_class = AddContractForm
    title = 'Add Contract'
    success_url = reverse_lazy('contracts:spends_overview')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()  # save the new contract
        return super().form_valid(form)


class ContractsDetailsListView(CommonContextMixin, ListView):
    model = ContractDetails
    template_name = 'contracts/contracts_details.html'
    title = 'Contracts Details'


### SPENDS: TransferOrders
class AddTransferOrderFormView(CommonContextMixin, FormView):
    template_name = 'contracts/transfer_order_add.html'
    form_class = AddTransferOrderForm
    title = 'Add Transfer Order'
    success_url = reverse_lazy('contracts:spends_overview')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()  # save the new contract
        return super().form_valid(form)


### SPENDS: Pocket
class AddPocketFormView(CommonContextMixin, FormView):
    template_name = 'contracts/pocket_add.html'
    form_class = AddPocketForm
    title = 'Add Pocket'
    success_url = reverse_lazy('contracts:spends_overview')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()  # save the new contract
        return super().form_valid(form)


### SPENDS: Budget
class AddBudgetFormView(CommonContextMixin, FormView):
    template_name = 'contracts/budget_add.html'
    form_class = AddBudgetForm
    title = 'Add Budget'
    success_url = reverse_lazy('contracts:spends_overview')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.save()  # save the new contract
        return super().form_valid(form)



# TIMELINE
def timeline_view(request):
    months = generate_monthly_datetimes(2023, 2024)

    #Contracts
    contracts = Contract.objects.all()
    all_contracts_monthly_spends = {}
    contracts_monthly_sums = []

    for contract in contracts:
        contract_detail = ContractDetails.objects.get(contract=contract)
        contract_monthly_spends = []

        if not contract_detail.start_date and not contract_detail.end_date:
            contract_monthly_spends = [float(contract.payment_monthly) for month in months]
        else:
            for month in months:
                if contract_detail.start_date <= month.date() and contract_detail.end_date >= month.date():
                    contract_monthly_spends.append(float(contract.payment_monthly))
                else:
                    contract_monthly_spends.append('-')

        all_contracts_monthly_spends[contract.id] = contract_monthly_spends

    for i in range(len(months)):
        contracts_month_sum = sum(value[i] for value in all_contracts_monthly_spends.values() if isinstance(value[i], (int, float)))

        contracts_monthly_sums.append(contracts_month_sum)


    #TransferOrders
    transfer_orders = TransferOrder.objects.all()
    all_transfer_orders_monthly_spends = {}
    transfer_orders_monthly_sums = []

    for transfer_order in transfer_orders:
        transfer_order_detail = TransferOrderDetails.objects.get(transfer_order=transfer_order)
        transfer_order_monthly_spends = []

        if not transfer_order_detail.start_date and not transfer_order_detail.end_date:
            transfer_order_monthly_spends = [float(transfer_order.payment_monthly) for month in months]
        else:
            for month in months:
                if transfer_order_detail.start_date <= month.date() and transfer_order_detail.end_date >= month.date():
                    transfer_order_monthly_spends.append(float(transfer_order.payment_monthly))
                else:
                    transfer_order_monthly_spends.append('-')

        all_transfer_orders_monthly_spends[transfer_order.id] = transfer_order_monthly_spends

    for i in range(len(months)):
        transfer_orders_month_sum = sum(value[i] for value in all_transfer_orders_monthly_spends.values() if isinstance(value[i], (int, float)))

        transfer_orders_monthly_sums.append(transfer_orders_month_sum)


    #Pocket
    pockets = Pocket.objects.all()
    all_pockets_monthly_spends = {}
    pockets_monthly_sums = []

    for pocket in pockets:
        pocket_detail = PocketDetails.objects.get(pocket=pocket)
        pocket_monthly_spends = []

        if not pocket_detail.start_date and not pocket_detail.end_date:
            pocket_monthly_spends = [float(pocket.payment_monthly) for month in months]
        else:
            for month in months:
                if pocket_detail.start_date <= month.date() and pocket_detail.end_date >= month.date():
                    pocket_monthly_spends.append(float(pocket.payment_monthly))
                else:
                    pocket_monthly_spends.append('-')

        all_pockets_monthly_spends[pocket.id] = pocket_monthly_spends

    for i in range(len(months)):
        pockets_month_sum = sum(value[i] for value in all_pockets_monthly_spends.values() if isinstance(value[i], (int, float)))

        pockets_monthly_sums.append(pockets_month_sum)



    return render(request, 'contracts/timeline.html', {
        'months': months,
        'all_contracts_monthly_spends': all_contracts_monthly_spends,
        'contracts_monthly_sums': contracts_monthly_sums,
        'all_transfer_orders_monthly_spends': all_transfer_orders_monthly_spends,
        'transfer_orders_monthly_sums': transfer_orders_monthly_sums,
        'all_pockets_monthly_spends': all_pockets_monthly_spends,
        'pockets_monthly_sums': pockets_monthly_sums,
    })








# Generate a list of datetime objects
def generate_monthly_datetimes(start_year, end_year):
    datetime_list = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            date_obj = datetime(year, month, 1)
            datetime_list.append(date_obj)
    return datetime_list
