from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django.db import models

from gtas.apis.models import Notification
from gtas.users.delete.delete import SoftDeletionModel
import reversion


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


@reversion.register()
class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = False
        db_table = '`role`'


@reversion.register()
class User(SoftDeletionModel):
    user_id = models.CharField(primary_key=True, max_length=255)
    active = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    high_priority_hits_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    email_enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = '`user`'


@reversion.register()
class UserGroup(SoftDeletionModel):
    id = models.BigIntegerField(primary_key=True)
    ug_name = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_group'


@reversion.register()
class UserGroupNotifications(SoftDeletionModel):
    id = models.OneToOneField(Notification, models.DO_NOTHING, db_column='id', primary_key=True)
    hm = models.ForeignKey(UserGroup, models.DO_NOTHING, blank=True, null=True)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_group_notifications'


@reversion.register()
class UserLocation(SoftDeletionModel):
    airport = models.CharField(primary_key=True, max_length=255)
    user_id = models.CharField(max_length=255)
    primary_location = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_location'
        unique_together = (('airport', 'user_id'),)


@reversion.register()
class UserNotification(SoftDeletionModel):
    id = models.OneToOneField(Notification, models.DO_NOTHING, db_column='id', primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_notification'


@reversion.register()
class UserQuery(SoftDeletionModel):
    id = models.IntegerField(primary_key=True)
    created_dt = models.DateTimeField()
    deleted_dt = models.DateTimeField(blank=True, null=True)
    query_description = models.CharField(max_length=100, blank=True, null=True)
    query_text = models.CharField(max_length=10485760)
    query_title = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, db_column='deleted_by', blank=True, null=True)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_query'


@reversion.register()
class UserRole(SoftDeletionModel):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    created_by = models.IntegerField(blank=False, null=False)
    updated_by = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=False, null=True)

    class Meta:
        managed = True
        db_table = 'user_role'
        unique_together = (('user', 'role'),)
