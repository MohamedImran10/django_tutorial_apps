# Generated by Django 4.2.11 on 2024-07-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField(unique=True)),
                ('emp_name', models.CharField(max_length=200)),
                ('basic_salary', models.FloatField()),
            ],
        ),
    ]
