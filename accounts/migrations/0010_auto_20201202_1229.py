# Generated by Django 3.1.3 on 2020-12-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201202_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geeksmodel',
            name='customer_id',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
    ]