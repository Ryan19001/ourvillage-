# Generated by Django 3.0 on 2019-12-25 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_quest2check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest2check',
            name='answer',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Quest2Check')),
            ],
        ),
    ]
