from django.conf.urls import url

from dynamicapp.views import ModuleView

urlpatterns = [
    url(r'^module/$', ModuleView.as_view(), name='dynamicapp_page'),
]
