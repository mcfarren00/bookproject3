# Generated by Django 3.2 on 2023-06-13 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0005_auto_20230612_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(1, '1'), (3, '3'), (0, '0'), (4, '4'), (2, '2'), (5, '5')]),
        ),
    ]
