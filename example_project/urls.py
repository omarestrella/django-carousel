from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example_project.views.home', name='home'),
    # url(r'^example_project/', include('example_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='base.html'))
)

urlpatterns += patterns('',
    (r'^%s(?P<path>.*)' % settings.MEDIA_URL.lstrip('/'),
      'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))
