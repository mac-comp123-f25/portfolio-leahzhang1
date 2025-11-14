import imagetools

def weighted_scale(pic):
    new_pic = pic.copy()
    for (x, y) in new_pic:
        (r, g, b) = new_pic.getColor(x, y)
        lumin = r/2 + g/4 + b/4
        new_pic.setColor(x, y, (lumin, lumin, lumin))

    return new_pic

