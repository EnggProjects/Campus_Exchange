# Generated by Django 5.1.1 on 2024-10-04 05:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
        ('users', '0002_alter_customuser_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.college'),
        ),
    ]
