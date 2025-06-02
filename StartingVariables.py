def create_troop (name, power, type, special):
        return {"Name": name, "Power": power, "Type": type, "Special": special}

def create_space (name, row, type, special):
        return {"Space": name, "Row": row, "Type": type, "Special": special, "Occupied": 0}
        
startingTroops = [
        create_troop ("Plane(Blitz)", 0, "Both", "blitz"},
        create_troop ("Plane", 1, "Both", None), 
        create_troop ("Plane", 1, "Both", None), 
        create_troop ("Plane", 1, "Both", None), 
        create_troop ("Plane", 2, "Both", None), 
        create_troop ("Plane", 2, "Both", None), 
        create_troop ("Tank", 1, "Army", None), 
        create_troop ("Tank", 1, "Army", None),
        create_troop ("Tank", 1, "Army", None),
        create_troop ("Tank", 2, "Army", None),
        create_troop ("Tank", 2, "Army", None),
        create_troop ("Tank", 3, "Army", None),
        create_troop ("Tank", 3, "Army", None),
        create_troop ("Ship", 1, "Navy", None), 
        create_troop ("Ship", 1, "Navy", None),  
        create_troop ("Ship", 1, "Navy", None), 
        create_troop ("Ship", 2, "Navy", None),  
        create_troop ("Ship", 2, "Navy", None),  
        create_troop ("Ship", 3, "Navy", None),  
        create_troop ("Ship", 3, "Navy", None),  
        create_troop ("General", 1, "Army", "general"),  
        create_troop ("Admiral", 1, "Navy", "admiral"),  
        ]

startingResearch = [
        create_troop ("Nuke", 7, "Army", "nuke"), 
        {"Spy": 0, "Type": "Any", "Special": spy}, 
        {"Scientist": 0, "Type": "Both", "Special": "Can be placed anywhere"},
        {"Carrier(Bombard)": 2, "Type": "Navy", "Special": Bombard}, 
        {"Carrier(Blitz)": 1, "Type": "Navy", "Special": Blitz}, 
        {"Carrier": 4, "Type": "Navy", "Special": None}, 
        {"Carrier": 4, "Type": "Navy", "Special": None}, 
        {"Carrier(Elite)": 5, "Type": "Navy", "Special": "Ignore space effects"},
        {"Tank_Charge": 1, "Type": "Army", "Special": "Blitz"}, 
        {"Tank": 4, "Type": "Army", "Special": None}, 
        {"Tank": 4, "Type": "Army", "Special": None}, 
        {"Tank(Elite)": 5, "Type": "Army", "Special": "Ignore space effects"},
        {"Bomber(Bombard)": 1, "Type": "Both", "Special": "Bombard"}, 
        {"Bomber": 3, "Type": "Both", "Special": None}, 
        {"Bomber": 3, "Type": "Both", "Special": None}, 
        {"Bomber(Elite)": 4, "Type": "Both", "Special": "Ignore space effects"}
        ]

'''
startingResearchJP = [
        {"Partisans": X, "Type": "Army", "Special": "3 if behind 1 if ahead"},
        {"Improved research" : X, "Type": "Both", "Special": "Triggers board space twice"}
        ]
'''

startingJapan = [
        {"Plane(Bombard)": 0, "Type": "Both", "Special": bombard},
        {"Plane": 1, "Type": "Both", "Special": None}, 
        {"Plane": 1, "Type": "Both", "Special": None}, 
        {"Plane": 1, "Type": "Both", "Special": None}, 
        {"Plane": 2, "Type": "Both", "Special": None}, 
        {"Plane": 2, "Type": "Both", "Special": None},
        {"Tank": 1, "Type": "Army", "Special": None}, 
        {"Tank": 1, "Type": "Army", "Special": None}, 
        {"Tank": 1, "Type": "Army", "Special": None},
        {"Tank": 2, "Type": "Army", "Special": None}, 
        {"Tank": 2, "Type": "Army", "Special": None},
        {"Tank": 3, "Type": "Army", "Special": None}, 
        {"Godzilla": 4, "Type": "Any", "Special": None},
        {"Ship": 1, "Type": "Navy", "Special": None}, 
        {"Ship": 1, "Type": "Navy", "Special": None}, 
        {"Ship": 1, "Type": "Navy", "Special": None}, 
        {"Ship": 1, "Type": "Navy", "Special": None},
        {"Ship": 2, "Type": "Navy", "Special": None}, 
        {"Ship": 2, "Type": "Navy", "Special": None},
        {"Ship": 3, "Type": "Navy", "Special": None},
        {"General": 1, "Type": "Army", "Special": general},
        {"Admiral": 1, "Type": "Navy", "Special": admiral}
        ]

westernEurope = [
        {"Space": "Industry", "Row": 1, "Type": "Navy", "Special": drawReserves, "Occupied": 0},
        {"Space": "Research", "Row": 1, "Type": "Army", "Special": addResearch, "Occupied": 0},
        {"Space": "Victory Point (1)", "Row": 1, "Type": "Both", "Special": "Add 1 VP", "Occupied": 0},
        {"Space": "Bombard", "Row": 2, "Type": "Army", "Special": bombard, "Occupied": 0},
        {"Space": "Industry", "Row": 2, "Type": "Army", "Special": drawReserves, "Occupied": 0},
        {"Space": "Blank", "Row": 2, "Type": "Both", "Special": None, "Occupied": 0},
        {"Space": "Research Industy", "Row": 3, "Type": "Both", "Special": drawResearch, "Occupied": 0},
        {"Space": "Strategic Advantage < +3 >", "Row": 3, "Type": "Army", "Special": tactAdvantage, "Occupied": 0},
        {"Space": "Blank", "Row": 3, "Type": "Both", "Special": None, "Occupied": 0}
        ]

easternEurope = [
        {"Space": "Tactical Advnatage (+1)", "Row": 1, "Type": "Army", "Special": "+1 to current theatre", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 2, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 2, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 2, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 3, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 3, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 3, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 3, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 3, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        ]

africa = [
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        ]

pacific = [
        {"Space": "Bombard", "Row": 1, "Type": "Navy", "Special": "Bombard", "Occupied": 0}, 
        {"Space": "Research", "Row": 1, "Type": "Navy", "Special": "draw from research", "Occupied": 0},
        {"Space": "Research (2x)", "Row": 2, "Type": "Navy", "Special": "Draw twice from research", "Occupied": 0}, 
        {"Space": "Industry", "Row": 2, "Type": "Navy", "Special": "Draw from reserves", "Occupied": 0}, 
        {"Space": "Strategic Advantage < +2 >", "Row": 2, "Type": "Navy", "Special": "Advance track of one other theatre", "Occupied": 0},
        {"Space": "Blank", "Row": 2, "Type": "Both", "Special": None, "Occupied": 0},
        {"Space": "Bombard", "Row": 3, "Type": "Navy", "Special": "Bombard", "Occupied": 0},
        {"Space": "Victory Point (2)", "Row": 3, "Type": "Both", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Blank", "Row": 3, "Type": "Both", "Special": None, "Occupied": 0}
        ]

southEastAsia = [
        {"Space": "Victory Point (2)", "Row": 1, "Type": "Navy", "Special": "Add 2 VP", "Occupied": 0},
        {"Space": "Victory Point (1)", "Row": 1, "Type": "Both", "Special": "Add 1 VP", "Occupied": 0}, 
        {"Space": "Strategic Advantage < +1 >", "Row": 1, "Type": "Both", "Special": "Advance track of one other theatre", "Occupied": 0}, 
        {"Space": "Bombard", "Row": 2, "Type": "Navy", "Special": "Bombard", "Occupied": 0}, 
        {"Space": "Victory Point (2)", "Row": 2, "Type": "Army", "Special": "Add 2 VP", "Occupied": 0}, 
        {"Space": "Blank", "Row": 2, "Type": "Both", "Special": None, "Occupied": 0}, 
        ]
