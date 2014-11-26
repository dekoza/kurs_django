from django.db import models
from django.contrib.auth.models import User
from shelf.models import BookItem

from django.utils.timezone import now


class Rental(models.Model):
    who = models.ForeignKey(User)
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return ''  # zadanie domowe :)