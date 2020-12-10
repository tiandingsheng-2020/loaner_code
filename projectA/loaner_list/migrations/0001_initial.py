# Generated by Django 3.1.3 on 2020-11-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loaner',
            fields=[
                ('loaner_id', models.AutoField(primary_key=True, serialize=False)),
                ('loaner_sn', models.TextField(verbose_name='SN')),
                ('loaner_request', models.TextField(verbose_name='外借人')),
                ('request_time', models.DateTimeField(auto_now=True, verbose_name='外借时间')),
                ('loaner_status', models.BooleanField(verbose_name='是否归还')),
            ],
        ),
    ]