from PIL import Image

def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
    min_height = min(im.height for im in im_list)
    im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height),resample=resample)
                      for im in im_list]
    total_width = sum(im.width for im in im_list_resize)
    dst = Image.new('RGB', (total_width, min_height))
    pos_x = 0
    for im in im_list_resize:
        dst.paste(im, (pos_x, 0))
        pos_x += im.width
    return dst

def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
    min_width = min(im.width for im in im_list)
    im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)),resample=resample)
                      for im in im_list]
    total_height = sum(im.height for im in im_list_resize)
    dst = Image.new('RGB', (min_width, total_height))
    pos_y = 0
    for im in im_list_resize:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst

hoge = input("type the name of the directory: ")

rotate = input('rotate (y/other): ') == 'y'

number_of_rows = int(input("number_of_rows: "))

if rotate:
    number_of_columns = 4
else:
    number_of_columns = int(input("number_of_columns: "))

matrix = [[] for i in range(number_of_rows)]

for i in range(number_of_rows):
    for j in range(number_of_columns):
        try:
            if rotate:
                matrix[i].append(Image.open('./tiles/' + hoge + '/' + str(i) + '.png').rotate(90*j))
            else:
                matrix[i].append(Image.open('./tiles/' + hoge + '/' + str(i*number_of_columns + j) + '.png'))
        except:
            matrix[i].append(Image.open('./empty.png'))

image = get_concat_v_multi_resize([get_concat_h_multi_resize(matrix[i]) for i in range(number_of_rows)]).convert('RGBA')

transparent = input('transparent? (y/other): ') == 'y'

newImage = []
for item in image.getdata():
    if item[:3] == (0, 0, 0) and transparent:
        newImage.append((0, 0, 0, 0))
    else:
        newImage.append(item)

image.putdata(newImage)

image.save('./tiles/' + hoge + '/' + hoge +'.png')
