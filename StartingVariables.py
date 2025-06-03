def create_troop (name, power, type, special):
        return {"Name": name, "Power": power, "Type": type, "Special": special}

def create_space (name, row, type, special):
        return {"Space": name, "Row": row, "Type": type, "Special": special, "Occupied": 0}

theatre = [westernEurope, easternEurope, paciifc, africa, oceania]

startingTroops = [
        create_troop ("Plane(Blitz)", 0, "Both", "blitz"),
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
        create_troop ("Spy", 0, "Both", "spy"), 
        create_troop ("Scientist", 0, "Both", "scientist"),
        create_troop ("Carrier(Bombard)", 2, "Navy", "bombard"), 
        create_troop ("Carrier(Blitz)", 1, "Navy", "blitz"), 
        create_troop ("Carrier", 4, "Navy", None), 
        create_troop ("Carrier", 4, "Navy", None), 
        create_troop ("Carrier(Elite)", 5, "Navy", "elite"),
        create_troop ("Tank (Blitz)", 1, "Army", "blitz"), 
        create_troop ("Tank", 4, "Army", None), 
        create_troop ("Tank", 4, "Army", None), 
        create_troop ("Tank(Elite)", 5, "Army", "elite"),
        create_troop ("Bomber(Bombard)", 1, "Both", "bombard"), 
        create_troop ("Bomber", 3, "Both", None), 
        create_troop ("Bomber", 3, "Both", None), 
        create_troop ("Bomber(Elite)", 4, "Both", "elite")
        ]

'''
startingResearchJP = [
        create_troop("Partisans", X, "Army", "partisan"),
        create_troop("Improved Research", 0, "Both, "impRD")
        ]
'''

startingJapan = [
        create_troop ("Plane(Bombard)", 0, "Both", "bombard"),
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
        create_troop ("Godzilla", 4, "Any", None),
        create_troop ("Ship", 1, "Navy", None),
        create_troop ("Ship", 1, "Navy", None),
        create_troop ("Ship", 1, "Navy", None),
        create_troop ("Ship", 1, "Navy", None),
        create_troop ("Ship", 2, "Navy", None),
        create_troop ("Ship", 2, "Navy", None),
        create_troop ("Ship", 3, "Navy", None),
        create_troop ("General", 1, "Army", "general"),  
        create_troop ("Admiral", 1, "Navy", "admiral"), 
        ]

westernEurope = [
        create_space("Industry", 1, "Navy", "drawReserves"),
        create_space("Research", 1, "Army", "addResearch"),
        create_space("VP 1", 1, "Both", "add 1 VP"),
        create_space("Bombard", 2, "Army", "bombard"),
        create_space("Industry", 2, "Army", "drawReserves"),
        create_space("Empty", 2, "Both", None),
        create_space("Research Industry", 3, "Both", "drawReseaerch"),
        create_space("Strategic Advantage < +3 >", 3, "Army", "add 3 to other theatre"),
        create_space("Empty", 3, "Both", None)
        ]
        
easternEurope = [
        create_space("Tactical Advantage +1", 1, "Army", "+1 to current theatre"),
        create_space("Industry", 1, "Army", "drawReserves"),
        create_space("VP 1", 2, "Army", "add 1 VP"),
        create_space("Research (2x)", 2, "Army", "addResearch2x"),
        create_space("Empty", 2, "Both", None),
        create_space("Bombard", 3, "Army", "bombard"),
        create_space("Tactical Advantage (+2)", 3, "Army", "add 2 to current theatre"),
        create_space("Strategic Advantage < +3 >", 3, "Army", "add 3 to any other theatre"),
        create_space("VP 2", 3, "Army", "add 2 to VP"),
        create_space("Empty", 3, "Army", None)
        ]

africa = [
        create_space("Strategic Advantage < +3 >", 1, "Army", "add 3 to any other theatre"),
        create_space("Tactical Advantage +1", 1, "Navy", "add 1 to current theatre"),
        create_space("Research", 1, "Both", "addResearch"),
        create_space("VP 1", 1, "Both", "add 1 VP"),
        create_space("Tactical Advantage (+2)", 2, "Army", "add 2 to current theatre"),
        create_space("Industry (2x)", 2, "Navy", "drawReserves2x"),
        create_space("Empty", 2, "Both", None)
        ]

pacific = [
        create_space("Bombard", 1, "Navy", "bombard"),
        create_space("Research", 1, "Navy", "addResearch"),
        create_space("Research (2x)", 2, "Navy", "addResearch2x"),
        create_space("Industry", 2, "Navy", "addReserve"),
        create_space("Strategic Advantage < +2 >", 2, "Navy", "add 2 to other theatre"),
        create_space("Empty", 2, "Both", None),
        create_space("Bombard", 3, "Navy", "bombard"),
        create_space("VP 2", 3, "Both", "add 2 VP"),
        create_space("Empty", 3, "Both", None)
        ]
        
southEastAsia = [
        create_space("VP 2", 1, "Navy", "add 2 VP"),
        create_space("VP 1", 1, "Both", "add 1 VP"),
        create_space("Strategic Advantage < +1 >", 1, "Both", "add 1 to other theatre"),
        create_space("Bombard", 2, "Navy", "bombard"),
        create_space("VP 2", 2, "Army", "add 2 VP"),
        create_space("Empty", 2, "Both", None)
        ]
        
