# Generated by Django 3.1.4 on 2020-12-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20201202_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='geeksmodel',
            name='image',
            field=models.ImageField(blank='True', upload_to='media'),
        ),
    ]
