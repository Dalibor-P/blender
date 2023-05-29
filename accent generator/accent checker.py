import requests

colornames = ['rosewater', 'flamingo', 'pink', 'mauve', 'red', 'maroon', 'peach', 'yellow', 'green', 'teal', 'sky', 'sapphire', 'blue', 'lavender']

# Original colors
# latte_colors =     ['dc8a78', 'dd7878', 'ea76cb', '8839ef', 'd20f39', 'e64553', 'fe640b', 'df8e1d', '40a02b', '179299', '04a5e5', '209fb5', '1e66f5', '7287fd']
# frappe_colors =    ['f2d5cf', 'eebebe', 'f4b8e4', 'ca9ee6', 'e78284', 'ea999c', 'ef9f76', 'e5c890', 'a6d189', '81c8be', '99d1db', '85c1dc', '8caaee', 'babbf1']
# macchiato_colors = ['f4dbd6', 'f0c6c6', 'f5bde6', 'c6a0f6', 'ed8796', 'ee99a0', 'f5a97f', 'eed49f', 'a6da95', '8bd5ca', '91d7e3', '7dc4e4', '8aadf4', 'b7bdf8']
# mocha_colors =     ['f5e0dc', 'f2cdcd', 'f5c2e7', 'cba6f7', 'f38ba8', 'eba0ac', 'fab387', 'f9e2af', 'a6e3a1', '94e2d5', '89dceb', '74c7ec', '89b4fa', 'b4befe']

# Refined colors
#                   rosewater flamingo    pink     mauve      red      maroon    peach     yellow    green      teal      sky     sapphire    blue    lavender
latte_colors =     ['dc8a78', 'dd7878', 'ea76cb', 'e0b0ff', 'd20f39', 'e64553', 'fe640b', 'df8e1d', '49b530', '19a1a9', '04a5e5', '209fb5', '6898f8', '7287fd']
frappe_colors =    ['f2d5cf', 'eebebe', 'f4b8e4', 'ca9ee6', 'e78284', 'ea999c', 'ef9f76', 'e5c890', 'a6d189', '81c8be', '99d1db', '85c1dc', '8caaee', 'babbf1']
macchiato_colors = ['f4dbd6', 'f0c6c6', 'f5bde6', 'c6a0f6', 'ed8796', 'ee99a0', 'f5a97f', 'eed49f', 'a6da95', '8bd5ca', '91d7e3', '7dc4e4', '8aadf4', 'b7bdf8']
mocha_colors =     ['f5e0dc', 'f2cdcd', 'f5c2e7', 'cba6f7', 'f38ba8', 'eba0ac', 'fab387', 'f9e2af', 'a6e3a1', '94e2d5', '89dceb', '74c7ec', '89b4fa', 'b4befe']

# text
latte_text = '4c4f69'
# frappe_text = 'c6d0f5'
# macchiato_text = 'cad3f5'
# mocha_text = 'cdd6f4'

# base
# latte_text = 'eff1f5'
frappe_text = '303446'
macchiato_text = '24273a'
mocha_text = '1e1e2e'

def check_flavor (colorhexes, colornames, colorstring, foregroundstring):
    for colorhex, colorname in zip(colorhexes, colornames):
        api_url = 'https://webaim.org/resources/contrastchecker/?fcolor=' + foregroundstring + '&bcolor=' + colorhex + '&api'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            if float(data['ratio']) < 2.0:
                severity = '***'
            elif float(data['ratio']) < 2.5:
                severity = '**'
            elif float(data['ratio']) < 3.0:
                severity = '*'
            else:
                severity = ''
            print(data['ratio'] + ' - ' + colorstring + ' ' +  colorname + ' (#' + colorhex + ') ' + severity)
        except requests.exceptions.RequestException as e:
            print("Error occurred:",e)

check_flavor(latte_colors, colornames, 'latte', latte_text)
print()
check_flavor(frappe_colors, colornames, 'frappe', frappe_text)
print()
check_flavor(macchiato_colors, colornames, 'macchiato', macchiato_text)
print()
check_flavor(mocha_colors, colornames, 'mocha', mocha_text)

##################################################
#                Original colors                 #
##################################################

# 3.02 - latte rosewater (#dc8a78) 
# 2.67 - latte flamingo (#dd7878) *
# 3.02 - latte pink (#ea76cb) 
# 1.47 - latte mauve (#8839ef) ***
# 1.47 - latte red (#d20f39) ***
# 2.03 - latte maroon (#e64553) **
# 2.67 - latte peach (#fe640b) *
# 3.05 - latte yellow (#df8e1d) 
# 2.38 - latte green (#40a02b) **
# 2.13 - latte teal (#179299) **
# 2.85 - latte sky (#04a5e5) *
# 2.54 - latte sapphire (#209fb5) *
# 1.62 - latte blue (#1e66f5) ***
# 2.50 - latte lavender (#7287fd) *

# 1.10 - frappe rosewater (#f2d5cf) ***
# 1.07 - frappe flamingo (#eebebe) ***
# 1.07 - frappe pink (#f4b8e4) ***
# 1.43 - frappe mauve (#ca9ee6) ***
# 1.73 - frappe red (#e78284) ***
# 1.44 - frappe maroon (#ea999c) ***
# 1.38 - frappe peach (#ef9f76) ***
# 1.05 - frappe yellow (#e5c890) ***
# 1.13 - frappe green (#a6d189) ***
# 1.25 - frappe teal (#81c8be) ***
# 1.09 - frappe sky (#99d1db) ***
# 1.28 - frappe sapphire (#85c1dc) ***
# 1.51 - frappe blue (#8caaee) ***
# 1.19 - frappe lavender (#babbf1) ***

# 1.12 - macchiato rosewater (#f4dbd6) ***
# 1.04 - macchiato flamingo (#f0c6c6) ***
# 1.06 - macchiato pink (#f5bde6) ***
# 1.44 - macchiato mauve (#c6a0f6) ***
# 1.66 - macchiato red (#ed8796) ***
# 1.45 - macchiato maroon (#ee99a0) ***
# 1.30 - macchiato peach (#f5a97f) ***
# 1.02 - macchiato yellow (#eed49f) ***
# 1.08 - macchiato green (#a6da95) ***
# 1.13 - macchiato teal (#8bd5ca) ***
# 1.08 - macchiato sky (#91d7e3) ***
# 1.29 - macchiato sapphire (#7dc4e4) ***
# 1.51 - macchiato blue (#8aadf4) ***
# 1.21 - macchiato lavender (#b7bdf8) ***

# 1.14 - mocha rosewater (#f5e0dc) ***
# 1.00 - mocha flamingo (#f2cdcd) ***
# 1.05 - mocha pink (#f5c2e7) ***
# 1.40 - mocha mauve (#cba6f7) ***
# 1.60 - mocha red (#f38ba8) ***
# 1.42 - mocha maroon (#eba0ac) ***
# 1.22 - mocha peach (#fab387) ***
# 1.13 - mocha yellow (#f9e2af) ***
# 1.02 - mocha green (#a6e3a1) ***
# 1.02 - mocha teal (#94e2d5) ***
# 1.07 - mocha sky (#89dceb) ***
# 1.30 - mocha sapphire (#74c7ec) ***
# 1.45 - mocha blue (#89b4fa) ***
# 1.23 - mocha lavender (#b4befe) ***

##################################################
#                Improved colors                 #
##################################################

# 3.02 - latte rosewater (#dc8a78) 
# 2.67 - latte flamingo (#dd7878) *
# 3.02 - latte pink (#ea76cb) 
# 4.49 - latte mauve (#e0b0ff) 
# 1.47 - latte red (#d20f39) ***
# 2.03 - latte maroon (#e64553) **
# 2.67 - latte peach (#fe640b) *
# 3.05 - latte yellow (#df8e1d) 
# 3.01 - latte green (#49b530) 
# 2.55 - latte teal (#19a1a9) *
# 2.85 - latte sky (#04a5e5) *
# 2.54 - latte sapphire (#209fb5) *
# 2.82 - latte blue (#6898f8) *
# 2.50 - latte lavender (#7287fd) *

# 8.90 - frappe rosewater (#f2d5cf) 
# 7.47 - frappe flamingo (#eebebe) 
# 7.51 - frappe pink (#f4b8e4) 
# 5.59 - frappe mauve (#ca9ee6) 
# 4.64 - frappe red (#e78284) 
# 5.59 - frappe maroon (#ea999c) 
# 5.80 - frappe peach (#ef9f76) 
# 7.62 - frappe yellow (#e5c890) 
# 7.09 - frappe green (#a6d189) 
# 6.41 - frappe teal (#81c8be) 
# 7.32 - frappe sky (#99d1db) 
# 6.25 - frappe sapphire (#85c1dc) 
# 5.33 - frappe blue (#8caaee) 
# 6.72 - frappe lavender (#babbf1) 

# 11.1 - macchiato rosewater (#f4dbd6) 
# 9.53 - macchiato flamingo (#f0c6c6) 
# 9.32 - macchiato pink (#f5bde6) 
# 6.84 - macchiato mauve (#c6a0f6) 
# 5.96 - macchiato red (#ed8796) 
# 6.80 - macchiato maroon (#ee99a0) 
# 7.61 - macchiato peach (#f5a97f) 
# 10.2 - macchiato yellow (#eed49f) 
# 9.17 - macchiato green (#a6da95) 
# 8.74 - macchiato teal (#8bd5ca) 
# 9.13 - macchiato sky (#91d7e3) 
# 7.63 - macchiato sapphire (#7dc4e4) 
# 6.56 - macchiato blue (#8aadf4) 
# 8.16 - macchiato lavender (#b7bdf8) 

# 12.9 - mocha rosewater (#f5e0dc) 
# 11.2 - mocha flamingo (#f2cdcd) 
# 10.7 - mocha pink (#f5c2e7) 
# 8.07 - mocha mauve (#cba6f7) 
# 7.08 - mocha red (#f38ba8) 
# 7.93 - mocha maroon (#eba0ac) 
# 9.26 - mocha peach (#fab387) 
# 12.9 - mocha yellow (#f9e2af) 
# 11.0 - mocha green (#a6e3a1) 
# 11.0 - mocha teal (#94e2d5) 
# 10.5 - mocha sky (#89dceb) 
# 8.68 - mocha sapphire (#74c7ec) 
# 7.78 - mocha blue (#89b4fa) 
# 9.16 - mocha lavender (#b4befe) 