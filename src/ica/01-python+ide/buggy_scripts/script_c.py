# This program converts celsius to fahrenheit

cels_temp = 30
fraction = 9/5   #Semantic error here, the correct fraction should be 9/5 instead of 5/9 to give the right value of the converted fahr
fahr_temp = (cels_temp * fraction) + 32
print(fahr_temp)