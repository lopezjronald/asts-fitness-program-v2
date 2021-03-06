# Generated by Django 3.1.3 on 2020-11-27 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airman',
            fields=[
                ('airman_id', models.AutoField(primary_key=True, serialize=False)),
                ('fitness_level', models.CharField(choices=[('Excellent', 'EXCELLENT'), ('Satisfactory', 'SATISFACTORY'), ('Pass', 'PASS'), ('Unsatisfactory', 'UNSATISFACTORY'), ('Fail', 'FAIL'), ('Exemption', 'EXEMPTION')], default='satisfactory', max_length=50)),
                ('rank', models.CharField(choices=[('AB', 'AB'), ('Amn', 'Amn'), ('A1C', 'A1C'), ('SrA', 'SrA'), ('SSgt', 'SSgt'), ('TSgt', 'TSgt'), ('MSgt', 'MSgt'), ('SMSgt', 'SMSgt'), ('CMSgt', 'CMSgt'), ('2nd Lt', '2nd Lt'), ('1st Lt', '1st Lt'), ('Capt', 'Capt'), ('Maj', 'Maj'), ('Lt Col', 'Lt Col'), ('Col', 'Col'), ('Brig Gen', 'Brig Gen'), ('Maj Gen', 'Maj Gen'), ('Lt Gen', 'Lt Gen'), ('Gen', 'General')], default='AB', max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_initial', models.CharField(max_length=5)),
                ('last_name', models.CharField(max_length=50)),
                ('ssn', models.IntegerField()),
                ('airman_slug', models.SlugField(unique_for_date='test_date')),
                ('test_date', models.DateField()),
                ('ptl', models.BooleanField(default=False)),
                ('ufpm', models.BooleanField(default=False)),
                ('active_status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='Physical_Training_Leader',
            fields=[
                ('ptl_id', models.AutoField(primary_key=True, serialize=False)),
                ('ptl_certification_date', models.DateField()),
                ('ptl_expiration_date', models.DateField()),
                ('cpr_expiration_date', models.DateField()),
                ('airman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.airman')),
            ],
            options={
                'ordering': ('ptl_expiration_date',),
            },
        ),
        migrations.CreateModel(
            name='Unit_Fitness_Program_Manager',
            fields=[
                ('ufpm_id', models.AutoField(primary_key=True, serialize=False)),
                ('ufpm_certification_date', models.DateField()),
                ('ufpm_expiration_date', models.DateField()),
                ('airman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.airman')),
                ('ptl_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.physical_training_leader')),
            ],
            options={
                'ordering': ('ufpm_expiration_date',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_start_date', models.DateField()),
                ('profile_expiration_date', models.DateField()),
                ('profile_details', models.TextField()),
                ('airman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.airman')),
            ],
            options={
                'ordering': ('profile_expiration_date',),
            },
        ),
        migrations.CreateModel(
            name='Naughty',
            fields=[
                ('naughty_id', models.AutoField(primary_key=True, serialize=False)),
                ('failure_date', models.DateField()),
                ('be_well_completion_date', models.DateField()),
                ('status_level', models.CharField(choices=[('Fail', 'FAIL'), ('Unsatisfactory', 'UNSATISFACTORY'), ('Non-Current', 'NON-CURRENT')], max_length=50)),
                ('airman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.airman')),
            ],
            options={
                'ordering': ('-failure_date',),
            },
        ),
    ]
