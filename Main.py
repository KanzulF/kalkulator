# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

Hasil = 1000
Perhitungan = 1001

###########################################################################
## Class Kalkulator
###########################################################################

class Kalkulator ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 575,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 575,500 ), wx.Size( 575,500 ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.File = wx.Menu()
		self.New = wx.MenuItem( self.File, wx.ID_ANY, u"New"+ u"\t" + u"Ctrl + N", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.Append( self.New )

		self.Save = wx.MenuItem( self.File, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl + S", wx.EmptyString, wx.ITEM_NORMAL )
		self.File.Append( self.Save )

		self.m_menubar1.Append( self.File, u"File" )

		self.Info = wx.Menu()
		self.MakedBy = wx.Menu()
		self.KanzulFiqri_19_2035 = wx.MenuItem( self.MakedBy, wx.ID_ANY, u"Kanzul Fiqri_19-2035", wx.EmptyString, wx.ITEM_NORMAL )
		self.MakedBy.Append( self.KanzulFiqri_19_2035 )

		self.Info.AppendSubMenu( self.MakedBy, u"Maked By" )

		self.PBO2Duties = wx.MenuItem( self.Info, wx.ID_ANY, u"PBO 2 Duties", wx.EmptyString, wx.ITEM_NORMAL )
		self.Info.Append( self.PBO2Duties )

		self.m_menubar1.Append( self.Info, u"Info" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Hasil" ), wx.VERTICAL )

		self.Hasil = wx.TextCtrl( sbSizer3.GetStaticBox(), Hasil, wx.EmptyString, wx.DefaultPosition, wx.Size( 550,45 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.Hasil.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.Hasil.SetMinSize( wx.Size( 550,45 ) )
		self.Hasil.SetMaxSize( wx.Size( 550,45 ) )

		sbSizer3.Add( self.Hasil, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Perhitungan" ), wx.VERTICAL )

		self.Perhitungan = wx.TextCtrl( sbSizer2.GetStaticBox(), Perhitungan, wx.EmptyString, wx.DefaultPosition, wx.Size( 550,45 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.Perhitungan.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.Perhitungan.SetMinSize( wx.Size( 550,45 ) )
		self.Perhitungan.SetMaxSize( wx.Size( 550,45 ) )

		sbSizer2.Add( self.Perhitungan, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )

		baris1 = wx.BoxSizer( wx.HORIZONTAL )

		self.tombol1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol1.SetMinSize( wx.Size( 100,45 ) )
		self.tombol1.SetMaxSize( wx.Size( 100,45 ) )

		baris1.Add( self.tombol1, 0, wx.ALL, 5 )

		self.tombol2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol2.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol2.SetMinSize( wx.Size( 100,45 ) )
		self.tombol2.SetMaxSize( wx.Size( 100,45 ) )

		baris1.Add( self.tombol2, 0, wx.ALL, 5 )

		self.tombol3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol3.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol3.SetMinSize( wx.Size( 100,45 ) )
		self.tombol3.SetMaxSize( wx.Size( 100,45 ) )

		baris1.Add( self.tombol3, 0, wx.ALL, 5 )

		self.tombolAkar = wx.Button( self, wx.ID_ANY, u"b√(a)", wx.Point( -1,-1 ), wx.Size( 100,45 ), 0 )
		self.tombolAkar.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolAkar.SetMinSize( wx.Size( 100,45 ) )
		self.tombolAkar.SetMaxSize( wx.Size( 100,45 ) )

		baris1.Add( self.tombolAkar, 0, wx.ALL, 5 )

		self.tombolKuadrat = wx.Button( self, wx.ID_ANY, u"a^b", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombolKuadrat.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolKuadrat.SetMinSize( wx.Size( 100,45 ) )
		self.tombolKuadrat.SetMaxSize( wx.Size( 100,45 ) )

		baris1.Add( self.tombolKuadrat, 0, wx.ALL, 5 )


		bSizer1.Add( baris1, 0, wx.EXPAND, 5 )

		baris2 = wx.BoxSizer( wx.HORIZONTAL )

		self.tombol4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol4.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol4.SetMinSize( wx.Size( 100,45 ) )
		self.tombol4.SetMaxSize( wx.Size( 100,45 ) )

		baris2.Add( self.tombol4, 0, wx.ALL, 5 )

		self.tombol5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol5.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol5.SetMinSize( wx.Size( 100,45 ) )
		self.tombol5.SetMaxSize( wx.Size( 100,45 ) )

		baris2.Add( self.tombol5, 0, wx.ALL, 5 )

		self.tombol6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol6.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol6.SetMinSize( wx.Size( 100,45 ) )
		self.tombol6.SetMaxSize( wx.Size( 100,45 ) )

		baris2.Add( self.tombol6, 0, wx.ALL, 5 )

		self.tombolBagi = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombolBagi.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolBagi.SetMinSize( wx.Size( 100,45 ) )
		self.tombolBagi.SetMaxSize( wx.Size( 100,45 ) )

		baris2.Add( self.tombolBagi, 0, wx.ALL, 5 )

		self.tombolHapus = wx.Button( self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombolHapus.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolHapus.SetMinSize( wx.Size( 100,45 ) )
		self.tombolHapus.SetMaxSize( wx.Size( 100,45 ) )

		baris2.Add( self.tombolHapus, 0, wx.ALL, 5 )


		bSizer1.Add( baris2, 0, wx.EXPAND, 5 )

		baris3 = wx.BoxSizer( wx.HORIZONTAL )

		self.tombol7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol7.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol7.SetMinSize( wx.Size( 100,45 ) )
		self.tombol7.SetMaxSize( wx.Size( 100,45 ) )

		baris3.Add( self.tombol7, 0, wx.ALL, 5 )

		self.tombol8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol8.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol8.SetMinSize( wx.Size( 100,45 ) )
		self.tombol8.SetMaxSize( wx.Size( 100,45 ) )

		baris3.Add( self.tombol8, 0, wx.ALL, 5 )

		self.tombol9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol9.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol9.SetMinSize( wx.Size( 100,45 ) )
		self.tombol9.SetMaxSize( wx.Size( 100,45 ) )

		baris3.Add( self.tombol9, 0, wx.ALL, 5 )

		self.tombolKali = wx.Button( self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombolKali.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolKali.SetMinSize( wx.Size( 100,45 ) )
		self.tombolKali.SetMaxSize( wx.Size( 100,45 ) )

		baris3.Add( self.tombolKali, 0, wx.ALL, 5 )

		self.tombolKoma = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombolKoma.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolKoma.SetMinSize( wx.Size( 100,45 ) )
		self.tombolKoma.SetMaxSize( wx.Size( 100,45 ) )

		baris3.Add( self.tombolKoma, 0, wx.ALL, 5 )


		bSizer1.Add( baris3, 0, wx.EXPAND, 5 )

		baris4 = wx.BoxSizer( wx.HORIZONTAL )

		self.minesPlus = wx.Button( self, wx.ID_ANY, u"-/+", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.minesPlus.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.minesPlus.SetMinSize( wx.Size( 100,45 ) )
		self.minesPlus.SetMaxSize( wx.Size( 100,45 ) )

		baris4.Add( self.minesPlus, 0, wx.ALL, 5 )

		self.tombol0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombol0.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombol0.SetMinSize( wx.Size( 100,45 ) )
		self.tombol0.SetMaxSize( wx.Size( 100,45 ) )

		baris4.Add( self.tombol0, 0, wx.ALL, 5 )

		self.tombolKurang = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombolKurang.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolKurang.SetMinSize( wx.Size( 100,45 ) )
		self.tombolKurang.SetMaxSize( wx.Size( 100,45 ) )

		baris4.Add( self.tombolKurang, 0, wx.ALL, 5 )

		self.tombolTambah = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombolTambah.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolTambah.SetMinSize( wx.Size( 100,45 ) )
		self.tombolTambah.SetMaxSize( wx.Size( 100,45 ) )

		baris4.Add( self.tombolTambah, 0, wx.ALL, 5 )

		self.tombolSamaDengan = wx.Button( self, wx.ID_ANY, u"=/clear", wx.DefaultPosition, wx.Size( 100,45 ), 0 )
		self.tombolSamaDengan.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tombolSamaDengan.SetMinSize( wx.Size( 100,45 ) )
		self.tombolSamaDengan.SetMaxSize( wx.Size( 100,45 ) )

		baris4.Add( self.tombolSamaDengan, 0, wx.ALL, 5 )


		bSizer1.Add( baris4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tombol1.Bind( wx.EVT_BUTTON, self.tombol1OnButtonClick )
		self.tombol2.Bind( wx.EVT_BUTTON, self.tombol2OnButtonClick )
		self.tombol3.Bind( wx.EVT_BUTTON, self.tombol3OnButtonClick )
		self.tombolAkar.Bind( wx.EVT_BUTTON, self.tombolAkarOnButtonClick )
		self.tombolKuadrat.Bind( wx.EVT_BUTTON, self.tombolKuadratOnButtonClick )
		self.tombol4.Bind( wx.EVT_BUTTON, self.tombol4OnButtonClick )
		self.tombol5.Bind( wx.EVT_BUTTON, self.tombol5OnButtonClick )
		self.tombol6.Bind( wx.EVT_BUTTON, self.tombol6OnButtonClick )
		self.tombolBagi.Bind( wx.EVT_BUTTON, self.tombolBagiOnButtonClick )
		self.tombolHapus.Bind( wx.EVT_BUTTON, self.tombolHapusOnButtonClick )
		self.tombol7.Bind( wx.EVT_BUTTON, self.tombol7OnButtonClick )
		self.tombol8.Bind( wx.EVT_BUTTON, self.tombol8OnButtonClick )
		self.tombol9.Bind( wx.EVT_BUTTON, self.tombol9OnButtonClick )
		self.tombolKali.Bind( wx.EVT_BUTTON, self.tombolKaliOnButtonClick )
		self.tombolKoma.Bind( wx.EVT_BUTTON, self.tombolKomaOnButtonClick )
		self.minesPlus.Bind( wx.EVT_BUTTON, self.minesPlusOnButtonClick )
		self.tombol0.Bind( wx.EVT_BUTTON, self.tombol0OnButtonClick )
		self.tombolKurang.Bind( wx.EVT_BUTTON, self.tombolKurangOnButtonClick )
		self.tombolTambah.Bind( wx.EVT_BUTTON, self.tombolTambahOnButtonClick )
		self.tombolSamaDengan.Bind( wx.EVT_BUTTON, self.tombolSamaDenganOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tombol1OnButtonClick( self, event ):
		event.Skip()

	def tombol2OnButtonClick( self, event ):
		event.Skip()

	def tombol3OnButtonClick( self, event ):
		event.Skip()

	def tombolAkarOnButtonClick( self, event ):
		event.Skip()

	def tombolKuadratOnButtonClick( self, event ):
		event.Skip()

	def tombol4OnButtonClick( self, event ):
		event.Skip()

	def tombol5OnButtonClick( self, event ):
		event.Skip()

	def tombol6OnButtonClick( self, event ):
		event.Skip()

	def tombolBagiOnButtonClick( self, event ):
		event.Skip()

	def tombolHapusOnButtonClick( self, event ):
		event.Skip()

	def tombol7OnButtonClick( self, event ):
		event.Skip()

	def tombol8OnButtonClick( self, event ):
		event.Skip()

	def tombol9OnButtonClick( self, event ):
		event.Skip()

	def tombolKaliOnButtonClick( self, event ):
		event.Skip()

	def tombolKomaOnButtonClick( self, event ):
		event.Skip()

	def minesPlusOnButtonClick( self, event ):
		event.Skip()

	def tombol0OnButtonClick( self, event ):
		event.Skip()

	def tombolKurangOnButtonClick( self, event ):
		event.Skip()

	def tombolTambahOnButtonClick( self, event ):
		event.Skip()

	def tombolSamaDenganOnButtonClick( self, event ):
		event.Skip()


