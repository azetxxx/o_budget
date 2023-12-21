from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from contracts.views import IncomeListView, \
                AddIncomeFormView, \
                IncomeDetailsListView, \
                \
                ContractsListView, \
                AddContractFormView, \
                ContractsDetailsListView, \
                \
                AddTransferOrderFormView, \
                \
                AddPocketFormView, \
                \
                AddBudgetFormView, \
                timeline_view


app_name = 'contracts'

urlpatterns = [
    path('income/', IncomeListView.as_view(), name='income_overview'),
    path('income_add/', AddIncomeFormView.as_view(), name='income_add'),
    path('income_details/', IncomeDetailsListView.as_view(), name='income_details'),

    path('spends/', ContractsListView.as_view(), name='spends_overview'),
    path('spends_add/', AddContractFormView.as_view(), name='spends_add'),
    path('spends_details/', ContractsDetailsListView.as_view(), name='spends_details'),

    path('transfer_order_add/', AddTransferOrderFormView.as_view(), name='transfer_order_add'),

    path('pocket_add/', AddPocketFormView.as_view(), name='pocket_add'),

    path('budget_add/', AddBudgetFormView.as_view(), name='budget_add'),

    path('timeline/', timeline_view, name='timeline'),

]
