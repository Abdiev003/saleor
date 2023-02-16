# Generated by Django 1.10.3 on 2017-01-13 12:38
from __future__ import unicode_literals

import django.contrib.sites.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "domain",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        validators=[
                            django.contrib.sites.models._simple_domain_name_validator
                        ],
                        verbose_name="domain",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                (
                    "header_text",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="header text"
                    ),
                ),
            ],
        )
    ]
