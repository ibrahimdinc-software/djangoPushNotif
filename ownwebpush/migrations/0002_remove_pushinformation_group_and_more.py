# Generated by Django 4.0.4 on 2022-07-10 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pushuser', '0005_alter_pushmessagemodel_detail'),
        ('ownwebpush', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pushinformation',
            name='group',
        ),
        migrations.RemoveField(
            model_name='subscriptioninfo',
            name='user_agent',
        ),
        migrations.AlterField(
            model_name='pushinformation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webpush_info', to='pushuser.pushusermodel'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
