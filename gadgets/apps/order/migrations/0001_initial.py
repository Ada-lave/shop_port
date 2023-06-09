# Generated by Django 4.1.7 on 2023-05-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=128)),
                ('place', models.CharField(max_length=128)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('paidAmount', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
