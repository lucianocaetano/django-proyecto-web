# Generated by Django 5.0 on 2024-01-02 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_categoria_options_alter_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.categoria'),
            preserve_default=False,
        ),
    ]