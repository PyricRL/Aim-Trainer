# ----- 3rd Party Libraries -----

# ----- Built-In Libraries ------

# -------- Local Files ----------
from target import *
import utils

def addTargetsToScreen(x, y, parent, window):
    if utils.targetsOnScreen < 20:
        target = Target(x, y, parent=parent, window=window)
    else:
        print("Target limit reached")