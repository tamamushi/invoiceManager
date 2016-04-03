#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set ts=4 fenc=utf-8:

import os, sys
from ConfigParser import SafeConfigParser

class DbAbstract():

	def __init__(self):
		self.__driver	= None
		self.__instance	= None
		pass

	def setDriver(self,fname="") :

		### File check
		if not os.path.exists(fname) :
			raise IOError(fname)

		parser			 = SafeConfigParser()
		parser.read(fname)

		## ConfigParserを使って連想配列に変換する
		config = {}
		for sect in parser.sections() :
			config[sect] = {}
			for opt in parser.options(sect) :
				config[sect][opt] = parser.get(sect, opt)

		self.__driver	= config['DataAccess']['driver']

		## DriverXxxxx の形式に変換。
		class_name		= 'Driver' + self.__driver.capitalize()

		## インポートを動的に実行。private変数の__instanceにドライバーの
		## インスタンスを格納する。
		module_name			= __import__('driver.' + self.__driver, globals(), locals(), [class_name], -1)
		class_constructor	= getattr(module_name, class_name)
		self.__instance		= class_constructor()

		## ドライバーにconfigオブジェクトを渡す
		self.__instance.setConfig(config)
		return self

	def connect(self, table_name):

		## ドライバーの「connect」メソッドでデータベースの
		## テーブルへ接続を実行
		return self.__instance.connect(table_name)

	def getRecordList(self):
		
		self.__instance.getTest()
