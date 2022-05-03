from configparser import ConfigParser
# from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
config = ConfigParser()

# parse existing file
# config.read('Hry/Pexeso/farby.ini')

# # read values from a section
# string_val = config.get('section_a', 'string_val')
# bool_val = config.getboolean('section_a', 'bool_val')
# int_val = config.getint('section_a', 'int_val')
# float_val = config.getfloat('section_a', 'pi_val')

# # update existing value
# config.set('section_a', 'string_val', 'world')

farby = {
'#00FFFF' : 'Aqua', '#7FFFD4' : 'Aquamarine', '#000000' : 'Black',
'#0000FF' : 'Blue', '#8A2BE2' : 'BlueViolet', '#5F9EA0' : 'CadetBlue',
'#D2691E' : 'Chocolate', '#6495ED' : 'CornflowerBlue', '#DC143C' : 'Crimson',
'#00008B' : 'DarkBlue', '#008B8B' : 'DarkCyan', '#B8860B' : 'DarkGoldenRod',

'#A9A9A9' : 'DarkGrey', '#006400' : 'DarkGreen', '#BDB76B' : 'DarkKhaki',
'#8B008B' : 'DarkMagenta', '#556B2F' : 'DarkOliveGreen', '#FF8C00' : 'DarkOrange',
'#8FBC8F' : 'DarkSeaGreen', '#483D8B' : 'DarkSlateBlue', '#FF1493' : 'DeepPink',
'#1E90FF' : 'DodgerBlue', '#B22222' : 'FireBrick', '#FF00FF' : 'Fuchsia',

'#FFD700' : 'Gold', '#DAA520' : 'GoldenRod', '#808080' : 'Grey', # rovnaká farba ako '..Gray'
'#ADFF2F' : 'GreenYellow', '#FF69B4' : 'HotPink', '#CD5C5C' : 'IndianRed',
'#4B0082' : 'Indigo', '#F0E68C' : 'Khaki', '#FFF0F5' : 'LavenderBlush',
'#7CFC00' : 'LawnGreen', '#FFFACD' : 'LemonChiffon', '#F08080' : 'LightCoral',

'#E0FFFF' : 'LightCyan', '#D3D3D3' : 'LightGrey', '#FFB6C1' : 'LightPink',
'#FFA07A' : 'LightSalmon', '#87CEFA' : 'LightSkyBlue', '#B0C4DE' : 'LightSteelBlue',
'#32CD32' : 'LimeGreen', '#800000' : 'Maroon', '#66CDAA' : 'MediumAquaMarine',
'#BA55D3' : 'MediumOrchid', '#3CB371' : 'MediumSeaGreen', '#7B68EE' : 'MediumSlateBlue',

'#00FA9A' : 'MediumSpringGreen', '#48D1CC' : 'MediumTurquoise', '#C71585' : 'MediumVioletRed',
'#808000' : 'Olive', '#FFA500' : 'Orange', '#FF4500' : 'OrangeRed',
'#98FB98' : 'PaleGreen', '#DDA0DD' : 'Plum', '#B0E0E6' : 'PowderBlue',
'#FF0000' : 'Red', '#BC8F8F' : 'RosyBrown', '#4169E1' : 'RoyalBlue',

'#8B4513' : 'SaddleBrown', '#FA8072' : 'Salmon', '#F4A460' : 'SandyBrown',
'#2E8B57' : 'SeaGreen', '#A0522D' : 'Sienna', '#C0C0C0' : 'Silver',
'#4682B4' : 'SteelBlue', '#D2B48C' : 'Tan', '#FF6347' : 'Tomato',
'#EE82EE' : 'Violet', '#FFFF00' : 'Yellow', '#9ACD32' : 'YellowGreen'}

# add a new section and some values
config.add_section('farby')

list(farby.items()) 
# Potom cez ne vieme takto iterovat. PORIADNE SI TOTO NASTUDUJTE 
for key, value in farby.items():
    # print(f"Key: {key}, Value {value}")
    config.set('farby', key[1:], value)

# save to a file
with open('Hry/Pexeso/farby.ini', 'w') as configfile:
    config.write(configfile)
