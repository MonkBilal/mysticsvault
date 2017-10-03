from django import template

register = template.Library()


@register.filter
def astring(s1,s2):
	s2='jpg'
	return (str(s1)+s2)