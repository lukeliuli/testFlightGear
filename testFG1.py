'''
flightgear-如何启动
https://www.bilibili.com/read/cv10460305/

flightgear-python入门
https://flightgear-python.readthedocs.io/en/latest/examples.html#simple-fdm-loop

'''

import os 



"""
Simple Flight Dynamics Model (FDM) example that makes the altitude increase and the plane roll in the air.
"""
import time
import os 
from flightgear_python.fg_if import FDMConnection
#define 
def fdm_callback(fdm_data, event_pipe):
    D2R = 3.14159 / 180.0
    if event_pipe.child_poll():
        phi_rad_child, = event_pipe.child_recv()  # unpack tuple
        # set only the data that we need to
        fdm_data['phi_rad'] = phi_rad_child  # we can force our own values
    fdm_data.alt_m = fdm_data.alt_m + 0.5  # or just make a relative change
    return fdm_data  # return the whole structure

"""
Start FlightGear with `--native-fdm=socket,out,30,localhost,5501,udp --native-fdm=socket,in,30,localhost,5502,udp`
(you probably also want `--fdm=null` and `--max-fps=30` to stop the simulation fighting with
these external commands)
"""
if __name__ == '__main__':  # NOTE: This is REQUIRED on Windows!
    #os.system('fgfs --fg-root="D:\Program Files\FlightGear 2020.3\data" --fdm=null --max-fps=30 --native-fdm=socket,out,30,localhost,5501,udp --native-fdm=socket,in,30,localhost,5502,udp ' )
    #time.sleep(1)
    
    fdm_conn = FDMConnection()
    fdm_event_pipe = fdm_conn.connect_rx('localhost', 5501, fdm_callback)
    fdm_conn.connect_tx('localhost', 5502)
    fdm_conn.start()  # Start the FDM RX/TX loop

    phi_rad_parent = 0.0
    while True:
        phi_rad_parent += 0
        # could also do `fdm_conn.event_pipe.parent_send` sF    o you just need to pass around `fdm_conn`
        fdm_event_pipe.parent_send((phi_rad_parent,))  # send tuple #旋转
        time.sleep(1)
