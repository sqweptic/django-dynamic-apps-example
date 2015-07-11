from django.views.generic.base import TemplateView
from django.conf import settings

class BaseTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseTemplateView, self).get_context_data(**kwargs)
        if hasattr(settings, 'ENABLED_MODULES'):
            context['modules'] = settings.ENABLED_MODULES
        return context