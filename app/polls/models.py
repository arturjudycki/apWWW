from django.db import models
from datetime import datetime

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True,
 null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Druzyna(models.Model):
    nazwa = models.CharField(max_length=255)
    kraj = models.CharField(max_length=2)

    def __str__(self):
        return self.nazwa + ' (' + self.kraj + ')'

class Osoba(models.Model):
    class Miesiace_urodzenia(models.IntegerChoices):
        Styczeń = 1
        Luty = 2
        Marzec = 3
        Kwiecień = 4
        Maj = 5
        Czerwiec = 6
        Lipiec = 7
        Sierpień = 8
        Wrzesień = 9
        Październik = 10
        Listopad = 11
        Grudzień = 12

    # MIESIACE_URODZENIA = (
    #     ('1', 'Styczeń'),
    #     ('2', 'Luty'),
    #     ('3', 'Marzec'),
    #     ('4', 'Kwiecień'),
    #     ('5', 'Maj'),
    #     ('6', 'Czerwiec'),
    #     ('7', 'Lipiec'),
    #     ('8', 'Sierpień'),
    #     ('9', 'Wrzesień'),
    #     ('10', 'Październik'),
    #     ('11', 'Listopad'),
    #     ('12', 'Grudzień'),
    # )

    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    # miesiac_urodzenia = models.CharField(max_length=2, choices=MIESIACE_URODZENIA, default='1')
    miesiac_urodzenia = models.IntegerField(choices=Miesiace_urodzenia.choices, default=datetime.now().month)
    data_dodania = models.DateField(auto_now_add=True)
    druzyna = models.ForeignKey(
        Druzyna,
        on_delete = models.SET_NULL,
        blank=True,
        null=True,
    )
    wlasciciel = models.ForeignKey('auth.User', related_name='osoby', on_delete=models.CASCADE, blank=True,
        null=True,)
    def __str__(self):
        return self.imie + " " + self.nazwisko

    @property
    def get_team(self):
        return self.druzyna


    class Meta:
        ordering = ["nazwisko"]
        permissions = [
            ("can_view_other_persons", "Pozwala przeglądać obiekty modelu Osoba, zalogowanym użytkownikom, którzy nie są własicielami danego obiektu modelu Osoba")
        ]

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)