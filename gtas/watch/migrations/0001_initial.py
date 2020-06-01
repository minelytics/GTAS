# Generated by Django 3.0.5 on 2020-05-24 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20200525_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255, unique=True)),
                ('severity', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hitcategory_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hitcategory_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hit_category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HitMaker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hm_hit_type', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hitmaker_createdby', to=settings.AUTH_USER_MODEL)),
                ('hm_author', models.ForeignKey(db_column='hm_author', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('hm_hit_category', models.ForeignKey(db_column='hm_hit_category', on_delete=django.db.models.deletion.DO_NOTHING, to='watch.HitCategory')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hitmaker_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hit_maker',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='KnowledgeBase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('kb_blob', models.BinaryField(null=True)),
                ('kb_name', models.CharField(max_length=20, null=True)),
                ('rl_blob', models.BinaryField(db_column='RL_BLOB')),
                ('version', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='knowledgebase_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='knowledgebase_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'knowledge_base',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RuleMeta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('enable_flag', models.CharField(max_length=1)),
                ('end_dt', models.DateTimeField(blank=True, null=True)),
                ('hit_share_flag', models.CharField(max_length=1)),
                ('rm_over_max_hits_flag', models.TextField(blank=True, null=True)),
                ('high_priority_flag', models.CharField(max_length=1)),
                ('start_dt', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rulemeta_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rulemeta_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rule_meta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GraphRules',
            fields=[
                ('hit_maker', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='watch.HitMaker')),
                ('cipher_query', models.CharField(blank=True, max_length=10000, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('display_condition', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'graph_rules',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ManualLookout',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='watch.HitMaker')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'manual_lookout',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UdrRule',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='watch.HitMaker')),
                ('del_id', models.BigIntegerField()),
                ('del_flag', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=20, unique=True)),
                ('udr_blob', models.BinaryField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'udr_rule',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UdrRuleCat',
            fields=[
                ('udr_rule', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='watch.RuleMeta')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'udr_rule_cat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WhiteList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dob', models.DateField(blank=True, null=True)),
                ('document_number', models.CharField(max_length=255)),
                ('document_type', models.CharField(max_length=3)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=2, null=True)),
                ('issuance_country', models.CharField(blank=True, max_length=255, null=True)),
                ('issuance_date', models.DateField(blank=True, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('residency_country', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='whitelist_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='whitelist_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'white_list',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wl_entity', models.CharField(max_length=20)),
                ('wl_name', models.CharField(max_length=64, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='watchlist_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='watchlist_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'watch_list',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UgHitCategoryJoin',
            fields=[
                ('ug', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='users.UserGroup')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ughitcategoryjoin_createdby', to=settings.AUTH_USER_MODEL)),
                ('hc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='watch.HitCategory')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ughitcategoryjoin_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ug_hit_category_join',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_criteria', models.CharField(blank=True, max_length=1024, null=True)),
                ('rule_drl', models.CharField(blank=True, max_length=4000, null=True)),
                ('rule_index', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rule_createdby', to=settings.AUTH_USER_MODEL)),
                ('kb_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='watch.KnowledgeBase')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rule_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rule',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GraphRuleParameters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key_value', models.CharField(blank=True, max_length=255, null=True)),
                ('parameter_type', models.CharField(blank=True, max_length=255, null=True)),
                ('rule_parameter', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='graphruleparameters_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='graphruleparameters_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'graph_rule_parameters',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WlItem',
            fields=[
                ('item_data', models.TextField()),
                ('item_rl_data', models.TextField()),
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='watch.HitMaker')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wlitem_createdby', to=settings.AUTH_USER_MODEL)),
                ('itm_wl_ref', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='watch.WatchList')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='wlitem_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'wl_item',
                'managed': True,
            },
        ),
        migrations.AddConstraint(
            model_name='ughitcategoryjoin',
            constraint=models.UniqueConstraint(fields=('ug', 'hc'), name='unique_ug_hc'),
        ),
        migrations.AddField(
            model_name='udrrulecat',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='udrrulecat_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='udrrulecat',
            name='rule_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='watch.HitCategory'),
        ),
        migrations.AddField(
            model_name='udrrulecat',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='udrrulecat_updatedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='udrrule',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='udrrule_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='udrrule',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='udrrule_updatedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rule',
            name='udr_rule_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='watch.UdrRule'),
        ),
        migrations.AddField(
            model_name='manuallookout',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='manuallookout_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='manuallookout',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='manuallookout_updatedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='hitcategory',
            constraint=models.UniqueConstraint(fields=('category',), name='unique_category'),
        ),
        migrations.AddField(
            model_name='graphrules',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='graphrules_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='graphrules',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='graphrules_updatedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='graphruleparameters',
            name='graph_rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='watch.GraphRules'),
        ),
        migrations.AddConstraint(
            model_name='udrrulecat',
            constraint=models.UniqueConstraint(fields=('udr_rule', 'rule_cat'), name='unique_udr_rule_rule_cat'),
        ),
    ]