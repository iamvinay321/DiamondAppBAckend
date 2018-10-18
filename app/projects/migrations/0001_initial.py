# Generated by Django 2.1.1 on 2018-10-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procore_index', models.FloatField(blank=True, null=True)),
                ('pjm_index', models.DecimalField(blank=True, decimal_places=10, max_digits=28, null=True)),
                ('system_of_origin', models.CharField(max_length=7)),
                ('project', models.CharField(max_length=53)),
                ('project_number', models.CharField(blank=True, max_length=15, null=True)),
                ('project_description', models.CharField(blank=True, max_length=35, null=True)),
                ('address', models.CharField(blank=True, max_length=71, null=True)),
                ('city', models.CharField(blank=True, max_length=35, null=True)),
                ('state', models.CharField(blank=True, max_length=9, null=True)),
                ('zip', models.CharField(blank=True, max_length=15, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('project_stage', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.CharField(blank=True, max_length=255, null=True)),
                ('last_updated', models.CharField(blank=True, max_length=255, null=True)),
                ('procore_status', models.BooleanField(blank=True, null=True)),
                ('sage_status', models.CharField(blank=True, max_length=25, null=True)),
                ('project_status', models.CharField(max_length=8)),
                ('Construction_Type', models.CharField(blank=True, max_length=20, null=True)),
                ('product_type', models.CharField(blank=True, max_length=20, null=True)),
                ('size', models.BigIntegerField(blank=True, null=True)),
                ('estimated_start', models.DateTimeField(default=None, null=True)),
                ('revised_start', models.DateTimeField(default=None, null=True)),
                ('actual_start', models.DateTimeField(default=None, null=True)),
                ('estimated_completion', models.DateTimeField(default=None, null=True)),
                ('revised_completion', models.DateTimeField(default=None, null=True)),
                ('actual_completion', models.DateTimeField(default=None, null=True)),
                ('customer_id', models.CharField(blank=True, max_length=15, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=55, null=True)),
                ('architect', models.CharField(blank=True, max_length=255, null=True)),
                ('division', models.CharField(blank=True, max_length=22, null=True)),
                ('contract_type', models.CharField(blank=True, max_length=255, null=True)),
                ('team_leader', models.CharField(blank=True, max_length=255, null=True)),
                ('project_managers', models.CharField(blank=True, max_length=255, null=True)),
                ('superintendents', models.CharField(blank=True, max_length=255, null=True)),
                ('original_contract_value', models.FloatField(blank=True, null=True)),
                ('approved_contract_changes', models.FloatField(blank=True, null=True)),
                ('revised_contract_value', models.FloatField(blank=True, null=True)),
                ('jtd_work_billed', models.FloatField(blank=True, null=True)),
                ('jtd_retainage_held', models.FloatField(blank=True, null=True)),
                ('jtd_payments_received', models.FloatField(blank=True, null=True)),
                ('original_estimated_cost', models.FloatField(blank=True, null=True)),
                ('approved_estimate_changes', models.FloatField(blank=True, null=True)),
                ('revised_estimated_cost', models.FloatField(blank=True, null=True)),
                ('original_committed_cost', models.FloatField(blank=True, null=True)),
                ('approved_commitment_changes', models.FloatField(blank=True, null=True)),
                ('revised_committed_cost', models.FloatField(blank=True, null=True)),
                ('jtd_cost', models.FloatField(blank=True, null=True)),
                ('jtd_payments_made', models.FloatField(blank=True, null=True)),
                ('projected_post', models.FloatField(blank=True, null=True)),
                ('original_gp', models.FloatField(blank=True, null=True)),
                ('projected_gp', models.DecimalField(blank=True, decimal_places=10, max_digits=28, null=True)),
                ('original_gp_percent', models.FloatField(blank=True, null=True)),
                ('projected_gp_percent', models.FloatField(blank=True, null=True)),
                ('gain_fade', models.FloatField(blank=True, null=True)),
                ('gain_fade_percent', models.FloatField(blank=True, null=True)),
                ('database_stamp', models.CharField(max_length=4)),
            ],
            options={
                'managed': True,
                'db_table': 'project_master',
            },
        ),
    ]
