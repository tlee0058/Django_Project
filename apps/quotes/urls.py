from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^quotes$', views.quotes),
    url(r'^post_quote$', views.post_quote),
    url(r'^add_list/(?P<quote_id>\d+)$', views.add_list),
    url(r'^remove_list/(?P<fav_id>\d+)$', views.remove_list),
    url(r'^users/(?P<poster_id>\d+)', views.show),
]