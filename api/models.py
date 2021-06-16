from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('users must have an email addr')
        if not username:
            raise ValueError('users must have an username')

        user = self.model(
                    email = self.normalize_email(email),
                    username = username,
               )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
               email=self.normalize_email(email),
               password=password,
               username=username,
               )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length = 60, unique = True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name = 'last login' , auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email 

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

#creates tokens for when i create a user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#tuition models
class Ben_Tuition(models.Model):
    customer_resource_name = models.CharField(max_length=60)
    
    class Meta:
        abstract=True
    
class BenCampaign(Ben_Tuition):
    campaign_name = models.CharField(max_length=60)
    campaign_id = models.CharField(max_length=60)

    #class Meta(Ben_Tuition.Meta):
        #ordering=['campaign_name']
    
class BenAdGroup(BenCampaign):
    ad_group_name = models.CharField(max_length=60)

    #class Meta(BenCampaign.Meta):
        #ordering=['ad_group_name']
    
class BenMetrics(BenAdGroup):
    metrics_clicks = models.CharField(max_length=60)
    metrics_impressions = models.CharField(max_length=60)
    metrics_ctr = models.CharField(max_length=60)
    metrics_cpc = models.CharField(max_length=60)
    datepulled = models.CharField(max_length=20)

