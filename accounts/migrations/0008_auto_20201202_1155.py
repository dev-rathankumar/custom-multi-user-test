# Generated by Django 3.1.3 on 2020-12-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201202_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('customer_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='MyClass',
        ),
    ]