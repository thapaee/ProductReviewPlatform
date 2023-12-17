# Generated by Django 3.1 on 2020-08-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer_company', '0005_reviewer_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
