# coding: utf8
import os
import shutil
from PIL import Image


# python icon.py
def generate():
    iPath = input("请输入原始icon路径")
    strSizes = input("请输入需要重新调整的尺寸，多个用英文,号隔开 例如 20,512,1024 \nps:调整的icon尺寸必须为正方形\n")
    listSize = strSizes.split(',')
    icon = Image.open(iPath)
    sizes = []
    for i in listSize:
        sizes.append(('Icon-' + i + ".png", int(i)))
    if os.path.exists('out'):
        shutil.rmtree('out')
    os.makedirs('out')
    for s in sizes:
        name, size = s
        img = icon.resize((size, size), Image.NEAREST)
        oPath = 'out/' + name
        img.save(oPath, icon.format)
        print('输出到' + oPath)


generate()
