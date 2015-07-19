import importlib

from django.test import TestCase
from django.conf import settings

class PagesTest(TestCase):
    def setUp(self):
        self.available_modules = ['dynamicapp',]
    
    def test_modules_existing(self):
        enabled_modules = []
        if hasattr(settings, 'ENABLED_MODULES'):
            enabled_modules = settings.ENABLED_MODULES
        
        for module_name in self.available_modules:
            try:
                module = importlib.import_module(module_name)
            except ImportError:
                module = None
            
            self.assertIn(module_name, enabled_modules)
            self.assertIsNotNone(module)
            
            