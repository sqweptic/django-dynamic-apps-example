from __future__ import absolute_import
from . import settings
from . import urls

def _combine_specific_var(var_name, var_inst, settings_local_dict):
    settings_local_dict[var_name]['rororo'].extend(var_inst['rororo'])
    
EXCEPTION_VARS = {
    'SPECIFIC_SETTINGS_VAR': _combine_specific_var
}