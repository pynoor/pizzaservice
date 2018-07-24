from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import OrderCreateView

urlpatterns = [
    url(r'^$', OrderCreateView.as_view(), name='create')

]

urlpatterns = format_suffix_patterns(urlpatterns)