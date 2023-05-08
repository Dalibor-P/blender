import subprocess
import os
from colorutils import Color # pip install colorutils

# Define a function to replace colors in an XML file.
def replace_colors(flavor, accent_name, accent_hex, themes_path):
    # Load the primary accent color and calculate the secondary accent color.
    loaded_color = Color(hex=accent_hex)
    loaded_color_str = str(loaded_color.hsv)
    loaded_color_tupple = eval(loaded_color_str)
    hue, saturation, value = loaded_color_tupple    
    darker_color = Color(hsv=(hue, saturation, round(value*0.5,3)))

    # print('Primary accent color as rgb: ' + str(loaded_color) + '.')
    # print('Primary accent color as hex: ' + str(loaded_color.hex) + '.')
    # print('Primary accent color as hsv: ' + str(loaded_color.hsv) + '.')
    # print('Secondary accent color as rgb: ' + str(darker_color) + '.')
    # print('Secondary accent color as hex: ' + str(darker_color.hex) + '.')
    # print('Secondary accent color as hsv: ' + str(darker_color.hsv) + '.')

    # Open the master XML file and read its contents.
    with open(flavor + '_master.xml', 'r') as file:
        file_content = file.read()

    # Replace the color codes in the XML file with the new color codes.
    new_file_content = file_content.replace('#bada55', str(loaded_color.hex))
    new_file_content = new_file_content.replace('#bada66', str(darker_color.hex))

    # Create a new XML file with the replaced colors.
    with open(os.path.join(themes_path, flavor + '_' + accent_name + '.xml'), 'w') as file:
        file.write(new_file_content)
    print('Created '+ accent_name + ' variant.')

# Loop through all old themes files in the themes folder and remove them.
themes_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'themes')
for f in os.listdir(themes_path):
    os.remove(os.path.join(themes_path, f))

# Run Puccinier to generate Frappé, Macchiato and Mocha flavors off of Latte
cmd_str = ".\puccinier-0.1.2-x86_64-pc-windows-msvc.exe -s .\latte_master.xml -o frappe macchiato mocha"
subprocess.run(cmd_str, shell=True)
os.rename('frappe.xml', 'frappe_master.xml')
os.rename('macchiato.xml', 'macchiato_master.xml')
os.rename('mocha.xml', 'mocha_master.xml')

# Create lists of flavors and colors with their respective hex codes.
colors = ['rosewater', 'flamingo', 'pink', 'mauve', 'red', 'maroon', 'peach', 'yellow', 'green', 'teal', 'sky', 'sapphire', 'blue', 'lavender']
latte_colors =     ['#dc8a78', '#dd7878', '#ea76cb', '#8839ef', '#d20f39', '#e64553', '#fe640b', '#df8e1d', '#40a02b', '#179299', '#04a5e5', '#209fb5', '#1e66f5', '#7287fd']
frappe_colors =    ['#f2d5cf', '#eebebe', '#f4b8e4', '#ca9ee6', '#e78284', '#ea999c', '#ef9f76', '#e5c890', '#a6d189', '#81c8be', '#99d1db', '#85c1dc', '#8caaee', '#babbf1']
macchiato_colors = ['#f4dbd6', '#f0c6c6', '#f5bde6', '#c6a0f6', '#ed8796', '#ee99a0', '#f5a97f', '#eed49f', '#a6da95', '#8bd5ca', '#91d7e3', '#7dc4e4', '#8aadf4', '#b7bdf8']
mocha_colors =     ['#f5e0dc', '#f2cdcd', '#f5c2e7', '#cba6f7', '#f38ba8', '#eba0ac', '#fab387', '#f9e2af', '#a6e3a1', '#94e2d5', '#89dceb', '#74c7ec', '#89b4fa', '#b4befe']

# Call the replace_colors function to generate all flavors and accent combinations.
for accent_name, accent_hex in zip(colors, latte_colors):
    replace_colors('latte', accent_name, accent_hex, themes_path)
print('Created all Latte variants!')

for accent_name, accent_hex in zip(colors, frappe_colors):
    replace_colors('frappe', accent_name, accent_hex, themes_path)
print('Created all Frappé variants!')

for accent_name, accent_hex in zip(colors, macchiato_colors):
    replace_colors('macchiato', accent_name, accent_hex, themes_path)
print('Created all Macchiato variants!')

for accent_name, accent_hex in zip(colors, mocha_colors):
    replace_colors('mocha', accent_name, accent_hex, themes_path)
print('Created all Mocha variants!')

# Remove the generated master XML files.
os.remove('frappe_master.xml')
os.remove('macchiato_master.xml')
os.remove('mocha_master.xml')