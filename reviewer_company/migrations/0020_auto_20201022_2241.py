# Generated by Django 3.1 on 2020-10-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer_company', '0019_auto_20201021_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_answer',
            name='question10',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='question_answer',
            name='question5',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='question_answer',
            name='question6',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='question_answer',
            name='question7',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='question_answer',
            name='question8',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='question_answer',
            name='question9',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
