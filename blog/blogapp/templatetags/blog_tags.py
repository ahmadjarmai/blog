from django import template
from ..models import Post 

register =template.Library()

@register.simple_tag
def total_post() :
    return Post.published.count()

@register.inclusion_tag('blog/latest_post.html')
def show_latest_posts(count=3) :
    latest_posts=Post.published.order_by('-publish')[:count] 
    return {'latest_posts':latest_posts}
