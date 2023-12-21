# Generated by Django 4.2.7 on 2023-12-03 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desciption', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=200)),
                ('payment_day', models.IntegerField(blank=True, null=True)),
                ('payment_monthly', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('payment_period', models.IntegerField(blank=True, null=True)),
                ('payment_sum', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.category')),
            ],
        ),
        migrations.CreateModel(
            name='ContractDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(blank=True, null=True)),
                ('tariff', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('min_months', models.IntegerField(blank=True, null=True)),
                ('fixed_price_term', models.IntegerField(blank=True, null=True)),
                ('cancellation_period', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.contract')),
            ],
        ),
    ]
