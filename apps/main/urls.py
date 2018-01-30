from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^actors/$', views.actor_index),
    url(r'^actors/create$', views.actor_create),
    url(r'^actors/(?P<actor_id>\d+)$', views.actor_show),
    url(r'^actors/add_to_film/(?P<actor_id>\d+)$', views.featured_create),
    url(r'^movies/$', views.movie_index),
    url(r'^movies/create$', views.movie_create),

]
