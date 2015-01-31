from django.template import Library
from shelf.models import BookItem

register = Library()

@register.filter
def pub_date(date):
    return date.year
    
@register.inclusion_tag('tags/show_editions.html')
def show_editions(obj):
    return {'editions': obj.editions.all()}

@register.inclusion_tag('tags/show_items.html')
def show_items(obj):
    editions = obj.editions.all()
    return {'items': BookItem.objects.filter(edition__in=editions)}
