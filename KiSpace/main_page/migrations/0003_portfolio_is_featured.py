# Generated by Django 4.1 on 2023-09-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0002_remove_portfolio_external_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="is_featured",
            field=models.BooleanField(default=False, help_text="是否为精选作品"),
        ),
    ]
