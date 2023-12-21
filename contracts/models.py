from django.db import models

# INCOMES: General
class IncomeCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    payer = models.CharField(max_length=200)
    income_category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    payment_day = models.IntegerField(null=True, blank=True)
    payment_monthly = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.recipient} - {self.category}'


class IncomeDetails(models.Model):
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    min_months = models.IntegerField(null=True, blank=True)
    cancellation_period = models.IntegerField(null=True, blank=True)
    notes = models.TextField()


# SPENDS: Contract
class ContractCategory(models.Model):
    name = models.CharField(max_length=200)
    desciption = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    recipient = models.CharField(max_length=200)
    category = models.ForeignKey(ContractCategory, on_delete=models.CASCADE)
    payment_day = models.IntegerField(null=True, blank=True)
    payment_monthly = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
    payment_period = models.IntegerField(null=True, blank=True)
    payment_sum = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.recipient} - {self.category}'


class ContractDetails(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    customer_id = models.CharField(null=True, blank=True)
    tariff = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    min_months = models.IntegerField(null=True, blank=True)
    fixed_price_term = models.IntegerField(null=True, blank=True)
    cancellation_period = models.IntegerField(null=True, blank=True)
    notes = models.TextField()


# SPENDS: TrasferOrder
class TransferOrderCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class TransferOrder(models.Model):
    recipient = models.CharField(max_length=200)
    category = models.ForeignKey(TransferOrderCategory, on_delete=models.CASCADE)
    payment_day = models.IntegerField(null=True, blank=True)
    payment_monthly = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.recipient} - {self.category}'


class TransferOrderDetails(models.Model):
    transfer_order = models.ForeignKey(TransferOrder, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField()


# SPENDS: Pocket
class PocketCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Pocket(models.Model):
    recipient = models.CharField(max_length=200)
    category = models.ForeignKey(PocketCategory, on_delete=models.CASCADE)
    payment_day = models.IntegerField(null=True, blank=True)
    payment_monthly = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.recipient} - {self.category}'


class PocketDetails(models.Model):
    pocket = models.ForeignKey(Pocket, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField()


# SPENDS: Budget
class BudgetCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Budget(models.Model):
    recipient = models.CharField(max_length=200)
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    payment_day = models.IntegerField(null=True, blank=True)
    payment_monthly = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.recipient} - {self.category}'


class BudgetDetails(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField()
