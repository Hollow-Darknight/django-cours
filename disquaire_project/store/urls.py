from django.urls import path, re_path

from . import views # Import views pour l'utiliser in urls

app_name = 'store'
urlpatterns = [
    path('', views.listing, name="listing"), # "/store" va appeler la méthode "index" dans "views.py"
    re_path('^(?P<albumID>[0-9]+)/$', views.detail, name="detail"),
    re_path('^search/$', views.search, name="search"),
]