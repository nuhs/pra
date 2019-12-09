#!/usr/bin/env python

'''MyFarmware'''

from time import time, sleep
from farmware_tools import device
import cv2

device.log(message='Now OK!', message_type='success')

cap = cv2.VideoCapture(0)
sleep(0.1)
device.log('{}'.format(cap))
