# Generated by Django 5.0 on 2023-12-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_course_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='academicyear',
            field=models.CharField(choices=[('2022-23', '2022-23'), ('2023-24', '2023-24'), ('2024-25', '2024-25')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10),
        ),
    ]
