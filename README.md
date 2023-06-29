<h3 align="center">
    <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
    <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
    Catppuccin for <a href="https://www.blender.org/">Blender</a>
    <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
    <a href="https://github.com/Dalibor-P/blender/stargazers"><img src="https://img.shields.io/github/stars/Dalibor-P/blender?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/Dalibor-P/blender/issues"><img src="https://img.shields.io/github/issues/Dalibor-P/blender?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/Dalibor-P/blender/contributors"><img src="https://img.shields.io/github/contributors/Dalibor-P/blender?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
    <img src="assets/catwalk.webp"/>
</p>

## 📷 Previews and accents

<details>
<summary>🌻 Latte</summary>
<img src="assets/latte_preview.png"/>
&nbsp;
<img src="assets/accents latte.svg"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="assets/frappe_preview.png"/>
&nbsp;
<img src="assets/accents frappe.svg"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="assets/macchiato_preview.png"/>
&nbsp;
<img src="assets/accents macchiato.svg"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="assets/mocha_preview.png"/>
&nbsp;
<img src="assets/accents mocha.svg"/>
</details>

## ⬇️ Usage

1. Head over to the [latest release](https://github.com/Dalibor-P/blender/releases/latest) and download your selected accented flavour.
2. Open Blender's settings and theme installation dialogue: `Edit → Preferences → Themes → Install`.
3. Browse to where you downloaded the theme and install the `.xml` file.
4. This copies the theme into `./scripts/presets/interface_theme/` subdirectory of your Blender [configuration directory](https://docs.blender.org/manual/en/latest/advanced/blender_directory_layout.html). You may now select it from the drop down menu.

Made for Blender 3.5+. You can try my add-on [Theme Swapper](https://github.com/Dalibor-P/Theme-Swapper) to quickly swap between light and dark themes.

## ❓ FAQ

**Q: Custom Panel/Box/Button roundness? Custom accent colour?**

A: Clone or download the repository locally. If you don't have python, open your desired flavour master files in any text editor (for example `accent generator/latte_master.xml`). Find and replace following text:

1. `roundness="0.8"` replace for your desired element roundness. For example, `roundness="0.4"` is Blender Dark default.
2. `#bada55` replace for your custom accent colour, that will show on many UI elements. For example `#ad75f5` is light mauve.
3. `#bada66` replace for your custom secondary accent colour, that will show when selecting multiple objects. For example `#563a7a` is dark mauve.

If you have python, run `accent generator/accent generator.py` with arguments of your choice. All files in `themes/` will be regenerated for all four flavours. You need colorutils installed (`pip install colorutils`). Examples:

* `python 'accent generator.py' '0.4' 'All'` will generate all default accents with roundness of 0.4 which is Blender Dark default roundness.
* `python 'accent generator.py' '#E64553' '1'` will generate only custom maroon accent with maximum roundness.
* `python 'accent generator.py' 'all' '0.1' '#ff0000'` will generate all default accents as well as a custom red accent, all with roundness of 0.1.

**Q: I have contrast issues with accent X!**

A: Raise an issue and propose an alternative accent colour.

**Q: Well, you see, I think that ...**

A: Others have made Catppuccin themes for Blender as well. You might like their versions too:

* [Catppuccin by Ameknite](https://github.com/ameknite/blender) is a well done dark theme inspired by Blenders default dark theme.
* [Catppuccin by codekisser](https://github.com/codekisser/blender) is another well done dark theme.
* [Catppuccin by nekowinston](https://github.com/nekowinston/ctp-blender) appears to be build on an older version of Catppuccin, and no longer maintained.

[Catppuccin team](https://github.com/catppuccin) has not yet selected one particular implementation as official.

## 👐 Contributing

* Report any inconsistencies, flaws, mistakes or contrast issues you can find.
* Propose alternative accent colours for better contrast between foreground and background elements.

## 💝 Thanks to

- [Dalibor-P](https://github.com/Dalibor-P)
- [Ameknite](https://github.com/ameknite)

&nbsp;

<p align="center">
    <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
    Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
    <a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
