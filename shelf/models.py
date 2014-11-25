#coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.utils.encoding import python_2_unicode_compatible

from django.utils.translation import ugettext_lazy as _

from django.db import models

@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=20)
    last_name = models.CharField(_('last name'), max_length=50)

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name,
            last_name=self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = _('Author')  # raczej używać Dopełniacza
        verbose_name_plural = _('Authors')


@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class BookEdition(models.Model):
    book = models.ForeignKey(Book)
    publisher = models.ForeignKey(Publisher)
    isbn = models.CharField(max_length=17)
    issue_date = models.DateField()

    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book,
                                                       publisher=self.publisher)

COVER_TYPES = (
    ('soft', "Soft"),
    ('hard', 'Hard')
    # (wartość_w_bazie, Wyświetlana nazwa)
)

@python_2_unicode_compatible
class BookItem(models.Model):
    edition = models.ForeignKey(BookEdition)
    cover = models.CharField(max_length=4, choices=COVER_TYPES)  # rodzaj okładki

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition,
                                           cover=self.get_cover_display())
