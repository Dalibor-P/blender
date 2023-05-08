# Contributing!

🎉 First off, thanks for taking the time to contribute! 🎉

## Puccinier issue

This port started off with a need for a light theme for Blender, thus Latte flavor was created. I will continue to maintain the Latte flavor for the forseeable future.

The Frappé, Macchiato and Mocha flavors were created using a [Puccinier](https://github.com/catppuccin/toolbox#%EF%B8%8F-puccinier) converter off of the Latte Flavor. The results are mostly good, but some UI elements appear too bright. For example, Properties editor navbar background, Top header background, 3D Viewport grid color or Editor outlines all appear a little too bright.

## How to contribute?

You can contribute by reviewing a Puccinier-generated dark theme `accent generator/frappe_master_for_contribution.xml` and checking all UI elements in Blender and fixing any inconsistencies you can find. This file also contains two colors used in accent generating script:

* `#bada55` for primary accents (everywhere in UI)
* `#bada66` for secondary accents (visible when selecting multiple objects or other elements)

Respect these two colors and do not change them. The `accent generator/accent generator.py` script uses these colors to generate all accent variants that are saved in `themes/`. The python script can be later edited to generate Macchiato and Mocha off of Frappé and keep Latte separate.
