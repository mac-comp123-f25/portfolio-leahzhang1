import colorsys

# Define RGB coordinates
r = 0.2
g = 0.4
b = 0.4

# Convert the color from RGB
# coordinates to YIQ coordinates
yiq = colorsys.rgb_to_yiq(r, g, b)

# Print the yiq coordinates
print(yiq)