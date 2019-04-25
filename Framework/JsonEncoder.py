import json
from Framework.Component import *

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Component):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)