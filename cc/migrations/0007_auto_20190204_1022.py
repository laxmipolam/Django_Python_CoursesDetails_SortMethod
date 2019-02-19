# Generated by Django 2.1.5 on 2019-02-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0006_auto_20190204_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('c', 'Closed'), ('a', 'Available'), ('w', 'WaitList')], default='w', help_text='Course availability', max_length=1),
        ),
    ]