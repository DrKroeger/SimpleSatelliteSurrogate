"""
Internal Communications Master

Name: int_comms_mstr.py
Description:
  This script serves as the internal
  communications of the satellite. It
  allows the internal components to talk
  to the command and data handler. This
  particular script is the master
  interface.
  
Satellite Function:
  The allows internal compoent
  configuration and status reporting. 
"""
class int_comms_mstr:
  def __init__(self):
    self.name = "mstr_comms"
    self.addr = "0x0"
    self.data = "0x0"
    self.rw   = "0"
    self.vld  = "0"
    
    
#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nInternal Communications Master Controller\n")

  
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()
    