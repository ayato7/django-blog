# Generated by Django 3.2.6 on 2021-09-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0002_alter_biography_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biography',
            options={'verbose_name': 'biography', 'verbose_name_plural': 'my biography'},
        ),
        migrations.AlterField(
            model_name='biography',
            name='instagram',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
