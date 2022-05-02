from PIL import Image
filename = r'Obrazky/ico/logo.png'
img = Image.open(filename)
img.save('logo.ico')

# ====================

# Optionally, you may specify the icon sizes you want:

icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
img.save('logo.ico', sizes=icon_sizes)