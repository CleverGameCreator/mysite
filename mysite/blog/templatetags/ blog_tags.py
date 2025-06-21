from multiprocessing.resource_tracker import register

from django import template
from django.template.autoreload import template_changed

from ..models import Post

register = template.Library()

@register.simple_tag 
def total_posts():  
    return Post.published.count()