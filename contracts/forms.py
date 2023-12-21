from django import forms

from contracts.models import Income, \
                IncomeCategory, \
                IncomeDetails, \
                \
                Contract, \
                ContractCategory, \
                ContractDetails, \
                \
                TransferOrder, \
                TransferOrderCategory, \
                TransferOrderDetails, \
                \
                Pocket, \
                PocketCategory, \
                PocketDetails, \
                \
                Budget, \
                BudgetCategory, \
                BudgetDetails


class AddIncomeForm(forms.ModelForm):
    payer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter payer'}))
    income_category = forms.ModelChoiceField(queryset=IncomeCategory.objects.all(), empty_label='Select Category')
    payment_day = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter payment day'}), required=False)
    payment_monthly = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Enter monthly payment sum'}))

    class Meta:
        model = Income
        fields = ['payer', 'income_category', 'payment_day', 'payment_monthly']


    def save(self, commit=True):
        income = super().save(commit=commit)

        # Now, create a ContractDetails instance linked to this contract
        # Note: Fill in the fields for ContractDetails as needed. Here it's left blank.
        if commit:
            IncomeDetails.objects.create(income=income)

        return income


class AddContractForm(forms.ModelForm):
    recipient = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter recipient'}))
    category = forms.ModelChoiceField(queryset=ContractCategory.objects.all(), empty_label='Select Category')
    payment_day = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter payment day'}), required=False)
    payment_monthly = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Enter monthly payment sum'}))
    payment_period = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter payment period in months'}))
    payment_sum = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Enter total payment sum'}))

    class Meta:
        model = Contract
        fields = ['recipient', 'category', 'payment_day', 'payment_monthly', 'payment_period', 'payment_sum']


    def save(self, commit=True):
        contract = super().save(commit=commit)

        # Now, create a ContractDetails instance linked to this contract
        # Note: Fill in the fields for ContractDetails as needed. Here it's left blank.
        if commit:
            ContractDetails.objects.create(contract=contract)

        return contract


class AddTransferOrderForm(forms.ModelForm):
    recipient = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter recipient'}))
    category = forms.ModelChoiceField(queryset=TransferOrderCategory.objects.all(), empty_label='Select Category')
    payment_day = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter payment day'}), required=False)
    payment_monthly = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Enter monthly payment sum'}))

    class Meta:
        model = TransferOrder
        fields = ['recipient', 'category', 'payment_day', 'payment_monthly']


    def save(self, commit=True):
        transfer_order = super().save(commit=commit)

        # Now, create a ContractDetails instance linked to this contract
        # Note: Fill in the fields for ContractDetails as needed. Here it's left blank.
        if commit:
            TransferOrderDetails.objects.create(transfer_order=transfer_order)

        return transfer_order


class AddPocketForm(forms.ModelForm):
    recipient = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter recipient'}))
    category = forms.ModelChoiceField(queryset=PocketCategory.objects.all(), empty_label='Select Category')
    payment_day = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter payment day'}), required=False)
    payment_monthly = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Enter monthly payment sum'}))

    class Meta:
        model = Pocket
        fields = ['recipient', 'category', 'payment_day', 'payment_monthly']


    def save(self, commit=True):
        pocket = super().save(commit=commit)

        # Now, create a ContractDetails instance linked to this contract
        # Note: Fill in the fields for ContractDetails as needed. Here it's left blank.
        if commit:
            PocketDetails.objects.create(pocket=pocket)

        return pocket


class AddBudgetForm(forms.ModelForm):
    recipient = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter recipient'}))
    category = forms.ModelChoiceField(queryset=BudgetCategory.objects.all(), empty_label='Select Category')
    payment_day = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter payment day'}), required=False)
    payment_monthly = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Enter monthly payment sum'}))

    class Meta:
        model = Budget
        fields = ['recipient', 'category', 'payment_day', 'payment_monthly']


    def save(self, commit=True):
        budget = super().save(commit=commit)

        # Now, create a ContractDetails instance linked to this contract
        # Note: Fill in the fields for ContractDetails as needed. Here it's left blank.
        if commit:
            BudgetDetails.objects.create(budget=budget)

        return budget
