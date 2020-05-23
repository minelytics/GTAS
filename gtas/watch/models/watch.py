from django.db import models
from gtas.watch.models.delete import SoftDeletionModel
import reversion


@reversion.register()
class GraphRuleParameters(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    keyvalue = models.CharField(db_column='keyValue', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    parametertype = models.CharField(db_column='parameterType', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    ruleparameter = models.CharField(db_column='ruleParameter', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    graphrule = models.ForeignKey('GraphRules', models.DO_NOTHING, db_column='graphRule_id', blank=True,
                                  null=True)  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'graph_rule_parameters'


@reversion.register()
class GraphRules(SoftDeletionModel):
    cipherquery = models.CharField(db_column='cipherQuery', max_length=10000, blank=True,
                                   null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    displaycondition = models.CharField(db_column='displayCondition', max_length=255, blank=True,
                                        null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    id = models.OneToOneField('HitMaker', models.DO_NOTHING, db_column='id', primary_key=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'graph_rules'


@reversion.register()
class HitCategory(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(unique=True, max_length=255)
    severity = models.IntegerField()
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hit_category'


@reversion.register()
class HitDetail(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    flight = models.ForeignKey(Flight, models.DO_NOTHING, db_column='flight')
    hitenum = models.CharField(db_column='hitEnum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hm = models.ForeignKey('HitMaker', models.DO_NOTHING)
    hit_type = models.CharField(max_length=3)
    passenger = models.ForeignKey('Passenger', models.DO_NOTHING, db_column='passenger', blank=True, null=True)
    percentage_match = models.FloatField(blank=True, null=True)
    cond_text = models.TextField(blank=True, null=True)
    rule_id = models.BigIntegerField()
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hit_detail'


@reversion.register()
class HitMaker(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    hm_hit_type = models.CharField(max_length=255)
    hm_author = models.ForeignKey(User, models.DO_NOTHING, db_column='hm_author')
    hm_hit_category = models.ForeignKey(HitCategory, models.DO_NOTHING, db_column='hm_hit_category')
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hit_maker'


@reversion.register()
class HitViewStatus(SoftDeletionModel):
    id = models.BigIntegerField()
    hv_status = models.CharField(max_length=255)
    hv_hit_detail = models.OneToOneField(HitDetail, models.DO_NOTHING, db_column='hv_hit_detail', primary_key=True)
    hv_passenger = models.ForeignKey('Passenger', models.DO_NOTHING)
    hv_user_group = models.ForeignKey('UserGroup', models.DO_NOTHING, db_column='hv_user_group')
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hit_view_status'
        unique_together = (('hv_hit_detail', 'hv_user_group'),)


@reversion.register()
class HitsSummary(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    flight = models.ForeignKey(Flight, models.DO_NOTHING, blank=True, null=True)
    hs_graph_count = models.IntegerField(blank=True, null=True)
    hs_manual_count = models.IntegerField(blank=True, null=True)
    hs_partial_count = models.IntegerField(blank=True, null=True)
    hs_passenger = models.ForeignKey('Passenger', models.DO_NOTHING, blank=True, null=True)
    hs_rule_count = models.IntegerField(blank=True, null=True)
    hs_wl_count = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hits_summary'


@reversion.register()
class KnowledgeBase(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    creation_dt = models.DateTimeField(db_column='CREATION_DT')  # Field name made lowercase.
    kb_blob = models.BinaryField(db_column='KB_BLOB')  # Field name made lowercase.
    kb_name = models.CharField(db_column='KB_NAME', max_length=20)  # Field name made lowercase.
    rl_blob = models.BinaryField(db_column='RL_BLOB')  # Field name made lowercase.
    version = models.BigIntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'knowledge_base'


@reversion.register()
class ManualLookout(SoftDeletionModel):
    description = models.CharField(max_length=255, blank=True, null=True)
    id = models.OneToOneField(HitMaker, models.DO_NOTHING, db_column='id', primary_key=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'manual_lookout'


@reversion.register()
class Rule(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    rule_criteria = models.CharField(db_column='RULE_CRITERIA', max_length=1024, blank=True,
                                     null=True)  # Field name made lowercase.
    rule_drl = models.CharField(db_column='RULE_DRL', max_length=4000, blank=True,
                                null=True)  # Field name made lowercase.
    rule_indx = models.IntegerField(db_column='RULE_INDX', blank=True, null=True)  # Field name made lowercase.
    kb_ref = models.ForeignKey(KnowledgeBase, models.DO_NOTHING, db_column='KB_REF', blank=True,
                               null=True)  # Field name made lowercase.
    udr_rule_ref = models.ForeignKey('UdrRule', models.DO_NOTHING,
                                     db_column='UDR_RULE_REF')  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'rule'


@reversion.register()
class RuleMeta(SoftDeletionModel):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=1024, blank=True,
                                   null=True)  # Field name made lowercase.
    enable_flag = models.CharField(db_column='ENABLE_FLAG', max_length=1)  # Field name made lowercase.
    end_dt = models.DateTimeField(db_column='END_DT', blank=True, null=True)  # Field name made lowercase.
    hit_share_flag = models.CharField(db_column='HIT_SHARE_FLAG', max_length=1)  # Field name made lowercase.
    rm_over_max_hits_flag = models.TextField(db_column='RM_OVER_MAX_HITS_FLAG', blank=True,
                                             null=True)  # Field name made lowercase. This field type is a guess.
    high_priority_flag = models.CharField(db_column='HIGH_PRIORITY_FLAG', max_length=1)  # Field name made lowercase.
    start_dt = models.DateTimeField(db_column='START_DT')  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=20)  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'rule_meta'


@reversion.register()
class UdrRule(SoftDeletionModel):
    del_id = models.BigIntegerField(db_column='DEL_ID')  # Field name made lowercase.
    del_flag = models.CharField(db_column='DEL_FLAG', max_length=1)  # Field name made lowercase.
    edit_dt = models.DateTimeField(db_column='EDIT_DT')  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', unique=True, max_length=20)  # Field name made lowercase.
    udr_blob = models.BinaryField(db_column='UDR_BLOB', blank=True, null=True)  # Field name made lowercase.
    id = models.OneToOneField(HitMaker, models.DO_NOTHING, db_column='id', primary_key=True)
    edited_by = models.ForeignKey(User, models.DO_NOTHING, db_column='EDITED_BY')  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'udr_rule'


@reversion.register()
class UdrRuleCat(SoftDeletionModel):
    udr_rule = models.OneToOneField(RuleMeta, models.DO_NOTHING, primary_key=True)
    rule_cat = models.ForeignKey(HitCategory, models.DO_NOTHING)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'udr_rule_cat'
        unique_together = (('udr_rule', 'rule_cat'),)


@reversion.register()
class UgHitCategoryJoin(SoftDeletionModel):
    ug = models.OneToOneField('UserGroup', models.DO_NOTHING, primary_key=True)
    hc = models.ForeignKey(HitCategory, models.DO_NOTHING)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'ug_hit_category_join'
        unique_together = (('ug', 'hc'),)


@reversion.register()
class UgUserJoin(SoftDeletionModel):
    ug = models.OneToOneField('UserGroup', models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'ug_user_join'
        unique_together = (('ug', 'user'),)


@reversion.register()
class WatchList(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    wl_edit_dttm = models.DateTimeField(db_column='WL_EDIT_DTTM')  # Field name made lowercase.
    wl_entity = models.CharField(db_column='WL_ENTITY', max_length=20)  # Field name made lowercase.
    wl_name = models.CharField(db_column='WL_NAME', unique=True, max_length=64)  # Field name made lowercase.
    wl_editor = models.ForeignKey(User, models.DO_NOTHING, db_column='WL_EDITOR')  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'watch_list'


@reversion.register()
class WhiteList(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    del_flag = models.CharField(db_column='DEL_FLAG', max_length=1)  # Field name made lowercase.
    dob = models.DateField(blank=True, null=True)
    document_number = models.CharField(max_length=255)
    document_type = models.CharField(max_length=3)
    expiration_date = models.DateField(blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    issuance_country = models.CharField(max_length=255, blank=True, null=True)
    issuance_date = models.DateField(blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    residency_country = models.CharField(max_length=255, blank=True, null=True)
    editor = models.ForeignKey(User, models.DO_NOTHING, db_column='editor')
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'white_list'


@reversion.register()
class WlItem(SoftDeletionModel):
    itm_data = models.TextField(db_column='ITM_DATA')  # Field name made lowercase.
    itm_rl_data = models.TextField(db_column='ITM_RL_DATA')  # Field name made lowercase.
    id = models.OneToOneField(HitMaker, models.DO_NOTHING, db_column='id', primary_key=True)
    itm_wl_ref = models.ForeignKey(WatchList, models.DO_NOTHING, db_column='ITM_WL_REF')  # Field name made lowercase.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'wl_item'
