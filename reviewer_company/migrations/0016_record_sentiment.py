# Generated by Django 3.1 on 2020-09-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer_company', '0015_question_answer_question4'),
    ]

    operations = [
        migrations.CreateModel(
            name='record_sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=20)),
                ('reviewer_id', models.CharField(max_length=20)),
            ],
        ),
    ]