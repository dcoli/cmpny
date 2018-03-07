# Generated by Django 2.0.2 on 2018-03-04 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20180224_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_specific_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.Person'),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(default='Still to come 2018-03-04 13:15:15.145081+00:00', max_length=1024),
        ),
    ]