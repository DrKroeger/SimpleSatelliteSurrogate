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

class int_comms_slv(threading.Thread):
  def __init__(self, name, addr):
    threading.Thread.__init__(self)
    self._running = True
    self.name = name
    self.dev_addr = addr
    self.addr = '0x0'
    self.data = '0x0'
    self.rw = 0
    self.vld = 0
    
  def run(self):
    vld_flag = True
    while(self._running):
      
      if (self.vld == 1) and (vld_flag):
        if self.addr is self.dev_addr:
          print(self.dev_addr)
          if self.rw == 1:
            print('Write Message')
          else:
            print('Read Message')
          vld_flag = False
          
      elif (self.vld == 0):
        vld_flag = True
 
      time.sleep(0.010)
      #print('waiting')
        
  def slv_msg_snd(self, ad, da, rw):
    self.addr = ad
    self.data = da
    self.rw = rw
    self.vld = 1
    print('Msg Send '+str(rw))
    time.sleep(0.010)
    
  def slv_msg_done(self):
    self.vld = 0
    time.sleep(0.010)
    
    
  def shut_down(self):
    self._running = False
      
    
    
#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nInternal Communications Slave Controller\n")

  ics = int_comms_slv(name="slv_comms", addr="0x1")
  print(ics.name)
  
  ics.start()
  
  
  ics.slv_msg_snd('0x1','0x01',1)
  ics.slv_msg_done()
  
  time.sleep(0.5)
  
  ics.slv_msg_snd('0x1','0x01',0)
  ics.slv_msg_done()
  
  # Shut Down Thread
  ics.shut_down()
  
  ics.join()
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()
    