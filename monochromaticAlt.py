def hsv_to_rgb( h, s, v):
        if s == 0.0:
            return v, v, v
        i = int(h*6.0) # XXX assume int() truncates!
        f = (h*6.0) - i
        p = v*(1.0 - s)
        q = v*(1.0 - s*f)
        t = v*(1.0 - s*(1.0-f))
        i = i%6
        if i == 0:
            return v, t, p
        if i == 1:
            return q, v, p
        if i == 2:
            return p, v, t
        if i == 3:
            return p, q, v
        if i == 4:
            return t, p, v
        if i == 5:
            return v, p, q
        # Cannot get here

def rgb_to_hsv( r, g, b):
        maxc = max(r, g, b)
        minc = min(r, g, b)
        rangec = (maxc-minc)
        v = maxc
        if minc == maxc:
            return 0.0, 0.0, v
        s = rangec / maxc
        rc = (maxc-r) / rangec
        gc = (maxc-g) / rangec
        bc = (maxc-b) / rangec
        if r == maxc:
            h = bc-gc
        elif g == maxc:
            h = 2.0+rc-bc
        else:
            h = 4.0+gc-rc
        h = (h/6.0) % 1.0
        return h, s, v
def colorChange (ColorInput, numberColors):
    colorHSV = list(rgb_to_hsv(ColorInput[0] / 255, ColorInput[1] / 255, ColorInput[2] / 255))
    h = colorHSV[0] * 360
    s = colorHSV[1] * 100
    v = (colorHSV[2] * 100) / 255

    newcolorHSV = [h,s,v]

     
    return output
     
def monochromaticAlt ( ColorInput, numberColors):
        colorHSV = list(rgb_to_hsv(ColorInput[0] / 255, ColorInput[1] / 255, ColorInput[2] / 255))
        print (colorHSV[2])
        #h = colorHSV[0] * 360
        #s = colorHSV[1] * 100
        #v = round(colorHSV[2] * 100)

        #newcolorHSV = [h,s,v]

        num = numberColors
        color = colorHSV
        result = []
        listRGB = []
        for steps in range(num):
            if steps > 0:
                blank = ((color[1]*100) - ((color[1]*100) / steps))/100
                #blankrounded = round(blank)
                newColor = [color[0], blank, color[2]]
                result.append(newColor)
            print (result)
        
        result.append(color)
        output = []
        for colors in result:
            colorRGB = hsv_to_rgb(h=colors[0], s=colors[1], v=colors[2])
            newcolorRGB = [colorRGB[0]*255, colorRGB[1]*255, colorRGB[2]*255]
            output.append(newcolorRGB)

        return output

color = [250, 0 , 0]
number = 5
listColor = monochromaticAlt(ColorInput=color, numberColors=number)
print(listColor)