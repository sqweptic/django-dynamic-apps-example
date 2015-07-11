from django.conf.urls import url

from someapp.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_page'),
]
