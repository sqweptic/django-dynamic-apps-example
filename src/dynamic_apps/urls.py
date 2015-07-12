import os

from django.conf.urls import include, url

from dynamic_apps.utils import find_dynamic_modules, import_module_urls

urlpatterns = [
    url(r'^', include('someapp.urls')),
]

for module in find_dynamic_modules(os.path.abspath(__file__)):
    import_module_urls(module, locals())