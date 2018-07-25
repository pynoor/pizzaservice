from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import OrderCreateView, OrderDetailsView, OrderListView

urlpatterns = [
    url(r'^$', OrderCreateView.as_view(), name='create'),

    url(r'^orders/(?P<pk>[0-9]+)/$', OrderDetailsView.as_view(), name="details"),

    url(r'^orders/$', OrderListView.as_view(), name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
