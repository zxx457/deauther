import sys
from enum import Enum 
import shutil

def is_program_installed(program_name):
    return shutil.which(program_name) is not None

class PLATFORM(Enum):
    MAC = 0
    LINUX = 1
    WINDOWS = 2

def detect_platform() -> PLATFORM:
    
    if sys.platform.startswith('win'):
        return PLATFORM.WINDOWS
    elif sys.platform.startswith('linux'):
        return PLATFORM.LINUX
    elif sys.platform.startswith('darwin'):
        return PLATFORM.MAC
    

