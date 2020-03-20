# Generated by Django 3.0 on 2020-03-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200318_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('event_date', models.DateTimeField(null=True)),
                ('event_type', models.CharField(choices=[('In Person', 'in person'), ('Online', 'online')], max_length=20, null=True)),
                ('location', models.URLField(blank=True, help_text='Enter the link to the location of the event.', null=True)),
            ],
        ),
    ]