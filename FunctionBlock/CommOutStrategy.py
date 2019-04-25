from FunctionBlock.CommStrategy import *


class CommOutStrategy(CommStrategy):
    def __init__(self, block=None):
        CommStrategy.__init__(self, block)

    def create_command(self, context):
        values = self._input_values(context)
        command = 'write_data:' + str(values)
        return command

    def handle_response(self, context, response):
        value = self._input_values(context)
        box = context.get_box(self.key)
        value_index = 0
        for out in type_filter(Composite.iter(box.block), OutputPort):
            if value_index < len(response):
                context.set_value(out.tag, response[value_index])
                value_index = value_index + 1

