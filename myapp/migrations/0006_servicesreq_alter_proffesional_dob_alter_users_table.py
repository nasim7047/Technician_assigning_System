# Generated by Django 4.2 on 2023-05-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_work_proffesional_work_experiece'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicesreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('phone', models.IntegerField()),
                ('services', models.CharField(max_length=100)),
                ('technician', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'service_details',
            },
        ),
        migrations.AlterField(
            model_name='proffesional',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterModelTable(
            name='users',
            table='user_details',
        ),
    ]
