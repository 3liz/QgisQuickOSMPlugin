"""Modify an json encoder/decoder to accept enum."""

import json

from QuickOSM.definitions.format import Format
from QuickOSM.definitions.osm import LayerType

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'


class EnumEncoder(json.JSONEncoder):
    """Override the json encoder to serialize enum."""
    def default(self, obj):
        """Function of serialization."""
        if type(obj) in [LayerType, Format]:
            return {"__enum__": str(obj)}
        return json.JSONEncoder.default(self, obj)


def as_enum(d):
    """Retrieval of enum from deserialization of a json file."""
    if "__enum__" in d:
        name, member = d["__enum__"].split(".")
        if name == 'LayerType':
            return getattr(LayerType, member)
        if name == 'Format':
            return getattr(Format, member)
    else:
        return d
