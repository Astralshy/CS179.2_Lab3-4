# Generated by Django 2.0.3 on 2018-04-12 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='product_cart',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Cart'),
            preserve_default=False,
        ),
    ]
