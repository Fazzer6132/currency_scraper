# Generated by Django 3.2 on 2022-06-24 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_caller', '0002_auto_20220613_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'currency', 'verbose_name_plural': 'currencies'},
        ),
        migrations.AlterModelOptions(
            name='currencyraterecord',
            options={'verbose_name': 'currency rate record', 'verbose_name_plural': 'currency rate records'},
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='currency',
            name='description',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='currencyraterecord',
            name='base_curr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='base_currency_rate_records', to='api_caller.currency', verbose_name='Currency (Base)'),
        ),
        migrations.AlterField(
            model_name='currencyraterecord',
            name='curr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='currency_rate_records', to='api_caller.currency', verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='currencyraterecord',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
        migrations.AlterField(
            model_name='currencyraterecord',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]