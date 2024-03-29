# Generated by Django 5.0 on 2023-12-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_course_academicyear_alter_course_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('Cse(Regular)', 'CSE(R)'), ('CSE(Honors)', 'CSE(H)'), ('CS&IT', 'CSIT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(choices=[('Prof.', 'professor'), ('Assoc . prof.', 'Associate Professor'), ('Asst . prof.', 'Assistant professor')], max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE ')], max_length=10),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('ph.D', 'ph.D')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('Cse(Regular)', 'CSE(R)'), ('CSE(Honors)', 'CSE(H)'), ('CS&IT', 'CSIT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE ')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10),
        ),
    ]
