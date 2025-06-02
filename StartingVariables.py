axisVP = 0
alliedVP = 0
japanVP = 0
westernEuropeTrack = 0
easternEuropeTrack = 0
africaTrack = 0
pacificTrack = 0
southEastAsiaTrack = 0

lastUsedTroop = []
strategems = []

startingAxis = [
        {"Plane(Blitz)": 0, "Type": "Both", "Special": "Blitz"},
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
        {"Tank": 3, "Type": "Army", "Special": None},
        {"Ship": 1, "Type": "Navy", "Special": None}, 
        {"Ship": 1, "Type": "Navy", "Special": None}, 
        {"Ship": 1, "Type": "Navy", "Special": None},
        {"Ship": 2, "Type": "Navy", "Special": None}, 
        {"Ship": 2, "Type": "Navy", "Special": None},
        {"Ship": 3, "Type": "Navy", "Special": None}, 
        {"Ship": 3, "Type": "Navy", "Special": None},
        {"General": 1, "Type": "Army", "Special": "General + Army"},
        {"Admiral": 1, "Type": "Navy", "Special": "Admiral + Navy"}
        ]

startingAllied = [
        {"Plane(Blitz)": 0, "Type": "Both", "Special": "Blitz"},
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
        {"Tank": 3, "Type": "Army", "Special": None},
        {"Ship": 1, "Type": "Navy", "Special": None}, 
        {"Ship": 1, "Type": "Navy", "Special": None}, 
        {"Ship": 1, "Type": "Navy", "Special": None},
        {"Ship": 2, "Type": "Navy", "Special": None}, 
        {"Ship": 2, "Type": "Navy", "Special": None},
        {"Ship": 3, "Type": "Navy", "Special": None}, 
        {"Ship": 3, "Type": "Navy", "Special": None},
        {"General": 1, "Type": "Army", "Special": "General + Army"},
        {"Admiral": 1, "Type": "Navy", "Special": "Admiral + Navy"}
        ]

startingResearch = [
        {"Nuke": 7, "Type": "Army", "Special": "-2 all other open theaters"}, 
        {"Spy": "X", "Type": "X", "Special": "Copy the last used troop"}, 
        {"Scientist": 0, "Type": "Both", "Special": "Can be placed anywhere"},
        {"Carrier(Bombard)": 2, "Type": "Navy", "Special": "Bombard"}, 
        {"Carrier(Blitz)": 1, "Type": "Navy", "Special": "Blitz"}, 
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

startingResearchJP = [
        {"Partisans": X, "Type": "Army", "Special": "3 if behind 1 if ahead"},
        {"Improved research" : X, "Type": "Both", "Special": "Triggers board space twice"}
        ]

startingJapan = [
        {"Plane(Bombard)": 0, "Type": "Both", "Special": "Bombard"},
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
        {"General": 1, "Type": "Army", "Special": "General + Army"},
        {"Admiral": 1, "Type": "Navy", "Special": "Admiral + Navy"}
        ]

westernEurope = [
        {}
        ]

easternEurope = [
        {}
        ]

africa = [
        {}
        ]

pacific = [
        {"Space": "Bombard", "Row": 1, "Type": "Navy", "Special": "Bombard"}, 
        {"Space": "Research", "Row": 1, "Type": "Navy", "Special": "draw from research"},
        {"Space": "Research (x2)", "Row": 2, "Type": "Navy", "Special": "Draw twice from research"}, 
        {"Space": "Industry", "Row": 2, "Type": "Navy", "Special": "Draw from reserves"}, 
        {"Space": "Strategic Advantage +2", "Row": 2, "Type": "Navy", "Special": "Advance track of one other theatre"},
        {"Space": "Blank", "Row": 2, "Type": "Both", "Special": None},
        {"Space": "Bombard", "Row": 3, "Type": "Navy", "Special": "Bombard"},
        {"Space": "Victory Point (2)", "Row": 3, "Type": "Both", "Special": "Add 2 VP"},
        {"Space": "Blank", "Row": 3, "Type": "Both", "Special": None}
        ]

southEastAsia = [
        {}
        ]
