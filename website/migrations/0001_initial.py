# Generated by Django 2.1.1 on 2018-09-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('name', models.TextField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Тэги',
            },
        ),
    ]
