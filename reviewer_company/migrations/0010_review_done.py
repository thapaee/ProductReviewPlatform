# Generated by Django 3.1 on 2020-09-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer_company', '0009_questions_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='review_done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('reviewer_id', models.CharField(max_length=20)),
            ],
        ),
    ]
