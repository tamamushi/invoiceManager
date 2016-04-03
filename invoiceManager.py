#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set ts=4 fenc=utf-8:

from driver.abstract import *

def main():

	table_name	= "invoice"
	db			= DbAbstract().setDriver('secret/driver.cfg')

	if not db.connect(table_name) :
		print "connect false"
		sys.exit()

	print "connect success"
	db.getRecordList()

if __name__ == '__main__':
	main()
