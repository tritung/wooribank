# Generated by Django 3.1 on 2020-08-22 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wooribank', '0001_initial'),
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaninfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wooribank.userinfo'),
        ),
    ]
