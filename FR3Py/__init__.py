import os

from FR3Py.lcm_msgs.fr3_commands import fr3_cmd
from FR3Py.lcm_msgs.fr3_states import fr3_state

FR3_USD_PATH = os.path.join(os.path.dirname(__file__), "assets/usd/fr3.usda")

def getDataPath():
    resdir = os.path.join(os.path.dirname(__file__))
    return resdir


