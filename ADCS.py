"""
Attitude Determination and Control System (ADCS)

Name: ADCS.py
Description:
  
  
Satellite Function:
  This system is responsible for the
  overall orientation of the satellite.
"""
class ADCS:
  def __init__(self):
    self.name = "ADCS"


#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nAttitude Determination and Control\n")
  #Insert Test Code Here
  adcs_mod = ADCS()
  print(adcs_mod.name)
  
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()