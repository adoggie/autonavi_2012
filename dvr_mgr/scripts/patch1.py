﻿# -*- coding:utf-8 -*-#patch1  #修复经纬度颠倒问题import sys,os,os.path,time,struct,traceback,threading,datetimecvtcmd='''avi2wmv\\ffmpeg.exe -r 15 -i %s -b 3000k -r 15  %s'''clips_dir='20111201'clips_dest='trp_new'files = os.listdir(clips_dir)for file in files:	name,ext = os.path.splitext(file)	if ext.lower() == '.trp':		#check wmv is existed?		ff = open("%s/%s"%(clips_dir,file),'r')		lines = ff.readlines()		ff.close()		ff = open("%s/%s"%(clips_dest,file),'w')		for line in lines:			pp = line.strip().split(',')			k = "%s,%s,%s\n"%(pp[1],pp[0],pp[2])			ff.write(k)		ff.close()		