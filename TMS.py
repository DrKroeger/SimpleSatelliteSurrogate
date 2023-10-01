"""
Thermal Management (TMS)

Name: TMS.py
Description:
  
  
Satellite Function:
  This system provides thermal
  management for the satellite.
  It monitors and may even control
  the overall temperature.
"""
class TMS:
  def __init__(self):
    self.name = "TMS"


#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nThermal Management System\n")
  #Insert Test Code Here
  tms_mod = TMS()
  print(tms_mod.name)
  
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()