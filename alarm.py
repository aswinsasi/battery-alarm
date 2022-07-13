# Get power status of the system using ctypes to call GetSystemPowerStatus

import ctypes
from ctypes import wintypes;
import psutil
from playsound import playsound;

class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]

SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
GetSystemPowerStatus.restype = wintypes.BOOL

status = SYSTEM_POWER_STATUS()

if not GetSystemPowerStatus(ctypes.pointer(status)):
    raise ctypes.WinError()

while(psutil.sensors_battery().power_plugged):
    if( status.ACLineStatus and status.BatteryLifePercent>=85):
        playsound('a.mp3');
    if( not status.ACLineStatus and status.BatteryLifePercent<=50):
        playsound('a.mp3');

# print('ACLineStatus', status.ACLineStatus)
# print('BatteryFlag', status.BatteryFlag)
# print('BatteryLifePercent', status.BatteryLifePercent)
# print('BatteryLifeTime', status.BatteryLifeTime)
# print('BatteryFullLifeTime', status.BatteryFullLifeTime)