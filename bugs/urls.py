from django.conf.urls import url
from .views import get_bugs


urlpatterns = [
    url(r'^$', get_bugs, name='get_bugs'),
    
    ]