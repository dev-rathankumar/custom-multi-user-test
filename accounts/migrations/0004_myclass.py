# Generated by Django 3.1.3 on 2020-12-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClass',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
