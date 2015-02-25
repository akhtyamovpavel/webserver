from django.conf.urls import patterns, url
from shop import views

__author__ = 'akhtyamovpavel'

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),
    url(r'^products/(?P<product_id>\d+)$', views.show_product),
)