# Generated by Django 4.2.3 on 2023-07-29 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EmployeeApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employees",
            old_name="EmployeeName",
            new_name="EmployeeName",
        ),
    ]
