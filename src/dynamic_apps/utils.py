import os
import pkgutil
import importlib


MODULES_DIR_NAME = 'modules'

#dynamic module settings and urls
MODULE_SETTINGS_NAME = 'settings'
SETTINGS_EXCEPTION_VARS_NAME = 'EXCEPTION_VARS'
MODULE_URLS_NAME = 'urls'
URLS_VAR = 'urlpatterns'

def find_dynamic_modules(project_settings_path):
    settings_dir_path = os.path.dirname(project_settings_path)
    _, settings_dir_name = os.path.split(settings_dir_path)
    modules_path = os.path.join(settings_dir_path, MODULES_DIR_NAME)
    for _, module_name, is_module in pkgutil.iter_modules((modules_path,)):
        if is_module:
            module_import_name = '.'.join((settings_dir_name, MODULES_DIR_NAME, module_name))
            module = importlib.import_module(module_import_name)
            yield module

def import_module_settings(module, _locals = {}):
    exception_vars = {}
    if hasattr(module, SETTINGS_EXCEPTION_VARS_NAME):
        exception_vars = getattr(module, SETTINGS_EXCEPTION_VARS_NAME)
    if not hasattr(module, MODULE_SETTINGS_NAME):
        return
    settings = getattr(module, MODULE_SETTINGS_NAME)
    for var in dir(settings):
        inst = getattr(settings, var)

        if not var.startswith('_'):
            if var in exception_vars:
                exception_vars[var](var, inst, _locals)
                continue
            if var in _locals:
                if isinstance(inst, list) and isinstance(_locals[var], list):
                    _locals[var].extend(inst)
                if isinstance(inst, dict) and isinstance(_locals[var], dict):
                    locals[var].update(inst)
                if isinstance(inst, tuple) and isinstance(_locals[var], tuple):
                    locals[var] += inst
            else:
                _locals[var] = inst
                
def import_module_urls(module, _locals = {}):
    if not hasattr(module, MODULE_URLS_NAME):
        return
    urls = getattr(module, MODULE_URLS_NAME)
    if hasattr(urls, URLS_VAR) and URLS_VAR in _locals:
        _locals[URLS_VAR] = getattr(urls, URLS_VAR) + _locals[URLS_VAR]