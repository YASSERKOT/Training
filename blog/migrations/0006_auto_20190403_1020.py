# Generated by Django 2.2 on 2019-04-03 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190403_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Post'),
        ),
    ]