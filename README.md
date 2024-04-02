**Please note**: Use [this link](https://git.hs-mittweida.de/hsmw-latex/hsmw-latex/-/tree/oldstyle) to acquire the old templates (that you may want to use and can not find) as long as there are no new ones.

---

# LaTeX Templates

This repository offers all available official LaTeX templates aggregated in one place (e.g. for your local TEXMF directory).
If you are just looking for a specific template (e.g. hsmw-beamer), you can use the respective standalone repository.

There are currently multiple subversions of official and inofficial templates around for the previous and current corporate design specifications of the university.
The previous specifications emerged in 2009 (\"CD09\") and are referred to by now as \"deprecated\" or \"old\".
The current specifications were introduced in 2019 (\"CD19\") and are still under active development, thus changes may be introduced.
Further information can be found on the [official corporate design website](https://zip.hs-mittweida.de/intranet/corporate_design.php).

## Available Templates and Current State of Implementation

| Template Name | Official Status | Template Status | | Primary Audience | Remarks |
| - | - | - | - | - | - |
| [hsmw-beamer](https://git.hs-mittweida.de/hsmw-latex/hsmw-beamer) | CD19 | CD19 | &#x2714;&#xFE0F; | student, researcher, lecturer, administration | beamer presentation |
| hsmw-card | CD19 | [deprecated](https://git.hs-mittweida.de/hsmw-latex/hsmw-latex/-/tree/oldstyle)<sup>1</sup> | &#x2755; | lecturer, administration | business card |
| hsmw-flyer | CD19 | [deprecated](https://git.hs-mittweida.de/hsmw-latex/hsmw-latex/-/tree/oldstyle)<sup>1</sup> | &#x2755; | administration | informative flyer, 	leaflet |
| hsmw-letter | CD19  | [deprecated](https://git.hs-mittweida.de/hsmw-latex/hsmw-latex/-/tree/oldstyle)<sup>1</sup> | &#x2755; | lecturer, administration | official letter |
| hsmw-poster | CD19 | [deprecated](https://git.hs-mittweida.de/hsmw-latex/hsmw-latex/-/tree/oldstyle)<sup>1</sup> | &#x2755; | researcher | scientific poster |
| hsmw-quicktalk | nonexistent | [deprecated](https://git.hs-mittweida.de/hsmw-latex/hsmw-latex/-/tree/oldstyle)<sup>1</sup> | &#x2755; | lecturer, administration | presentation of existing text document |
| hsmw-report | CD19 | nonexistent | &#x274C; | researcher, administration | project report |
| [hsmw-thesis](https://git.hs-mittweida.de/hsmw-latex/hsmw-thesis) | deprecated (!) | CD19 | &#x2714;&#xFE0F; | student | term paper, thesis |
| hsmw-worksheet | nonexistent | [deprecated](https://git.hs-mittweida.de/hsmw-latex/hsmw-latex/-/tree/oldstyle)<sup>1</sup> | &#x2755; | lecturer | worksheet with solutions |

<sup>1</sup>As long as no new LaTeX template is available, the use of the previous template is recommended.
You can access the old styles provided by Prof. Dohmen by using the [branch \"oldstyle\"](https://git.hs-mittweida.de/hsmw-latex/hsmw-latex/-/tree/oldstyle) of this repository.

## Get All the Templates

This repository uses submodules and therefore needs a slightly adjusted command syntax for cloning:
```sh
git clone --recursive git@git.hs-mittweida.de:hsmw-latex/hsmw-latex.git
# or
git clone --recursive https://git.hs-mittweida.de/hsmw-latex/hsmw-latex.git
```

Alternatively you can clone the repository the usual way and need to retrieve the submodules afterwards:
```sh
git clone git@git.hs-mittweida.de:hsmw-latex/hsmw-latex.git
# or
git clone https://git.hs-mittweida.de/hsmw-latex/hsmw-latex.git
# followed by
git submodule update --init --recursive
```

If you just want to to update your already existing repository to the latest version:
```sh
git pull --recurse-submodules
```

Note: You can retrieve individual repositories (e.g. hsmw-beamer) the usual way.

## User Groups

You may want to join the discussion group *HSMW-LaTeX* on Telegram:
[t.me/joinchat/Bxm0glfyeKXTM9OVlAhzJw](https://t.me/joinchat/Bxm0glfyeKXTM9OVlAhzJw)

Alternatively you can always ask for help on Discord:
[HSMW Community Discord](https://discord.com/channels/750860384126369822/765215969424834600)
