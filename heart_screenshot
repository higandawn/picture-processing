# -*- coding: utf-8 -*-
"""
:Project_name   DataDispose
:File           ima.py
:Create_date		20/02/15 1:59
:Environment		PyCharm | python3.7.2
:Licence 　　　　GPL
:Author         higandown@qq.coom
:Description    心之器截图
"""
from PIL import Image
import os

# 图片裁剪位置参数
START_X = 192
START_Y = 92
END_X = 428
END_Y = 510

IMAGE_SIZE = START_X*2, START_Y*2, END_X*2, END_Y*2

IMAGE_OLD_PATH = r'D:\image\old\\'
IMAGE_NEW_PATH = r'D:\image\new\\'

def cut(path, scale=1):
	""" 图片裁剪
	:param path:  文件名
	:param scale: 图片缩放
	:return:
	"""
	old_file_path = os.path.join(IMAGE_OLD_PATH, path) #旧文件路径
	new_file_path = os.path.join(IMAGE_NEW_PATH, path) #新文件路径

	with Image.open(old_file_path) as im: #打开图片
		im2 = im.crop(IMAGE_SIZE) #裁剪图片
		w, h = int(im2.size[0]*scale), int(im2.size[1]*scale)
		im3 = im2.resize((w, h), Image.ANTIALIAS) # 缩小图片
		im3.save(new_file_path) #保存图片

def main():
	lists = os.listdir(IMAGE_OLD_PATH) #获取图片名字

	for i in lists:
		cut(i, 0.5)


if __name__ == '__main__':
	main()
