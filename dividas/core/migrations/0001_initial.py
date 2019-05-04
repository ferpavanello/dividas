# Generated by Django 2.2.1 on 2019-05-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Divida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.CharField(max_length=100)),
                ('motivo', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField()),
            ],
            options={
                'verbose_name': 'divida',
                'verbose_name_plural': 'dividas',
                'db_table': 'divida',
            },
        ),
    ]