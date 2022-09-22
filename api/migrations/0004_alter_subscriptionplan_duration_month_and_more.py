# Generated by Django 4.1.1 on 2022-09-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_subscriptionplan_sharable_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='duration_month',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
