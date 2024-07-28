listColour = ["Black", "Red", "Maroon", "Yellow"]
ListColourCode = ["000000", "FF0000", "800000", "FFFF00"]

Colours = []
for i in range(0,4):
    Colours.append({"ColourName": listColour[i], "ColourCode": ListColourCode[i]})
    
print(Colours)