# Generated by Django 5.0 on 2024-04-18 12:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_energydieelfilling_global_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreMonsoonImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to='att_pmcl/%y', verbose_name='Images')),
            ],
        ),
        migrations.CreateModel(
            name='PMCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q1_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q1_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q1_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q2_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q2_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q2_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q3_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q3_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q3_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q4_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q4_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q4_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q5_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q5_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q5_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q6_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q6_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q6_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q7_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q7_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q7_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q8_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q8_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q8_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q9_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q9_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q9_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('Q10_Status', models.CharField(choices=[('Ok', 'Ok'), ('Not Ok', 'Not Ok')], max_length=10, verbose_name='Status')),
                ('Q10_Material_Required', models.TextField(null=True, verbose_name='Material_Required')),
                ('Q10_Remarks', models.TextField(null=True, verbose_name='Remarks')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Time')),
                ('global_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sitefixed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Q10_Attach', models.ManyToManyField(related_name='Q10_Attach', to='app.premonsoonimages')),
                ('Q1_Attach', models.ManyToManyField(related_name='Q1_Attach', to='app.premonsoonimages')),
                ('Q2_Attach', models.ManyToManyField(related_name='Q2_Attach', to='app.premonsoonimages')),
                ('Q3_Attach', models.ManyToManyField(related_name='Q3_Attach', to='app.premonsoonimages')),
                ('Q4_Attach', models.ManyToManyField(related_name='Q4_Attach', to='app.premonsoonimages')),
                ('Q5_Attach', models.ManyToManyField(related_name='Q5_Attach', to='app.premonsoonimages')),
                ('Q6_Attach', models.ManyToManyField(related_name='Q6_Attach', to='app.premonsoonimages')),
                ('Q7_Attach', models.ManyToManyField(related_name='Q7_Attach', to='app.premonsoonimages')),
                ('Q8_Attach', models.ManyToManyField(related_name='Q8_Attach', to='app.premonsoonimages')),
                ('Q9_Attach', models.ManyToManyField(related_name='Q9_Attach', to='app.premonsoonimages')),
            ],
        ),
    ]
