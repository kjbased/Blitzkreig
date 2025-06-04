import random
from StartingVariables import *

axisVP = 0
alliedVP = 0
japanVP = 0
westernEuropeTrack = 0
easternEuropeTrack = 0
africaTrack = 0
pacificTrack = 0
southEastAsiaTrack = 0

axisTroops = startingTroops
alliesTroops = startingTroops
researchTroops = startingResearch
axisReserves = []
alliesReserves = []

alliedReserves = []
axisReserves = []

activePlayer = "Axis"
lastUsedTroop = []
strategems = []

random.shuffle(axisTroops)
random.shuffle(alliesTroops)
random.shuffle(researchTroops)

'''
def pop(self):
  if len(self.items) == 0:
    return None
  item = self.items[-1]
  del self.items[-1]
  return item
'''

def startingReserves:
  for x in range(2):
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
    
    del alliesReserves[-1]
  if activePlayer == "Allies":

def blitz():
  test

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

main()
