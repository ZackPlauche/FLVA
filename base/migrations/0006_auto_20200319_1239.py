# Generated by Django 3.0 on 2020-03-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200319_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('in_person', 'In Person'), ('online', 'Online')], default='Online', max_length=20, null=True),
        ),
    ]
