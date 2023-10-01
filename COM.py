"""
Communications System (COM)

Name: COM.py
Description:
  
  
Satellite Function:
  System is Responsible for all
  communications from the satellite. 
"""
class COM:
  def __init__(self):
    self.name = "COM"


#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nCommunications System\n")
  #Insert Test Code Here
  com_mod = COM()
  print(com_mod.name)
  
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()