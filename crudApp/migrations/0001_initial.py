# Generated by Django 4.1.2 on 2022-11-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('sclass', models.IntegerField()),
                ('saddress', models.CharField(max_length=100)),
            ],
        ),
    ]
