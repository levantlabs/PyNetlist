#This is an initial test platform for PyNetlist

import PyNetlist as pn
import numpy as np
import matplotlib.pyplot as plt

import skywater130_pdk_v1 as pdk

#Initialize PDK
pdk130 = pdk.PDK_skywater130('pdkdetails/skywater_130_device_details.xlsx', debug=True)



fname = 'example.cir'


main_netlist = pn.PyNetlist('PDK_skywater130', fname)





