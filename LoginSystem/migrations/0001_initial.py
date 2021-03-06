# Generated by Django 3.2.4 on 2021-06-23 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalData',
            fields=[
                ('Hospital_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('address', models.CharField(max_length=80)),
                ('regNo', models.BigIntegerField(unique=True)),
                ('phoneNo', models.BigIntegerField(unique=True)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('test', models.CharField(max_length=20)),
                ('pincode', models.BigIntegerField()),
            ],
            options={
                'db_table': 'Hospital Data',
            },
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=40, unique=True)),
                ('gender', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=80)),
                ('blood_group', models.CharField(max_length=20)),
                ('phoneNo', models.BigIntegerField(unique=True)),
                ('id_proof_name', models.CharField(max_length=20)),
                ('id_proof_no', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'User Data',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.BigIntegerField()),
                ('hospital_id', models.ForeignKey(db_column='Hospital_ID', default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='+', to='LoginSystem.hospitaldata')),
            ],
            options={
                'db_table': 'Test',
            },
        ),
    ]
