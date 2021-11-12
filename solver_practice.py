#!/bin/env python3

from wand.image import Image

def main(img_path):
    img = Image(filename=img_path)
    print(f"Dimensions of '{img_path}':", img.width, 'x', img.height)

if __name__ == '__main__':
    main('assets/complex_maze_us6.png')
    print('Done.')
