from controller.domain.gxcode import *
from controller.domain.gcode import *
import re 

""" "G0 X12               ; move to 12mm on the X axis" -> "G0 X12" """
def clear_comments(_string_code:str) -> str:
    string_code:int=_string_code
    if re.split(";",string_code):
        print(re.split(";",string_code)[0])

def transform_string_to_g0_code(string_code:str) -> G0Command:
    pass

def transform_string_to_g1_code(string_code:str) -> G1Command:
    pass

""" "G1 X90.6 Y13.8 E22.4" -> Gcode() """
def transform_string_to_gxcode(string_code:str) -> GCommand:
    pass    

def transform_string_to_mxcode(string_code:str) -> MCommand:
    pass    


def is_gxcode(string_code:str) -> bool:
    pass

def is_mxcode(string_code:str) -> bool:
    pass

def transform_string_to_gcode(string_code:str) -> GCode:
    pass
enviarString:str=clear_comments("G0 X12               ; move to 12mm on the X axis")
