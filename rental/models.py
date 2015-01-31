from django.db import models
#~ from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models import Q
from django.conf import settings


class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL) # 'django.contrib.auth.User'
    what = models.ForeignKey('shelf.BookItem',
        limit_choices_to=(Q(rental__returned__isnull=False)|Q(rental__isnull=True)))
    when = models.DateTimeField(auto_now_add=True)  # domyślnie nie pojawi się w formularzu
    returned = models.DateTimeField(null=True, blank=True)    # pojawi się w formularzu z domyślną wartością

    def __str__(self):
        return '%s - %s' % (self.what, self.who)# zadanie domowe :)

    class Meta:
        permissions = (
            ('can_rent', 'Can rent a book'), # czy użytkownik może dokonać wypożyczenia
        )
