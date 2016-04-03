#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set ts=4 fenc=utf-8:

import gdata.spreadsheets.client
import gdata.spreadsheet.text_db 
from oauth2client.service_account import ServiceAccountCredentials
import pprint

class DriverGspread():

	def __init__(self):
		self.__id			= None
		self.__client		= None
		self.__sheet		= None
		self.__credential	= None
		self.__authorize	= False
		pass

	def connect(self,sheet_name=None) :

		self.__client	= gdata.spreadsheets.client.SpreadsheetsClient()

		if self.__authorize is False :
			credentials		= ServiceAccountCredentials.from_json_keyfile_name(
								self.__credential,
								['https://www.googleapis.com/auth/drive']
							)

			# OAuth2.0での認証設定
			auth_token		= gdata.gauth.OAuth2TokenFromCredentials(credentials)
			auth_token.authorize(self.__client)
			self.__authorize = True

		# worksheetの取得。シートが指定されて無い場合は1番目のシートに接続
		return self.getWorkSheetByName(sheet_name)
	
	def setConfig(self,config="") :
		self.setWorksheetsId(config['DataAccess']['id'])
		self.__credential	= config['DataAccess']['credential']
		pass

	def setWorksheetsId(self,id=None):
		self.__id	= id
		pass

	def getWorksheetsId(self):
		return self.__id

	def getTest(self):
		print type(self.__sheet)
		print self.__sheet.title.text
		
		list_feed	= self.__client.get_list_feed(self.getWorksheetsId(), 
									self.__sheet.get_worksheet_id())
		for feed in list_feed.entry:
			print feed.get_value('projectname')
			print feed.get_value('invoiceno')
			print feed.get_value('orderdate')
			if feed.get_value('paymentdate') 

	def getWorkSheetByName(self, sheet_name=None):

		# worksheetの取得。シートが指定されて無い場合は1番目のシートに接続
		if sheet_name is None :
			self.__sheet	= self.__client.get_worksheet(self.getWorksheetsId(), 'od6')
			return True
		else :
			work_sheets	= self.__client.get_worksheets(self.getWorksheetsId()) 
			for sheet in work_sheets.entry :
				if sheet.title.text == sheet_name :
					self.__sheet =  sheet
					return True
			return False
