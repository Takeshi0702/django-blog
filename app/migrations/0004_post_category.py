# Generated by Django 2.2.15 on 2020-08-27 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Category', verbose_name='カテゴリ'),
            preserve_default=False,
        ),
    ]