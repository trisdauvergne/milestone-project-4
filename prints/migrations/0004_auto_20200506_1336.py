# Generated by Django 3.0.6 on 2020-05-06 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0003_print_designer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.CharField(max_length=254, verbose_name='A few words about this work')),
                ('size', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
                ('image', models.ImageField(upload_to='previews/')),
                ('designer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prints.Designer')),
            ],
            options={
                'verbose_name': 'Prints',
            },
        ),
        migrations.DeleteModel(
            name='Print',
        ),
    ]
