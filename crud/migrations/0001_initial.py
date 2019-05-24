# Generated by Django 2.2.1 on 2019-05-20 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrp', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=50)),
                ('umur', models.IntegerField()),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(max_length=1)),
                ('alamat', models.CharField(max_length=255)),
            ],
        ),
    ]