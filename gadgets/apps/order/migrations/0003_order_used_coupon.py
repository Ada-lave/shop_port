# Generated by Django 4.1.7 on 2023-05-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orederitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='used_coupon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]