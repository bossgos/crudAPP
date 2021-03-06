# Generated by Django 3.2.3 on 2021-05-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
                ('student_first_name', models.CharField(max_length=100)),
                ('student_last_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=100)),
                ('student_address', models.CharField(max_length=100)),
                ('student_phone', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'student_data',
            },
        ),
    ]
