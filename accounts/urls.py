from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from accounts.views import CreateView, DetailsView

# router = DefaultRouter()
# router.register(r'users', CreateView)

urlpatterns = [
    url(r'^users/$', CreateView.as_view(), name='create'),
    url(r'^users/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
