from PIL import Image


def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def proper_position(arriving_file, file_to_save, **colors):
    im = Image.open(arriving_file)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            for color in colors:
                if pixels[i, j] == hex_to_rgb(color):
                    pixels[i, j] = hex_to_rgb(colors[color])

    im = im.rotate(-90, expand=True)
    im.save(file_to_save)


colors = {
    "#8adf2e": "#baddf4",
    "#3f48cc": "#7610b3",
    "#a953db": "#f0a4d4",
    "#b83dba": "#d74a66"
}
proper_position("wheeler.png", "alien.png", **colors)
