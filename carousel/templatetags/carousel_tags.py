from django import template
from django.conf import settings

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

@register.simple_tag
def carousel_media():
    template_content = ''
    static_url = getattr(settings, 'STATIC_URL', None)
    context = {
        'STATIC_URL': static_url
    }

    if static_url:
        t = template.Template(
            '''
            <script src="{{ STATIC_URL }}swipe.min.js"></script>
            <script src="{{ STATIC_URL }}carousel.js"></script>

            <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}swipe.css" />
            <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}carousel.css" />
            '''
        )

        template_content += t.render(template.Context(context))

    return template_content
