# Generated by Django 3.2.25 on 2024-05-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(db_column='FeedBack_id', primary_key=True, serialize=False)),
                ('feedback', models.CharField(db_column='Feedback', max_length=45)),
                ('date', models.DateField(db_column='Date')),
                ('type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'feedback',
                'managed': False,
            },
        ),
    ]
