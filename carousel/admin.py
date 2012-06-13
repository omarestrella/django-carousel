from django.contrib import admin

from carousel.models import Carousel, Slide


class SlideInline(admin.TabularInline):
    model = Slide


class CarouselAdmin(admin.ModelAdmin):
    inlines = [
        SlideInline
    ]


admin.site.register(Carousel, CarouselAdmin)
