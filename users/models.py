from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import logging

logger = logging.getLogger('moje')

class BiblioUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, default='')

    #~ def save(self, *args, **kwargs):
        #~ # sposób 1
        #~ super(BiblioUser, self).save(*args, **kwargs)
        #~ try:
            #~ p = Permission.objects.get(codename='can_rent')
            #~ self.user_permissions.add(p)
        #~ except Exception as e:   # Permission.DoesNotExist
            #~ # logowanie błędu
            #~ logger.log(logging.ERROR, "%s" % e)
            #~ 
        


# sposób 2 - sygnały
@receiver(post_save, sender=BiblioUser)
def add_rent_permission(sender, *args, **kwargs):
    user = kwargs.get('instance')
    try:
        p = Permission.objects.get(codename='can_rent')
        user.user_permissions.add(p)
        logger.info("Pomyślnie dodano uprawnienie.")
    except Exception as e:   # Permission.DoesNotExist
        logger.error("Wystąpił błąd w nadawaniu uprawnienia: %s" % e)
