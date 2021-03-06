# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-18 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0016_auto_20190318_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap3alertplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3alertplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3blockquoteplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3blockquoteplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3buttonplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3buttonplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3citeplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3citeplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3iconplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3iconplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3imageplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3imageplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3jumbotronplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3jumbotronplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3labelplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3labelplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3panelbodyplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3panelbodyplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3panelfooterplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3panelfooterplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3panelheadingplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3panelheadingplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3panelplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3panelplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3spacerplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3spacerplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3wellplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_bootstrap3_bootstrap3wellplugin', serialize=False, to='cms.CMSPlugin'),
        ),
    ]
