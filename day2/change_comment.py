#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys

if '-r' in sys.argv:
	rep_argv_pos = sys.argv.index('-r')
	find_str = sys.argv[rep_argv_pos+1]
	new_str = sys.argv[rep_argv_pos+2]

f = open('passwd','r+')

for line in f:
	if line == '':
		break
	else:
		print '--> ',f.tell()
		if find_str in line:
			print '-->cur pos: ',f.tell(),len(line)
			last_pos = f.tell() - len(line)
			f.seek(last_pos)
			print '-->last_pos: ',f.tell()
            new_line = line.replace(find_str,new_str)
            print '-->new_line: ',new_line
			f.write(new_line)
f.close()
