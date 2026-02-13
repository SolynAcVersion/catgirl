# rnekod
A cli catgirl random picture crawler for arch linux

**R**andom **neok** **d**ownloader

rnekod is a lightweight command-line tool that fetches random catgirl (anime-style cat girl) images from NekosAPI v4 and displays them directly in your default image viewer, browser, or saves them to disk.

## Installation

From AUR (Arch Linux / Arch-based)
If you use an Arch-based distribution, you can install rnekod directly from the AUR using an AUR helper like yay or paru:

```bash
yay -S rnekod
```

or

```bash
paru -S rnekod
```

## Manual installation

```bash
git clone https://github.com/SolynAcVersion/catgirl.git
cd catgirl
makepkg -si
```

## Dependencies

Python ≥ 3.10 (Actually 3.14 for this project)

requests

Pillow (for image display)

colorama (for colored terminal output)


## Usage

```bash
rnekod [-h] [-br] [-dp DOWNLOAD_PATH] [-r RATING] [-v]
```

#### Args

-h	--help	Show help message and exit.
-br	--browser	Open the fetched image in your default web browser instead of displaying it with the system image viewer.
-dp	--download-path	Download the image to the specified directory. The directory must exist. The file will be named nekoget_<image_id>.png.
-r	--rating	Filter images by rating(s). Provide a comma-separated list of ratings. Allowed values: safe, suggestive, borderline, explicit. You can also use aliases (see below). Default: safe,suggestive.
-v	--version	Show the program version and exit.

#### Few shortcuts for rating

- `safe`	safe, 12-, sfw, s
- `suggestive`	suggestive, 16-, S
- `borderline`	borderline, 18-, b
- `explicit`	explicit, r18, 18+, nsfw, src

Use `,` to combine ranges of rating


## Acknowledgements

- NekosAPI for providing the wonderful catgirl images.
- Claude Code for assistance in development.
- [jer4q/nekoget](https://github.com/jer4q/nekoget) for inspiration

