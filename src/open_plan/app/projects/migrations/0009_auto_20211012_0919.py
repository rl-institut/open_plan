# Generated by Django 3.2 on 2021-10-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20211012_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='maxemissionconstraint',
            name='name',
            field=models.CharField(default='min_renewable_constraint', editable=False, max_length=30),
        ),
        migrations.AddField(
            model_name='mindoaconstraint',
            name='name',
            field=models.CharField(default='min_renewable_constraint', editable=False, max_length=30),
        ),
        migrations.AddField(
            model_name='minrenewableconstraint',
            name='name',
            field=models.CharField(default='min_renewable_constraint', editable=False, max_length=30),
        ),
        migrations.AddField(
            model_name='nzeconstraint',
            name='name',
            field=models.CharField(default='min_renewable_constraint', editable=False, max_length=30),
        ),
    ]
