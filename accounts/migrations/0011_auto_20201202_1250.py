# Generated by Django 3.1.3 on 2020-12-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201202_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='customer_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]