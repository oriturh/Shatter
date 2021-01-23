# Generated by Django 3.1.4 on 2021-01-23 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20210123_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='thread',
            name='link',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='board',
            name='link',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='post',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.board', verbose_name='Board'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.thread', verbose_name='Thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='boards.board', verbose_name='Board'),
        ),
    ]