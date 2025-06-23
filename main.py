import random
from StartingVariables import *



#Player hands
axisReserves = []
alliesReserves = []

activePlayer = "Axis"
lastUsedTroop = []
strategems = []

aiPlayer = None
humanPlayer = None

'''
def pop(self):
  if len(self.items) == 0:
    return None
  item = self.items[-1]
  del self.items[-1]
  return item
'''

def startingReserves():
  for x in range(3):
    axisTemp = axisTroops[-1]
    axisReserves.append(axisTemp)
    del axisTroops[-1]
    alliesTemp = alliesTroops[-1]
    alliesReserves.append(alliesTemp)
    del alliesTroops[-1]
  
def research():
  if len(researchTroops) == 0:
    return None
  temp = researchTroops[-1]
  if activePlayer == "Axis":
    axisReserves.append(temp)
  if activePlayer == "Allies":
    alliesReserves.append(temp)
  del researchTroops[-1]
  
def industry():
  if axisTroops == 0:
    return None
  if activePlayer == "Axis":
    axisTemp = axisTroops[-1]
    axisReserves.append(axisTemp)
    del axisTroops[-1]
  if activePlayer == "Allies":
    alliesTemp = alliesTroops[-1]
    alliesReserves.append(alliesTemp)
    del alliesTroops[-1]
    
def bombard():
  if activePlayer == "Axis":
    alliesTemp = alliesReserve[-1]
    alliesTroops.append(alliesTemp)
    del alliesReserves[-1]
  if activePlayer == "Allies":
    axisTemp = axisReserve[-1]
    axisTroops.append(axisReserve)
    del axisReserves[-1]

#def blitz():
  #Deploy another troop

def draw2reserves ():
  if activePlayer == "Axis":
    axisTemp = axisTroops[-1]
    axisReserves.append(axisTemp)
    del axisTroops[-1]
  if activePlayer == "Allies":
    alliesTemp = alliesTroops[-1]
    alliesReserves.append(alliesTemp)
    del alliesTroops[-1]
  
def main():
  #Shuffle the starting troops
  random.shuffle(axisTroops)
  random.shuffle(alliesTroops)
  random.shuffle(researchTroops)

  #player chooses a side

  startingReserves()
  print (axisReserves)
  print (alliesReserves)

  print (alliesReserves[0]["Power"])
main()
