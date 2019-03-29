from django.conf.urls import url
from .views import get_features, feature_view, create_or_edit_feature, delete_feature


urlpatterns = [
    url(r'^$', get_features, name='get_features'),
    url(r'^(?P<pk>\d+)/$', feature_view, name='feature_view'),
    url(r'^new/$', create_or_edit_feature, name='create_feature'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_feature, name="edit_feature"),
    url(r'^(?P<pk>\d+)/delete/$', delete_feature, name="delete_feature"),
    ]