# -*- coding: utf-8 -*-
"""
:Project_name 		DataDispose
:File               im.py
:Create_date		20/02/14 10:32
:Environment		PyCharm | python3.7.2
:Licence            GPL
:Author             higandown@qq.coom
:Description        游戏图片裁剪-合并
"""
from PIL import Image
import os, shutil

# 大小定位(1像素=2单位)
IMAGE_OLD_PATH = r'D:\image\old\\'  	#旧路径
IMAGE_NEW_PATH = r'D:\image\new\\'		#截图路径
IMAGE_SIZE_PATH= r'D:\image\size\\'	#合并路径

IMAGE_COL = 3 # 图片间隔，也就是合并成一张图后，一共有几行 ↓
IMAGE_ROW = 2 # 图片间隔，也就是合并成一张图后，一共有几列 →
IMAGE_SIZE= (974, 738) # 每张小图片的大小

FRONT = (199, 58, 1170, 794)	#截图大小1
QUEEN = (972, 242, 1947, 980)	#截图大小2
# rectangular = start_x, start_y, end_x, end_y

def empty_file(file_path):
	shutil.rmtree(file_path)
	os.mkdir(file_path)

def cut(path, rectangular):
	# 图片裁剪
	old_file_path = os.path.join(IMAGE_OLD_PATH, path) #旧文件路径
	new_file_path = os.path.join(IMAGE_NEW_PATH, path) #新文件路径

	with Image.open(old_file_path) as im: #打开图片
		im2 = im.crop(rectangular) #裁剪图片
		im2.save(new_file_path) #保存图片

def image_compose(name):
	image_save_path = IMAGE_SIZE_PATH + str(name) + '.jpg'  # 图片转换后的地址
	image_names = [name for name in os.listdir(IMAGE_NEW_PATH)]
	to_image = Image.new('RGB', (IMAGE_ROW * IMAGE_SIZE[0], IMAGE_COL * IMAGE_SIZE[1]))

	for c in range(1, IMAGE_COL+1): # 列
		for r in range(1, IMAGE_ROW+1): # 行
			from_image = Image.open(IMAGE_NEW_PATH + image_names[IMAGE_ROW * (c - 1) + r - 1]).resize(
				(IMAGE_SIZE[0], IMAGE_SIZE[1]), Image.ANTIALIAS)
			to_image.paste(from_image, ((r - 1) * IMAGE_SIZE[0], (c - 1) * IMAGE_SIZE[1]))
	return to_image.save(image_save_path)

def cut_merge(name, lists):
	# 裁剪后合并
	for i, file in enumerate(lists):
		if i == 0:
			cut(file, FRONT)
		else:
			cut(file, QUEEN)
	image_compose(name)
	empty_file(IMAGE_NEW_PATH)

def main():
	a = 0
	lists = []

	for i, j in enumerate(os.listdir(IMAGE_OLD_PATH), 1):
		lists.append(j)
		if i % 6 == 0:
			cut_merge(a, lists)
			lists.clear()
			a += 1
			print(a)

if __name__ == '__main__':
	main()
