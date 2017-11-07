from django.conf.urls import url
from atcar.views1 import atcar_list_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listall$', atcar_list_views.list_all, name='listcars'),
    url(r'^listall1$', atcar_list_views.list_all1, name='listcars1'),
    url(r'^listall2$', atcar_list_views.list_all2, name='listcars2'),
    url(r'^listall3$', atcar_list_views.list_all3, name='listcars3'),
    url(r'^listall4$', atcar_list_views.list_all4, name='listcars4'),
    url(r'^add$', views.addvehicle, name="addcar"),
    url(r'^listmake/(?P<make>\w+)$', atcar_list_views.list_make, name='listmake'),
    url(r'^detail/(?P<id>[0-9]+)', atcar_list_views.detail_list, name='detail')
] 