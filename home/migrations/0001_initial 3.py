# Generated by Django 4.0.5 on 2022-07-29 18:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True)),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('NON_BINARY', 'Non-Binary')], max_length=10)),
                ('dob', models.DateField(max_length=11)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Account',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(default='NA', max_length=100)),
                ('country', models.CharField(default='NA', max_length=20)),
                ('city', models.CharField(default='NA', max_length=45)),
                ('zipcode', models.IntegerField(default=0)),
                ('state', models.CharField(default='NA', max_length=45)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='generalUser',
            fields=[
                ('trackingID', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'generalUser',
            },
        ),
        migrations.CreateModel(
            name='Supportstaff',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('staff_email', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'SupportStaff',
            },
        ),
        migrations.CreateModel(
            name='Requestsupport',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=52)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('REP', 'Report User or Content'), ('ONB', 'Registration Issues'), ('BUG', 'PlayDate Not Working'), ('OTH', 'Other')], default='ONB', max_length=3)),
                ('details', models.TextField(max_length=500)),
                ('accountID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('general', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.generaluser')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.supportstaff')),
            ],
            options={
                'db_table': 'RequestSupport',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('is_verified', models.BooleanField(auto_created=True, default=False)),
                ('profileID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profileDesc', models.TextField(blank=True, default=None, max_length=256, null=True)),
                ('avatar', models.ImageField(blank=True, default=None, upload_to='uploads')),
                ('verification', models.ImageField(blank=True, default=None, upload_to='verification', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'apng', 'tiff', 'avif', 'webp'])])),
                ('date_verified', models.DateTimeField(default=None, null=True)),
                ('address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='home.address')),
            ],
            options={
                'db_table': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Friendlist',
            fields=[
                ('friend_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'FriendList',
            },
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('dependent_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('dob', models.DateTimeField()),
                ('interests', models.CharField(max_length=45)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.profile')),
            ],
            options={
                'db_table': 'Dependent',
            },
        ),
        migrations.CreateModel(
            name='Backendadmin',
            fields=[
                ('backend_admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BackendAdmin',
                'unique_together': {('backend_admin_id', 'user')},
            },
        ),
    ]
