# Generated by Django 4.1.1 on 2022-11-23 17:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_userprofile_profile_contact_phonecountrycode_and_more'),
        ('organization', '0005_alter_organization_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('jobType', models.CharField(max_length=20)),
                ('description', ckeditor.fields.RichTextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('skillSet', models.ManyToManyField(to='profiles.skill')),
            ],
        ),
    ]
