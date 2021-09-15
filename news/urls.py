from django.urls import path
from . import views
urlpatterns = [
    path('<slug:c_slug>/<slug:news_slug>', views.latest_news, name='latest_news'),
]
