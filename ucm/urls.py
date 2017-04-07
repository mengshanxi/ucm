from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns(
#    '',
#    (r'^login/$', 'ucmapp.views.login'),
#    (r'^welcome/$', 'ucmapp.views.welcome'),
#    (r'^users/$', 'ucmapp.views.users'),
#    (r'^add/$', 'ucmapp.views.addUser'),
#    (r'^admin/$', 'admin.site.urls'),
#)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]
