# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./Arial.ttf', 24)

def add_text_to_img(image, text, font=font):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    text_size_x, text_size_y = image_draw.textsize(text, font=font)

    print(text_size_x, text_size_y)
    # return 0

    print(rgba_image)
    text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)

    image_draw.text((rgba_image.size[0] - text_size_x, 0), text, font=font, fill=(76, 234, 124, 180))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text

im_before = Image.open("test.png")
# im_before.show()
im_after = add_text_to_img(im_before, '5')
im_after.show()
# im.save('im_after.png')