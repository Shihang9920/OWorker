# Generated by Django 4.1.7 on 2023-04-04 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='ip地址')),
                ('port', models.PositiveIntegerField(verbose_name='端口')),
                ('username', models.CharField(max_length=255, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('status', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='状态')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='server', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
