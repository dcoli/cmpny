# Generated by Django 2.0.2 on 2018-02-20 15:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('jobs', '0004_auto_20180218_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMPUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=1024)),
                ('admin_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.CMPUser')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start date')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='email_primary',
        ),
        migrations.AddField(
            model_name='employer',
            name='contact_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.Person'),
        ),
        migrations.AddField(
            model_name='cmpuser',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.Person'),
        ),
    ]
