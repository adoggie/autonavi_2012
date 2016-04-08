#!/usr/bin/env python
#coding=utf-8
from __future__ import division

def mesh2coord(mesh):
	mesh_coord = {}
	
	diff_lat = 5/60				# 1：2.5万纬差
	diff_lon = 7/60+30/3600		# 1：2.5万经差

	# 西南图廓坐标公式
	# x = (b - 31) * 6 + (d - 1) * diff_long
	# y = (a - 1) * 4 + (4 / diff_lat - c) * diff_lat

	if len(mesh) != 10:
		return -1
	try:
		a = ord(mesh[0]) - 65 + 1
		b = int(mesh[1:3])
		c = int(mesh[4:7])
		d = int(mesh[-3:])
	except (ValueError,TypeError):
		return -1
		
	southwest_x = (b - 31) * 6 + (d - 1) * diff_lon
	southwest_y = (a - 1) * 4 + (4 / diff_lat - c) * diff_lat

	northeast_x = southwest_x + diff_lon
	northeast_y = southwest_y + diff_lat
	
	mesh_coord['x'] = southwest_x
	mesh_coord['y'] = southwest_y
	# mesh_coord['northeast'] = "%s,%s" %(northeast_x,northeast_y)

	mesh_coord['height'] = diff_lat	
	mesh_coord['width'] = diff_lon

	
	return mesh_coord


if __name__ == '__main__':
	
	a = 'H51F009013'
	coord = mesh2coord(a)
	
	print coord
	
	
	
	
	
	
	
	
	