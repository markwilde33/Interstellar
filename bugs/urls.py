from django.conf.urls import url
from .views import get_bugs, bug_view


urlpatterns = [
    url(r'^$', get_bugs, name='get_bugs'),
    url(r'^(?P<pk>\d+)/$', bug_view, name='bug_view'),
    ]