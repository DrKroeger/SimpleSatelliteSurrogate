"""
Command and Data Handling System (CDHS)

Name: CDHS.py
Description:
  
  
Satellite Function:
  This module provides the primary
  computations for the satellite and
  provides the data needed to various
  systems.
"""

class CDHS:
  def __init__(self):
    self.name = "CDHS"


#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nCommand and Data Handling System\n")
  #Insert Test Code Here
  cdhs_mod = CDHS()
  print(cdhs_mod.name)
  
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()