# -*- coding: utf-8 -*- ############################################################################# Python code generated with wxFormBuilder (version Nov 27 2012)## http://www.wxformbuilder.org/#### PLEASE DO "NOT" EDIT THIS FILE!###########################################################################import wximport wx.xrc############################################################################# Class BaseDialog###########################################################################class BaseDialog ( wx.Frame ):		def __init__( self, parent ):		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tumblr Templatr - Develop tumblr themes offline", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )				self.SetSizeHintsSz( wx.DefaultSize, wx.Size( 600,400 ) )		self.SetForegroundColour( wx.Colour( 255, 255, 255 ) )		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )				gSizer2 = wx.GridSizer( 0, 2, 0, 0 )				bSizer5 = wx.BoxSizer( wx.VERTICAL )				self.intro_bitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"dialog/bg.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )		self.intro_bitmap.SetMaxSize( wx.Size( 250,400 ) )				bSizer5.Add( self.intro_bitmap, 0, wx.ALL, 5 )						gSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )				bSizer7 = wx.BoxSizer( wx.VERTICAL )						bSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )				self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Select Themes Directory", wx.Point( -1,-1 ), wx.DefaultSize, 0 )		self.m_staticText11.Wrap( -1 )		bSizer7.Add( self.m_staticText11, 0, wx.ALL, 5 )				self.themes_directory = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.Point( 100,100 ), wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )		self.themes_directory.Enable( False )				bSizer7.Add( self.themes_directory, 0, wx.ALL, 5 )				self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )		self.m_staticText5.Wrap( -1 )		bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )				self.server_port = wx.TextCtrl( self, wx.ID_ANY, u"13323", wx.DefaultPosition, wx.DefaultSize, 0 )		self.server_port.SetMaxLength( 6 ) 		bSizer7.Add( self.server_port, 0, wx.ALL, 10 )						bSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )				self.status_text = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )		self.status_text.Wrap( -1 )		bSizer7.Add( self.status_text, 0, wx.ALL, 5 )				self.server_ctrl_button = wx.Button( self, wx.ID_ANY, u"Start Server", wx.DefaultPosition, wx.DefaultSize, 0 )		bSizer7.Add( self.server_ctrl_button, 0, wx.ALL, 5 )						bSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )						bSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )						gSizer2.Add( bSizer7, 1, wx.EXPAND, 5 )						self.SetSizer( gSizer2 )		self.Layout()		self.m_menubar1 = wx.MenuBar( 0 )		self.m_menu1 = wx.Menu()		self.how_to_use = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"How to use?", wx.EmptyString, wx.ITEM_NORMAL )		self.m_menu1.AppendItem( self.how_to_use )				self.m_menubar1.Append( self.m_menu1, u"Help" ) 				self.SetMenuBar( self.m_menubar1 )						self.Centre( wx.BOTH )				# Connect Events		self.Bind( wx.EVT_CLOSE, self.exit_server )		self.themes_directory.Bind( wx.EVT_DIRPICKER_CHANGED, self.select_path )		self.server_ctrl_button.Bind( wx.EVT_BUTTON, self.start_server )		def __del__( self ):		pass			# Virtual event handlers, overide them in your derived class	def exit_server( self, event ):		event.Skip()		def select_path( self, event ):		event.Skip()		def start_server( self, event ):		event.Skip()	