# Generated by Django 4.1.1 on 2022-11-18 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_experience_enddate'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='companySize',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='profile',
        ),
        migrations.AddField(
            model_name='organization',
            name='companyCover',
            field=models.ImageField(default='cover.png', upload_to='organization/'),
        ),
        migrations.AddField(
            model_name='organization',
            name='companyLogo',
            field=models.ImageField(default='defaultProfile.jpg', upload_to='organization/'),
        ),
        migrations.AddField(
            model_name='organization',
            name='website',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.website'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='companyName',
            field=models.CharField(default='company', max_length=300),
        ),
    ]
