from django.urls import path

from .views import BlogDetailView,BlogIndexView

urlpatterns = {
  path('', BlogIndexView.as_view()) #Urlbase, lista post
   path('', BlogDetailView.as_view()) #Vista detalle, blog/id:
}