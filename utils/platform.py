import sys
from enum import Enum 

class Platform(Enum):
    MAC = 0
    LINUX = 1
    WINDOWS = 2

def detect_platform() -> Platform:
    
    if sys.platform.startswith('win'):
        return Platform.WINDOWS
    elif sys.platform.startswith('linux'):
        return Platform.LINUX
    elif sys.platform.startswith('darwin'):
        return Platform.MAC
    
