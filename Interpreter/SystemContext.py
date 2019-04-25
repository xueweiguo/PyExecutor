from enum import *

class R_string(Enum):
    error_invalid_input = 'error_invalid_input'
    error_mathmatic_error = 'error_mathmatic_error'
    error_invalid_parameter_count = 'error_invalid_parameter_count'
    error_invalid_date_type = 'error_invalid_date_type'
    character_pi = 'Π'
    character_angle = '∠'
    character_degree = '°'
    error_self_call = 'error_self_call'

class SystemContext:
    def __init__(self):
        pass

    def getText(self, str):
        if str == R_string.character_angle:
            return character_angle