# Generated by Django 3.0 on 2019-12-26 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191226_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest2check',
            name='answer',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
