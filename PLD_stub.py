"""
Payload Subsystem Stub

Name: PLD_stub.py
Description:
  User should modify for their payload
  needs.
  
Satellite Function:
  This is an example payload for the
  satellite. It can be updated, changed,
  and multiplied for various satellite
  payloads.
"""
class PLD:
  def __init__(self):
    self.name = "Payload"


#####################################
# main function used for testing
#####################################
def main():
  print("\nTESTING\nPayload Subsystem\n")
  #Insert Test Code Here
  pld_mod = PLD()
  print(pld_mod.name)
  
  # End of Testing
  print("\nTesting Complete")


if __name__ == "__main__":
    main()