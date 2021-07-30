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

vowels = ['A', 'I', 'U', 'E', 'O']

consonants = ['', 'K', 'S', 'T', 'N', 'H', 'M', 'Y', 'R', 'W']

matrix = [[] for i in range(10)]

for i in range(10):
    for j in range(5):
        try:
            if i == 9 and j == 2:
                matrix[i].append(Image.open('./tiles/KATAKANA/WO_KATAKANA.png'))
            elif i == 9 and j == 4:
                matrix[i].append(Image.open('./tiles/KATAKANA/N_KATAKANA.png'))
            else:
                matrix[i].append(Image.open('./tiles/KATAKANA/' + consonants[i] + vowels[j] + '_KATAKANA.png'))
        except:
            matrix[i].append(Image.open('./empty.png'))

image = get_concat_v_multi_resize([get_concat_h_multi_resize(matrix[i]) for i in range(10)]).convert('RGBA')

newImage = []
for item in image.getdata():
    if item[:3] == (0, 0, 0):
        newImage.append((0, 0, 0, 0))
    else:
        newImage.append(item)

image.putdata(newImage)

image.save('./tiles/KATAKANA/KATAKANA.png')
