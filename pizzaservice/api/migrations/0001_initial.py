# Generated by Django 2.0.7 on 2018-07-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('pizza_id', models.IntegerField(primary_key=1, serialize=False)),
                ('pizza_size', models.IntegerField(max_length=2)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_address', models.CharField(max_length=250)),
            ],
        ),
    ]
