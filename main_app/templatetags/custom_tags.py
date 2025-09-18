from django import template

register = template.Library()

@register.filter
def join_names(queryset, delimiter=", "):
  return delimiter.join([obj.name for obj in queryset])