from django.template import Library

register = Library()

@register.filter
def pub_date(date):
    return date.year
    
@register.inclusion_tag('tags/show_editions.html')
def show_editions(obj):
    return {'editions': obj.editions.all()}
