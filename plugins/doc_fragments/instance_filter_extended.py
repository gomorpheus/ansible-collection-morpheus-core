from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r'''
options:
    environment:
        description:
            - Filter instances by environment.
        type: str
    labels:
        description:
            - Filter instances by matching labels.
        type: list
        elements: str
    match_all_labels:
        description:
            - If labels have been specified, filter instances by those that match all specified labels.
        default: false
        type: bool
    tags:
        description:
            - Filter instances by matching tags.
        type: list
        elements: str
'''
