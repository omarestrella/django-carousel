from django import template

from carousel.models import Carousel

register = template.Library()


@register.tag('carousel')
def show_carousel(parser, token):
    try:
        tag_name, function, carousel_slug = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('%r tag requires the carousel slug as an argument'
            % token.contents.split()[0])
    else:
        if not (carousel_slug[0] == carousel_slug[-1] and carousel_slug[0] in ('"', "'")):
            raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
        return CarouselNode(carousel_slug)


class CarouselNode(template.Node):
    def __init__(self, carousel_slug):
        self.carousel_slug = carousel_slug.strip('"')

    def render(self, context):
        if self.carousel_slug is not None:
            try:
                carousel = Carousel.objects.get(slug=self.carousel_slug)
                context['carousel'] = carousel
                return template.loader.render_to_string('carousel/carousel.html', context)
            except Carousel.DoesNotExist:
                return ''

        return ''
