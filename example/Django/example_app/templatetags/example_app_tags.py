
from django import template

from example_app.models import Video


register = template.Library()

@register.simple_tag
def get_related_videos(from_video):
    return Video.objects.exclude(pk=from_video.pk).filter(category=from_video.category)[:3]


