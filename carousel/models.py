from django.db import models


class Carousel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('name',)


class Slide(models.Model):
    carousel = models.ForeignKey(Carousel, related_name='slides')
    title = models.CharField(max_length=100)
    blurb = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel')
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.title,)

    class Meta:
        verbose_name = u'Carousel Slide'
        verbose_name_plural = u'Carousel Slides'
        ordering = ('weight', 'title')
