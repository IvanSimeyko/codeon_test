# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=25, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88\xd0\xb5 \xd0\xb8\xd0\xbc\xd1\x8f')),
                ('contact_subject', models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('contact_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('contact_email', models.EmailField(max_length=254, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88 email \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd0\xb0')),
                ('contact_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
        ),
    ]
