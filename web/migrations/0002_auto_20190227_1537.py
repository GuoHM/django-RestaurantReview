# Generated by Django 2.1.7 on 2019-02-27 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='master_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Review'),
        ),
    ]
