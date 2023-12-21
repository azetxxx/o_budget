from django.contrib import admin

from contracts.models import  IncomeCategory, \
                Income, \
                IncomeDetails, \
                \
                ContractCategory, \
                Contract, \
                ContractDetails, \
                \
                TransferOrderCategory, \
                TransferOrder, \
                TransferOrderDetails, \
                \
                PocketCategory, \
                Pocket, \
                PocketDetails, \
                \
                BudgetCategory, \
                Budget, \
                BudgetDetails


admin.site.register(IncomeCategory)
admin.site.register(Income)
admin.site.register(IncomeDetails)
admin.site.register(ContractCategory)
admin.site.register(Contract)
admin.site.register(ContractDetails)
admin.site.register(TransferOrderCategory)
admin.site.register(TransferOrder)
admin.site.register(TransferOrderDetails)
admin.site.register(PocketCategory)
admin.site.register(Pocket)
admin.site.register(PocketDetails)
admin.site.register(BudgetCategory)
admin.site.register(Budget)
admin.site.register(BudgetDetails)
