"""
Port of Ren'Py's launcher gui7 generator (MIT, Tom Rothamel) to Pillow, so a
project can be created without the Ren'Py launcher. Writes gui.rpy,
screens.rpy, options.rpy and the gui/*.png images into <target>/game.

It also makes the bar, slider, scrollbar, check/radio and save-slot images
that the launcher would make with gui._gui_images() (00gui.rpy).

Usage: python3 tools/make_gui.py <renpy-source-checkout> <project-dir>

The Ren'Py source is https://github.com/renpy/renpy (only gui/ and
launcher/game/gui7/ are needed). It overwrites gui.rpy, screens.rpy and
options.rpy, so re-apply local edits to options.rpy afterwards.
"""

import colorsys
import math
import os
import re
import shutil
import sys
import time

from PIL import Image

SRC, TARGET = sys.argv[1], sys.argv[2]
NAME = "Shadows & Silk"
SIMPLE_NAME = "ShadowsAndSilk"
WIDTH, HEIGHT = 1920, 1080
ACCENT = "#b07cc6"
BORING = "#0a0610"

SCALE = min(WIDTH / 1280, HEIGHT / 720)
GAME = os.path.join(TARGET, "game")
GUI = os.path.join(GAME, "gui")


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(c):
    return "#{:02x}{:02x}{:02x}".format(*(max(0, min(255, int(round(v)))) for v in c))


def tint(c, n):
    return tuple(n * v + (1 - n) * 255 for v in c)


def shade(c, n):
    return tuple(n * v for v in c)


def hsv_replace(c, s=None, v=None):
    h, s0, v0 = colorsys.rgb_to_hsv(*(x / 255 for x in c))
    r, g, b = colorsys.hsv_to_rgb(h, s0 if s is None else s, v0 if v is None else v)
    return (r * 255, g * 255, b * 255)


accent = hex_to_rgb(ACCENT)
boring = hex_to_rgb(BORING)

# Dark theme, as in gui7/parameters.py.
colors = {
    "accent": accent,
    "hover": tint(accent, .6),
    "muted": shade(accent, .4),
    "hover_muted": shade(accent, .6),
    "menu": hsv_replace(accent, s=.25, v=.25),
    "title": hsv_replace(accent, s=.5, v=1.0),
    "selected": hex_to_rgb("#ffffff"),
    "idle": hex_to_rgb("#888888"),
    "idle_small": hex_to_rgb("#aaaaaa"),
    "text": hex_to_rgb("#ffffff"),
}


def rgba(c, opacity=1.0):
    return tuple(int(round(v)) for v in c) + (int(255 * opacity),)


# ---------------------------------------------------------------- images ---

def save(img, name):
    fn = os.path.join(GUI, name + ".png")
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    img.save(fn, optimize=True)


def generate_line(template):
    template = list(template)
    size = int(max(i[0] for i in template))
    rv = []
    right_pos, right_value = template[0]
    left_pos, left_value = right_pos, right_value
    for i in range(size):
        if i == right_pos:
            rv.append(right_value)
            continue
        while i >= right_pos:
            left_pos, left_value = right_pos, right_value
            right_pos, right_value = template.pop(0)
        done = (i - left_pos) / (right_pos - left_pos)
        rv.append(left_value + done * (right_value - left_value))
    return rv


def crop_line(line, size):
    if len(line) <= size:
        return line
    start = (len(line) - size) // 2
    return line[start:start + size]


def generate_image(name, xtmpl, ytmpl, color):
    r, g, b, a = color
    xline = crop_line(generate_line([(p * SCALE, o) for p, o in xtmpl]), WIDTH)
    yline = crop_line(generate_line([(p * SCALE, o) for p, o in ytmpl]), HEIGHT)
    img = Image.new("RGBA", (len(xline), len(yline)))
    px = img.load()
    for x, xv in enumerate(xline):
        for y, yv in enumerate(yline):
            px[x, y] = (r, g, b, int(a * xv * yv))
    save(img, name)


def scale_int(n):
    return max(1, int(n * SCALE))


def blank(w, h):
    return Image.new("RGBA", (w, h))


def fill(img, rect, color):
    x, y, w, h = rect
    img.paste(Image.new("RGBA", (w, h), color), (x, y))


def generate_images():
    full_w, full_h = WIDTH / SCALE, HEIGHT / SCALE

    # Textbox.
    inside = (full_w - 744) // 2
    generate_image("textbox", [(0, 0), (inside, 1), (full_w - inside, 1), (full_w, 0)],
                   [(0, 0), (5, 1), (185, 1)], rgba(boring, .8))
    generate_image("phone/textbox", [(0, 1), (full_w, 1)], [(0, 0), (5, 1), (240, 1)], rgba(boring, .8))
    save(blank(scale_int(300), scale_int(36)), "namebox")

    # Choice buttons.
    X = [(0, 0), (100, 1), (690, 1), (790, 0)]
    Y = [(0, 0), (3, 1), (32, 1), (35, 0)]
    for prefix in ("", "phone/"):
        generate_image(prefix + "button/choice_idle_background", X, Y, rgba(boring, .8))
        generate_image(prefix + "button/choice_hover_background", X, Y, rgba(accent, .95))

    # Overlays.
    width, phone_width = scale_int(280), scale_int(340)
    game_y, game_h, line = scale_int(120), scale_int(570), scale_int(3)
    for prefix, w in (("", width), ("phone/", phone_width)):
        mm = blank(WIDTH, HEIGHT)
        fill(mm, (0, 0, w, HEIGHT), rgba(boring, .8))
        fill(mm, (w - line, 0, line, HEIGHT), rgba(accent))
        save(mm, prefix + "overlay/main_menu")

        gm = Image.new("RGBA", (WIDTH, HEIGHT), rgba(boring, .8))
        fill(gm, (w - line, game_y, line, game_h), rgba(accent))
        save(gm, prefix + "overlay/game_menu")
    save(Image.new("RGBA", (WIDTH, HEIGHT), rgba(boring, .6)), "overlay/confirm")

    # Frame.
    w, h, border = scale_int(600), scale_int(250), scale_int(3)
    fr = Image.new("RGBA", (w, h), rgba(accent))
    fill(fr, (border, border, w - 2 * border, h - 2 * border), rgba(boring))
    save(fr, "frame")

    # NVL.
    inside = (full_w - 800) // 2
    generate_image("nvl", [(0, 0), (inside, 1), (full_w - inside, 1), (full_w, 0)],
                   [(0, 1), (full_h, 1)], rgba(boring, .8))
    generate_image("phone/nvl", [(0, 1), (full_w, 1)], [(0, 1), (full_h, 1)], rgba(boring, .8))

    # Quick menu buttons.
    q = blank(scale_int(100), scale_int(30))
    save(q, "button/quick_idle_background")
    save(q, "button/quick_hover_background")

    # Skip and notify.
    generate_image("skip", [(0, 1), (190, 1), (240, 0)], [(0, 1), (43, 1)], rgba(boring, .8))
    generate_image("notify", [(0, 1), (872, 1), (922, 0)], [(0, 1), (43, 1)], rgba(boring, .8))

    # Menu backgrounds, replaced later by key art.
    menu = Image.new("RGBA", (WIDTH, HEIGHT), rgba(colors["menu"]))
    save(menu, "main_menu")
    save(menu, "game_menu")

    # Window icon, tinted towards the accent colour.
    icon = Image.open(os.path.join(SRC, "launcher/game/gui7/icon.png")).convert("RGBA")
    ro, go, bo = (v - 23 for v in accent)
    px = icon.load()
    for y in range(icon.height):
        for x in range(icon.width):
            r, g, b, a = px[x, y]
            px[x, y] = (max(0, min(r + ro, 255)), max(0, min(g + go, 255)),
                        max(0, min(b + bo, 255)), a)
    save(icon, "window_icon")

    for fn in ("bubble.png", "thoughtbubble.png"):
        shutil.copyfile(os.path.join(SRC, "gui/game/gui", fn), os.path.join(GUI, fn))


def generate_widgets(phone):
    """
    Port of gui._gui_images() from renpy/common/00gui.rpy, which the launcher
    runs once when it creates a project. Sizes match the defines in gui.rpy.
    """

    prefix = "phone/" if phone else ""
    factor = HEIGHT / 720

    def scaled(n):
        return int(n * factor)

    def solid(w, h, color=None):
        return Image.new("RGBA", (w, h), rgba(color) if color else (0, 0, 0, 0))

    # Buttons. gui.check_button_borders = gui.radio_button_borders = Borders(27, 6, 6, 6)
    width = scaled(300)
    height = scaled(43 if phone else 33)
    toggle_width, margin = 27, scaled(3)
    toggle_rect = (margin, 6, min(toggle_width - margin, scaled(5)), height - 12)

    save(solid(width, height), prefix + "button/idle_background")
    save(solid(width, height), prefix + "button/hover_background")

    for kind in ("check", "radio"):
        selected = solid(toggle_width, height)
        fill(selected, toggle_rect, rgba(accent))
        save(selected, prefix + "button/{}_selected_foreground".format(kind))
        save(solid(toggle_width, height), prefix + "button/{}_foreground".format(kind))

    # Bars. gui.bar_size = 38, gui.slider_size = 38 (54 on phones), gui.scrollbar_size = 18
    long_size = scaled(350)
    bar_size, slider_size, scrollbar_size = 38, 54 if phone else 38, 18
    thumb_size = scaled(15 if phone else 10)

    save(solid(long_size, bar_size, colors["hover"]), prefix + "bar/left")
    save(solid(long_size, bar_size, colors["muted"]), prefix + "bar/right")
    save(solid(bar_size, long_size, colors["hover"]), prefix + "bar/bottom")
    save(solid(bar_size, long_size, colors["muted"]), prefix + "bar/top")

    def bar_set(kind, size, long_size, thumb_size):
        for state, bar, thumb in (("idle", "muted", "accent"), ("hover", "hover_muted", "hover")):
            save(solid(long_size, size, colors[bar]), "{}{}/horizontal_{}_bar".format(prefix, kind, state))
            save(solid(thumb_size, size, colors[thumb]), "{}{}/horizontal_{}_thumb".format(prefix, kind, state))
            save(solid(size, long_size, colors[bar]), "{}{}/vertical_{}_bar".format(prefix, kind, state))
            save(solid(size, thumb_size, colors[thumb]), "{}{}/vertical_{}_thumb".format(prefix, kind, state))

    bar_set("slider", slider_size, long_size, thumb_size)
    bar_set("scrollbar", scrollbar_size, scaled(700), scaled(700))

    # Save slots. gui.slot_button_* and config.thumbnail_* in gui.rpy.
    slot_w, slot_h, slot_pad = 414, 309, 15
    thumb_w, thumb_h = 384, 216
    tnx = (slot_w - thumb_w) // 2

    idle = solid(slot_w, slot_h)
    fill(idle, (tnx, slot_pad, thumb_w, thumb_h), rgba(colors["muted"]))
    save(idle, prefix + "button/slot_idle_background")

    hover = solid(slot_w, slot_h)
    fill(hover, (tnx, slot_pad, thumb_w, thumb_h), rgba(colors["hover_muted"]))
    fill(hover, (0, slot_pad, scaled(5), thumb_h), rgba(accent))
    save(hover, prefix + "button/slot_hover_background")


# ------------------------------------------------------------------ code ---

def load(fn):
    with open(os.path.join(SRC, "gui/game", fn), encoding="utf-8") as f:
        return [l.rstrip().replace("﻿", "") for l in f]


def write(fn, lines):
    with open(os.path.join(GAME, fn), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def remove_scale(lines):
    sub = lambda m: str(int(math.ceil(int(m.group(1)) * SCALE)))
    return [re.sub(r"gui.scale\((.*?)\)", sub, l) for l in lines]


def update_defines(lines, replacements):
    rv = []
    for l in lines:
        m = re.match(r"^(\s*)define (.*?) =", l)
        if m and m.group(2) in replacements:
            l = "{}define {} = {}".format(m.group(1), m.group(2), replacements[m.group(2)])
        rv.append(l)
    return rv


def generate_code():
    h = {k: repr(rgb_to_hex(v)) for k, v in colors.items()}
    insensitive = repr(rgb_to_hex(colors["idle"]) + "7f")

    gui = remove_scale(load("gui.rpy"))
    gui = [re.sub(r"gui.init\(.*?\)", "gui.init({}, {})".format(WIDTH, HEIGHT), l) for l in gui]
    gui = update_defines(gui, {
        "gui.accent_color": h["accent"],
        "gui.selected_color": h["selected"],
        "gui.hover_color": h["hover"],
        "gui.muted_color": h["muted"],
        "gui.hover_muted_color": h["hover_muted"],
        "gui.title_color": h["title"],
        "gui.idle_color": h["idle"],
        "gui.idle_small_color": h["idle_small"],
        "gui.insensitive_color": insensitive,
        "gui.text_color": h["text"],
        "gui.interface_text_color": h["text"],
        "gui.choice_button_text_idle_color": h["idle"],
        "gui.choice_button_text_insensitive_color": insensitive,
    })
    write("gui.rpy", gui)

    write("screens.rpy", remove_scale(load("screens.rpy")))

    options = update_defines(load("options.rpy"), {
        "config.name": '_("{}")'.format(NAME),
        "build.name": '"{}"'.format(SIMPLE_NAME),
        "config.save_directory": '"{}-{}"'.format(SIMPLE_NAME, int(time.time())),
    })
    write("options.rpy", options)

    if not os.path.exists(os.path.join(TARGET, ".gitignore")):
        shutil.copyfile(os.path.join(SRC, "gui/gitignore.txt"), os.path.join(TARGET, ".gitignore"))
    for dn in ("images", "audio", "libs"):
        os.makedirs(os.path.join(GAME, dn), exist_ok=True)


os.makedirs(GUI, exist_ok=True)
generate_images()
generate_widgets(phone=False)
generate_widgets(phone=True)
generate_code()
print("done", SCALE, {k: rgb_to_hex(v) for k, v in colors.items()})
