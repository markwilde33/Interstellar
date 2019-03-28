from django.conf.urls import url
from .views import get_bugs, bug_view, create_or_edit_bug, delete_bug, upvote_bug


urlpatterns = [
    url(r'^$', get_bugs, name='get_bugs'),
    url(r'^(?P<pk>\d+)/$', bug_view, name='bug_view'),
    url(r'^new/$', create_or_edit_bug, name='create_bug'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name="edit_bug"),
    url(r'^(?P<pk>\d+)/delete/$', delete_bug, name="delete_bug"),
    url(r'^upvote(?P<pk>\d+)/$', upvote_bug, name='upvote_bug'),
    ]