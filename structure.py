"""
Structure

Name: STRUCTURE.py
Description:
  As the structure each of the
  individual components is
  instantiated here, as if they were
  installed on an actual satellite.
  
Satellite Function:
  The stucture of the satellite
  physically holds all of the various
  components together. 
"""
from sat_cfg import *

class STRUCTURE:
  def __init__(self):
    self.name = "STRUCTURE"
    
# Check to see which cards are
# present in the satellite.
# The flags for which cards are
# present are in sat_cfg.py
  # Attitude Determination and Control System (ADCS)
    if adcs_present: 
      from ADCS import ADCS
      self.adcs = ADCS()
      
  # Command and Data Handling System (CDHS)
    if cdhs_present:
      from CDHS import CDHS
      self.cdhs = CDHS()
      
  # Electrical Power System (EPS)
    if eps_present:
      from EPS import EPS
      self.eps = EPS()
      
  # Communications System (COM)
    if com_present:
      from COM import COM
      self.com = COM()
      
  # Thermal Management (TMS)
    if tms_present:
      from TMS import TMS
      self.tms = TMS()
          
  # Payload
    if pld_present:
      from PLD_stub import PLD
      self.pld = PLD()


#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nStructure\n")
  #Insert Test Code Here
  phys_struct = STRUCTURE()
  print(phys_struct.name)
  print(phys_struct.adcs.name)
  print(phys_struct.cdhs.name)
  print(phys_struct.eps.name)
  print(phys_struct.com.name)
  print(phys_struct.tms.name)
  print(phys_struct.pld.name)
  
  #print(globals())
  
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()