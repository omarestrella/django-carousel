from django import template

from carousel.models import Carousel

register = template.Library()


@register.inclusion_tag('carousel/carousel.html', takes_context=True)
def show_carousel(context, slug, *args, **kwargs):
    try:
        carousel = Carousel.objects.get(slug=slug)
        context['carousel'] = carousel
    except Carousel.DoesNotExist:
        return ''
    else:
        pass
    return context
