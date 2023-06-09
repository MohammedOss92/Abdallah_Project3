# Generated by Django 4.1.1 on 2022-12-05 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Msgs_Api', '0002_alter_msgstypes_new_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeesageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MsgTypes', models.CharField(max_length=100, null=True)),
                ('new_msg', models.CharField(default=1, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MessageName', models.CharField(max_length=1000, null=True)),
                ('new_msgs', models.CharField(default=1, max_length=2, null=True)),
                ('ID_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Msgs_Api.meesagetype')),
            ],
        ),
    ]
