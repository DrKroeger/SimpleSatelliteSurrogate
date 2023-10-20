"""
Internal Communications Slave

Name: int_comms_slv.py
Description:
  This script serves as the internal
  communications of the satellite. It
  allows the internal components to talk
  to the command and data handler. This
  particular script is the slave
  interface.
  
Satellite Function:
  The allows internal compoent
  configuration and status reporting. 
"""
import time
import threading

class int_comms_slv:
  def __init__(self, name, addr):
    self.name = name
    self.dev_addr = addr
    self.addr = '0x0'
    self.data = '0x0'
    self.rw = 0
    self.vld = '0'
    
  def slv_monitor(self):
    vld_flag = True
    while(True):
      if (self.vld == '1') and (vld_flag):
        if self.addr == self.dev_addr:
          print(self.dev_addr)
          vld_flag = False
      elif (self.vld == '0'):
        vld_flag = True
      time.sleep(0.10)
        
  def slv_msg_snd(self, ad, da, rw):
    self.addr = ad
    self.data = da
    self.rw = rw
    self.vld = '1'
    
  def slv_msg_done(self):
    self.vld = '0'
      
    
    
#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nInternal Communications Slave Controller\n")

  ics = int_comms_slv(name="slv_comms", addr="0x1")
  print(ics.name)
  
  # End of Testing
  print("\nTesting Complete")
  


if __name__ == "__main__":
    main()
    