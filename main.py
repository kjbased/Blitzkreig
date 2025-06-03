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

axisTiles = startingTroops
alliesTiles = startingTroops
researchTiles = startingResearch

alliedReserves = []
axisReserves = []

activePlayer = "Axis"
lastUsedTroop = []
strategems = []

random.shuffle(axisTiles)
random.shuffle(alliesTiles)
random.shuffle(researchTiles)

'''
def pop(self):
  if len(self.items) == 0:
    return None
  item = self.items[-1]
  del self.items[-1]
  return item
'''
def research():
  if len(researchTiles) == 0:
    return None
  item = researchTiles[-1]
  if activePlayer == "Axis":
    axisTiles.append(item)
  if activePlayer == "Allies":
    alliesTiles.append(item)
  del researchTiles[-1]
  
def industry():
  if axisTiles == 0:
    return None
  item = 
  if activePlayer == "Axis":
    
def bombard():

def blitz():

def draw2reserves ():
  item
  

def main():

main()
