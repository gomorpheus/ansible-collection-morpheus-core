from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r'''
options:
    id:
        description:
            - Specify the id of an instance.
        type: int
    name:
        description:
            - Filter instances by name.
        type: str
    regex_name:
        description:
            - Treat the name parameter as a regular expression.
        default: false
        type: bool
'''
