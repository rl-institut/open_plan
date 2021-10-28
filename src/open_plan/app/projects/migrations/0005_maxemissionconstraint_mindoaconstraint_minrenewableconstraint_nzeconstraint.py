# Generated by Django 3.2 on 2021-09-29 21:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_delete_dummyscenario'),
    ]

    operations = [
        migrations.CreateModel(
            name='NZEConstraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('activated', models.BooleanField(choices=[(None, 'Choose'), (True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('value', models.BooleanField(choices=[(None, 'Choose'), (True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.scenario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MinRenewableConstraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('activated', models.BooleanField(choices=[(None, 'Choose'), (True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('value', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.scenario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MinDOAConstraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('activated', models.BooleanField(choices=[(None, 'Choose'), (True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('value', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.scenario')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaxEmissionConstraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('activated', models.BooleanField(choices=[(None, 'Choose'), (True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('value', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.scenario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
