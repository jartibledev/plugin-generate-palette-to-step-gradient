import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('Gtk', '3.0') # O '4.0' según la versión de GIMP 3
from gi.repository import Gtk
gi.require_version('GObject', '2.0')
from gi.repository import GObject
from gi.repository import Gegl

import sys

plug_in_proc   = "plug-in-jartibledev-py3-generate-palette-to-step-gradient"
plug_in_binary = "py3-generate-palette-to-step-gradient"

class SpinButtonWindow(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.connect('destroy', Gtk.main_quit)

        adjustment = Gtk.Adjustment(upper=100, step_increment=1, page_increment=10)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)
        self.spinbutton.connect("value-changed", self.on_value_changed)
        self.pack_start(self.spinbutton, False, False, 0)

        check_numeric = Gtk.CheckButton(label="Numeric")
        check_numeric.connect("toggled", self.on_numeric_toggled)
        self.pack_start(check_numeric, False, False, 0)

        check_ifvalid = Gtk.CheckButton(label="If Valid")
        check_ifvalid.connect("toggled", self.on_ifvalid_toggled)
        self.pack_start(check_ifvalid, False, False, 0)

    def on_value_changed(self, scroll):
        print(self.spinbutton.get_value_as_int())

    def on_numeric_toggled(self, button):
        self.spinbutton.set_numeric(button.get_active())

    def on_ifvalid_toggled(self, button):
        if button.get_active():
            policy = Gtk.SpinButtonUpdatePolicy.IF_VALID
        else:
            policy = Gtk.SpinButtonUpdatePolicy.ALWAYS
        self.spinbutton.set_update_policy(policy)
    
    @property
    def get_number(self):
        number = self.spinbutton.get_value_as_int()
        return number

class GeneratePalette :

    def __init__(self):
        self.listColorRgb = []     

    def Normalize(self, Value,Min,Max):
        Output = Value
        if Value > Max:
            Output = Max
        elif Value < Min:
            Output = Min
        return Output
    
    def rgb_to_hsv(self, r, g, b):
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
    
    def hsv_to_rgb(self, h, s, v):
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

    def createPalette (self, hexColorInput, numberColorsInput):
            hexColor = hexColorInput
            numberColors = numberColorsInput

            rgbColor = self.hexToRgb(hexColor)
            self.listColorRgb = self.monochromaticAlt( rgbColor, numberColors )

            hexListColor = self.generateHexList(self.listColorRgb)
            print (hexListColor)

            return hexListColor
    
    def rgbToHex(self, r,g,b):
        return ('#{:02x}{:02x}{:02x}'). format(r, g, b)

    def hexToRgb(self, hexColor : str ):
            hexColor = hexColor.lstrip('#')
            return list(int(hexColor[i:i+2],16) for i in (0, 2, 4))

    def generateHexList( self, listColorsRgb ):
        mylistColorsRgb = listColorsRgb
        sortedListColorsRgb = self.sortByLuminance( mylistColorsRgb )
        listColorHex = []
        numbersColors = len(sortedListColorsRgb)
        for i in range(numbersColors) :
            listColorHex.append( self.rgbToHex(sortedListColorsRgb[i][0], sortedListColorsRgb[i][1], sortedListColorsRgb[i][2] ))
        return listColorHex
    def sortByLuminance(self, colores_rgb):
        def calcular_luminancia(rgb):
            r, g, b = rgb
            return 0.2126 * r + 0.7152 * g + 0.0722 * b

        return sorted(colores_rgb, key=calcular_luminancia, reverse=True)

    def monochromaticAlt (self, ColorInput, numberColors):
        colorHSV = list(self.rgb_to_hsv(ColorInput[0] / 255, ColorInput[1] / 255, ColorInput[2] / 255))
        print (colorHSV[2])

        num = numberColors
        color = colorHSV
        result = []
        listRGB = []
        for steps in range(num):
            if steps > 0:
                blank = ((color[1]*100) - ((color[1]*100) / steps))/100
                newColor = [color[0], blank, color[2]]
                result.append(newColor)
            print (result)
        
        result.append(color)
        output = []
        for colors in result:
            colorRGB = self.hsv_to_rgb(h=colors[0], s=colors[1], v=colors[2])
            newcolorRGB = [round(colorRGB[0]*255), round(colorRGB[1]*255), round(colorRGB[2]*255)]
            output.append(newcolorRGB)

        return output

    def monochromaticColor(self, ColorInput, numberColors):
        color = ColorInput
        color = list(self.rgb_to_hsv(ColorInput[0] / 255, ColorInput[1] / 255, ColorInput[2] / 255))
        
        numberColors_selectionated = numberColors
        percentage_increment = 100 / numberColors_selectionated

        increment = [ 0, percentage_increment/100, numberColors_selectionated/100 ]
        result = []
        output = []
        for x in increment:
            for y in increment:
                result.append(list(map(lambda x: self.Normalize(round(x * 255),0,255), self.hsv_to_rgb(color[0], self.Normalize(color[1],0,100) + x, self.Normalize(color[2] + y,0,100)))))
                result.append(list(map(lambda x: self.Normalize(round(x * 255),0,255), self.hsv_to_rgb(color[0], self.Normalize(color[1],0,100) - x, self.Normalize(color[2] - y,0,100)))))
        [output.append(x) for x in result if x not in output]
        
        return output

    @property 
    def getRgbList(self):
        listSortedColor = self.sortByLuminance(self.listColorRgb) 

        return listSortedColor

class ColorButton(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.connect('destroy', Gtk.main_quit)
        self.colorRgb = []
        self.colorHex=[]

        self.colorbutton = Gtk.ColorButton()
        self.colorbutton.connect('color-set', self.on_color_set)
        self.add(self.colorbutton)
        self.color = self.colorbutton.get_rgba()

    def on_color_set(self, colorbutton):
        color = colorbutton.get_rgba()

        red = int(color.red * 255)
        green = int(color.green * 255)
        blue = int(color.blue * 255)

        self.colorRgb = [red, green, blue]
        #self.get_color 
        #print (self.colorRgb)
        #return self.colorRgb
        
        print('Hex: #%02x%02x%02x' % (red, green, blue))
        self.colorHex = "#%02x%02x%02x" % (red, green, blue)
    @property
    def get_color (self):
        color = self.colorHex
        return color

def selector_color_run(procedure, run_mode, image, drawables, config, data):
  if run_mode == Gimp.RunMode.INTERACTIVE:
       
       
        # Crear un diálogo
       
        dialog = Gtk.Dialog(title="Mi Plugin con Botón")
        dialog.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        dialog.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)

        #box = Gtk.Box()
        
        # Añadir un botón personalizado
        colorButton = ColorButton()
        colorButton.set_halign(Gtk.Align.CENTER)
        colorButton.set_valign(Gtk.Align.CENTER)
        colorButton.set_hexpand(True)
        colorButton.set_vexpand(True)
        #dialog.get_content_area().pack_start(box, True, False, 10)
        # Añadir el botón al área de contenido del diálogo
       
        dialog.get_content_area().pack_start(colorButton, True, False, 10)
        colorButton.show_all()
        
        #SpinButton
        spinButton = SpinButtonWindow()
        spinButton.set_halign(Gtk.Align.CENTER)
        spinButton.set_valign(Gtk.Align.CENTER)
        spinButton.set_hexpand(True)
        spinButton.set_vexpand(True)
        dialog.get_content_area().pack_start(spinButton, True, False, 10)
        spinButton.show_all() 
        
        #PaletteName
        entry = Gtk.Entry()
        entry.set_text("Write the palette name")
        entry.set_halign(Gtk.Align.CENTER)
        entry.set_valign(Gtk.Align.CENTER)
        entry.set_hexpand(True)
        entry.set_vexpand(True)
        #box.pack
        dialog.get_content_area().pack_start(entry, True, False, 10)
        entry.show_all()

        def printGetters (widget):

            color = colorButton.get_color
            print(color)

            numberPalete = spinButton.get_number
            print(numberPalete)

            generatePalete = GeneratePalette()
            listHexColor = generatePalete.createPalette(hexColorInput=color, numberColorsInput=numberPalete)

            
            name = entry.get_text()
            print(name)

            procedure = Gimp.get_pdb().lookup_procedure('gimp-palette-new') 
            config = procedure.create_config(); config.set_property('name', name); result = procedure.run(config)
            success = result.index(0)
            palette = result.index(1)

            geglColor = []
            for numbers in range(numberPalete):
                colorGegl = Gegl.Color.new(listHexColor[numbers])
                geglColor.append(colorGegl)
            
            
            for number in range(numberPalete):
                entry_name = f"Color:{listHexColor[number]}"
                procedure = Gimp.get_pdb().lookup_procedure('gimp-palette-add-entry')
                config = procedure.create_config(); config.set_property('palette', palette)
                config.set_property('entry-name', entry_name)
                config.set_property('color', geglColor[number])
                result = procedure.run(config)
                success = result.index(0)
                entry_num = result.index(1)
            
            num_colors = palette.get_color_count()
            num_segments = num_colors - 1
            make_gradient(palette, num_segments, num_colors)

        #crear paleta
        buttonCreatePalette = Gtk.Button(label = "Create Palette")
        buttonCreatePalette.connect("clicked",printGetters )
        buttonCreatePalette.set_halign(Gtk.Align.CENTER)
        buttonCreatePalette.set_valign(Gtk.Align.CENTER)
        buttonCreatePalette.set_hexpand(True)
        buttonCreatePalette.set_vexpand(True)
        dialog.get_content_area().pack_start(buttonCreatePalette, True, False, 0)
        buttonCreatePalette.show_all()




        # Mostrar diálogo
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            # Lógica de GIMP
            dialog.destroy()
            return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)
        else:
            dialog.destroy()

        
  return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)

def make_gradient(palette, num_segments, num_colors):

    # name the gradient same as the source palette
    # For now, the name of a resource is the same as the ID
    palette_name = palette.get_name()
    gradient = Gimp.Gradient.new(palette_name)
    # assert gradient is valid but is has only one segment
    assert gradient.get_number_of_segments() == 1

    # split one segment into desired count
    # index is zero-based
    gradient.segment_range_split_uniform(0, 0, num_segments)
   
    palette_colors = palette.get_colors()
    for color_number in range(0, num_segments):
        if color_number == num_colors - 1:
            color_number_next = 0
        else:
            color_number_next = color_number + 1
        color_left = palette_colors[color_number]
        color_right = palette_colors[color_number_next]
        gradient.segment_set_left_color(color_number, color_left)
        gradient.segment_set_right_color(color_number, color_right)
        gradient.segment_range_set_blending_function(color_number, color_number_next, Gimp.GradientSegmentType.STEP)

    
    # Side effects on the context. Probably not what most would expect.
    Gimp.context_set_gradient(gradient)
    return gradient

class SetUpPixelArt (Gimp.PlugIn):
  def do_query_procedures(self):
    return [ plug_in_proc ]

  def do_create_procedure(self, name):
    procedure = None

    if name == plug_in_proc:
      procedure = Gimp.ImageProcedure.new(self, name,
                                          Gimp.PDBProcType.PLUGIN,
                                          selector_color_run, None)
      procedure.set_sensitivity_mask (Gimp.ProcedureSensitivityMask.DRAWABLE |
                                      Gimp.ProcedureSensitivityMask.NO_DRAWABLES)
      procedure.set_menu_label("Palette to Gradient Generator")
      procedure.set_attribution("JartibleDev", "JartibleDev, Palette to gradient step generator", "2026")
      procedure.add_menu_path ("<Image>/Palette to Gradient")
      procedure.set_documentation ("Palete to gradient step generator",
                                   "This plugin is useful to automatize your creation of palettes to painting areas in pixel art. " + \
                                   "The plugin generate a palette from a choosen colour and return a degradade that you can use in pincel to paint areas.",
                                   None)
    return procedure

Gimp.main(SetUpPixelArt.__gtype__, sys.argv)