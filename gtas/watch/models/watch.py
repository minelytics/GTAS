from django.db import models
from gtas.watch.models.delete import SoftDeletionModel

from gtas.users.models import User
from gtas.users.models import UserGroup

import reversion


@reversion.register()
class HitCategory(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    category = models.CharField(unique=True, max_length=255)
    severity = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hit_category'
        constraints = [models.UniqueConstraint(fields=['category'], name='unique_category')]


@reversion.register()
class HitMaker(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    hm_hit_type = models.CharField(max_length=255)
    hm_author = models.ForeignKey(User, models.DO_NOTHING)
    hm_hit_category = models.ForeignKey(HitCategory, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'hit_maker'


@reversion.register()
class GraphRules(SoftDeletionModel):
    hit_maker = models.OneToOneField(HitMaker, models.DO_NOTHING, primary_key=True)
    cipher_query = models.CharField(max_length=10000, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    display_condition = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'graph_rules'


@reversion.register()
class GraphRuleParameters(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    key_value = models.CharField(max_length=255, blank=True, null=True)
    parameter_type = models.CharField(max_length=255, blank=True, null=True)
    rule_parameter = models.CharField(max_length=255, blank=True, null=True)
    graph_rule = models.ForeignKey(GraphRules, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'graph_rule_parameters'


@reversion.register()
class KnowledgeBase(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    kb_blob = models.BinaryField(null=True)
    kb_name = models.CharField(max_length=20, null=True)
    rl_blob = models.BinaryField()
    version = models.BigIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'knowledge_base'


@reversion.register()
class ManualLookout(SoftDeletionModel):
    id = models.OneToOneField(HitMaker, models.DO_NOTHING, primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'manual_lookout'


@reversion.register()
class Rule(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    rule_criteria = models.CharField(max_length=1024, blank=True, null=True)
    rule_drl = models.CharField(max_length=4000, blank=True, null=True)
    rule_index = models.IntegerField(blank=True, null=True)
    kb_ref = models.ForeignKey(KnowledgeBase, models.DO_NOTHING, blank=True, null=True)
    udr_rule_ref = models.ForeignKey('UdrRule', models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'rule'


@reversion.register()
class RuleMeta(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    enable_flag = models.CharField(max_length=1)
    end_dt = models.DateTimeField(blank=True, null=True)
    hit_share_flag = models.CharField(max_length=1)
    rm_over_max_hits_flag = models.TextField(blank=True, null=True)
    high_priority_flag = models.CharField(max_length=1)
    start_dt = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'rule_meta'


@reversion.register()
class UdrRule(SoftDeletionModel):
    id = models.OneToOneField(HitMaker, models.DO_NOTHING, primary_key=True)
    del_id = models.BigIntegerField()
    del_flag = models.CharField(max_length=1)
    title = models.CharField(unique=True, max_length=20)
    udr_blob = models.BinaryField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
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
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'udr_rule_cat'
        constraints = [models.UniqueConstraint(fields=['udr_rule', 'rule_cat'],
                                               name='unique_udr_rule_rule_cat')]


@reversion.register()
class UgHitCategoryJoin(SoftDeletionModel):
    ug = models.OneToOneField(UserGroup, models.DO_NOTHING, primary_key=True)
    hc = models.ForeignKey(HitCategory, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'ug_hit_category_join'
        constraints = [models.UniqueConstraint(fields=['ug', 'hc'],
                                               name='unique_ug_hc')]


@reversion.register()
class WatchList(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    wl_entity = models.CharField(max_length=20)
    wl_name = models.CharField(unique=True, max_length=64)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'watch_list'


@reversion.register()
class WhiteList(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
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
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'white_list'


@reversion.register()
class WlItem(SoftDeletionModel):
    item_data = models.TextField()
    item_rl_data = models.TextField()
    id = models.OneToOneField(HitMaker, models.DO_NOTHING, primary_key=True)
    itm_wl_ref = models.ForeignKey(WatchList, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'wl_item'
