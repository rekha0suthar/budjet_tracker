# Generated by Django 5.2.1 on 2025-05-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_budget_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('SALARY', 'Salary'), ('GROCERY', 'Grocery'), ('ENTERTAINMENT', 'Entertainment'), ('RENT', 'Rent'), ('OTHERS', 'Others')], max_length=20),
        ),
    ]
