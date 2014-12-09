from django.conf.urls import patterns, include, url
from django.contrib import admin
from userprofiles.views import List, Create
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'examen2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'django.contrib.auth.views.login',{'template_name':'index.html'}, name='login'),
	url(r'^cerrar/$', 'userprofiles.views.cerrar'),




	url(r'^update/$', 'userprofiles.views.update', name='update'),
	url(r'^delete/$', 'userprofiles.views.borrar', name='delete'),
	url(r'^nuevo_usuario/$', 'userprofiles.views.nuevo'),
	url(r'^listar/$', 'userprofiles.views.listar'),
    url(r'^new/', Create.as_view(), name='new'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail/(?P<id_user>\d+)$','userprofiles.views.detail',name='detail'),
    url(r'^list/$',List.as_view(),name='list'),
)
