"""
Electrical Power System (EPS)

Name: EPS.py
Description:
  
  
Satellite Function:
  This module provides the electrical
  power system for the satellite. It
  distributes the power to various
  modules.
"""
class EPS:
  def __init__(self):
    self.name = "EPS"
    self.pow_in = False
    self.pow_out = 0.0
    
  # Initialize Power Input  
  def pow_input(self):
    self.pow_in = True
    print("Power Input Stable")
    return 0
    
  # Inititalize Power Output
  # Note that power ibput must be stable
  # before EPS can output power
  def pow_output(self):
    ret_val = 1
    if self.pow_in:
      self.pow_out = 24.0
      print("EPS Power Ready")
      ret_val = 0
    else:
      print("ERROR: Power Input")
      
    return ret_val
    
  # Get the output power for 
  # distribution to other modules
  def get_pow_val(self):
    return self.pow_out


#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nElectrical Power System\n")
  #Insert Test Code Here
  eps_mod = EPS()
  print(eps_mod.name)
  
  tmp = eps_mod.pow_output()
  if tmp:
    print("Error - A - Expected")
  print("Output Power: " + str(eps_mod.get_pow_val())+"v")
  
  tmp = eps_mod.pow_input()
  if tmp:
    print("Error - B")
  
  tmp = eps_mod.pow_output()
  if tmp:
    print("Error - C")
    
  print("Output Power: " + str(eps_mod.get_pow_val())+"v")
  
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()