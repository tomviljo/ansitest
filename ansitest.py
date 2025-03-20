
def sgr(*attributes):
    '''Select Graphic Rendition'''
    return '\x1b[' + ';'.join(str(a) for a in attributes) + 'm'

def styled(text, *attributes):
    '''Decorate the text with ANSI codes'''
    return sgr(*attributes) + text + sgr(0)

def contrast(color):
    '''Return white or black, depending on the given color'''
    if color < 7:
        return 15
    elif color < 16:
        return 0
    elif color < 232:
        if (color - 16) % 36 < 18:
            return 15
        else:
            return 0
    elif color < 244:
        return 15
    else:
        return 0

def test_attributes():
    styles = [
        ['Bold', 1],
        ['Faint', 2],
        ['Italic', 3],
        ['Underline', 4],
        ['Slow blink', 5],
        ['Rapid blink', 6],
        ['', 0], # Do not put Underline right above Reverse
        ['Reverse', 7],
        ['Conceal', 8],
        ['Crossed-out', 9],
        ['Primary font', 10],
        ['Alternative font 1', 11],
        ['Alternative font 2', 12],
        ['Alternative font 3', 13],
        ['Alternative font 4', 14],
        ['Alternative font 5', 15],
        ['Alternative font 6', 16],
        ['Alternative font 7', 17],
        ['Alternative font 8', 18],
        ['Alternative font 9', 19],
        ['Gothic', 20],
        ['Doubly underlined', 21],
        ['Framed', 51],
        ['Encircled', 52],
        ['Overlined', 53],
        ['Set underline color', 58, 5, 1, 4],
        ['Ideogram underline', 60],
        ['Ideogram double underline', 61],
        ['Ideogram overline', 62],
        ['Ideogram double overline', 63],
        ['Ideogram stress marking', 64],
        ['Superscript', 73],
        ['Subscript', 74]
    ]
    for offset in range(0, len(styles), 3):
        cells = []
        for i in range(offset, min(offset + 3, len(styles))):
            cells.append(styled('%-32s' % (styles[i][0],), *styles[i][1:]))
        print(''.join(cells))

def test_xterm_colors(print_row):
    print_row(0, 8, 12)
    print_row(8, 16, 12)
    for block in range(3):
        for row in range(6):
            start = 16 + 12 * block + 36 * row
            print_row(start, start + 12, 8)
    print_row(232, 244, 8)
    print_row(244, 256, 8)

def test_xterm_colors_fg():
    def box(fg, width):
        return styled(' ' * (width - 4) + '%3d ' % (fg,), 38, 5, fg)
    def print_row(start, stop, width):
        print(''.join(box(color, width) for color in range(start, stop)))

    test_xterm_colors(print_row)

def test_xterm_colors_bg_spacing():
    def box(fg, bg, width):
        return styled(' ' * (width - 5) + '%3d ' % (bg,), 38, 5, fg, 48, 5, bg)
    def print_row(start, stop, width):
        print(' '.join(box(contrast(color), color, width) for color in range(start, stop)))
        print()

    test_xterm_colors(print_row)

def test_xterm_colors_bg():
    def box(fg, bg, width):
        return styled(' ' * (width - 4) + '%3d ' % (bg,), 38, 5, fg, 48, 5, bg)
    def print_row(start, stop, width):
        print(''.join(box(contrast(color), color, width) for color in range(start, stop)))

    test_xterm_colors(print_row)

def test_rgb_colors():
    for r in range(0, 256, 16):
        print(''.join(styled(' ', 48, 2, r, g, b) for b in [0, 100, 200] for g in range(0, 256, 8)))

def main():
    print()
    print('Attributes')
    print()
    test_attributes()
    print()
    print('XTerm colors, foreground')
    print()
    test_xterm_colors_fg()
    print()
    print('XTerm colors, background, with spacing')
    print()
    test_xterm_colors_bg_spacing()
    print()
    print('XTerm colors, background')
    print()
    test_xterm_colors_bg()
    print()
    print('RGB colors')
    print()
    test_rgb_colors()

if __name__ == '__main__':
    main()
