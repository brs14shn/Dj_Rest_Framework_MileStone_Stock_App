# Generated by Django 4.1.1 on 2022-10-07 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0002_alter_transaction_price_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction",
            field=models.SmallIntegerField(choices=[("1", "IN"), ("0", "OUT")]),
        ),
    ]
