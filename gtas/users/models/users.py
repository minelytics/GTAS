from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from gtas.users.models.delete import SoftDeletionModel
import reversion


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    high_priority_hits_email = models.CharField(max_length=1, blank=True, null=True)
    email_enabled = models.CharField(max_length=1, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


@reversion.register()
class UgUserJoin(SoftDeletionModel):
    ug = models.OneToOneField('UserGroup', models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'ug_user_join'
        constraints = [models.UniqueConstraint(fields=['ug', 'user'], name='unique_ug_user')]


@reversion.register()
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = False
        db_table = 'role'


@reversion.register()
class UserGroup(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    ug_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_group'
        constraints = [models.UniqueConstraint(fields=['ug_name'], name='unique_ug_name')]


@reversion.register()
class UserLocation(SoftDeletionModel):
    airport = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)
    primary_location = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_location'
        constraints = [models.UniqueConstraint(fields=['airport', 'user_id'], name='unique_airport_user_id')]



@reversion.register()
class UserQuery(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    query_description = models.CharField(max_length=100, blank=True, null=True)
    query_text = models.CharField(max_length=10485760)
    query_title = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_query'


@reversion.register()
class UserRole(SoftDeletionModel):
    user = models.OneToOneField(User, models.DO_NOTHING)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False,
                                                           related_name='%(class)s_updatedby')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_role'
        constraints = [models.UniqueConstraint(fields=['user', 'role'], name='unique_user_role')]
