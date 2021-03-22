import wx
import Main

class subClass(Main.Kalkulator):
	def __init__(self,parent):
		self.hasil = 0
		self.hitung = ""
		self.hitung2 = ""
		self.hitung3 = ""
		Main.Kalkulator.__init__(self,parent)

	def setValueHasil(self):
		self.Hasil.SetValue(str(self.hasil))

	def setValueperhitungan(self,tambahan):
		self.Perhitungan.SetValue(tambahan)


#override
	def tombol1OnButtonClick(self,event):
		self.hitung = self.hitung + "1"
		self.hitung2 = self.hitung2 + "1"
		self.setValueperhitungan(self.hitung2)

	def tombol2OnButtonClick(self,event):
		self.hitung = self.hitung + "2"
		self.hitung2 = self.hitung2 + "2"
		self.setValueperhitungan(self.hitung2)

	def tombol3OnButtonClick(self,event):
		self.hitung = self.hitung + "3"
		self.hitung2 = self.hitung2 + "3"
		self.setValueperhitungan(self.hitung2)

	def tombolAkarOnButtonClick(self,event):
		self.hitung2 = self.hitung2 + ' (√(a)), '
		self.hasil = self.hitung
		self.hasil = float(self.hasil)**(1/2)
		self.setValueHasil()
		self.setValueperhitungan(self.hitung2)
		self.hitung = ""

	def tombolKuadratOnButtonClick(self,event):
		self.hitung2 = self.hitung2 + ' (a^2), '
		self.hasil = self.hitung
		self.hasil = float(self.hasil) * float(self.hasil)
		self.setValueHasil()
		self.setValueperhitungan(self.hitung2)
		self.hitung = ""

	def tombol4OnButtonClick(self,event):
		self.hitung = self.hitung + "4"
		self.hitung2 = self.hitung2 + "4"
		self.setValueperhitungan(self.hitung2)

	def tombol5OnButtonClick(self,event):
		self.hitung = self.hitung + "5"
		self.hitung2 = self.hitung2 + "5"
		self.setValueperhitungan(self.hitung2)

	def tombol6OnButtonClick(self,event):
		self.hitung = self.hitung + "6"
		self.hitung2 = self.hitung2 + "6"
		self.setValueperhitungan(self.hitung2)

	def tombolBagiOnButtonClick(self,event):
		self.hitung2 = self.hitung2 + ' / '
		self.hasil = float(self.hasil) / float(self.hitung)
		self.setValueHasil()
		self.setValueperhitungan(self.hitung2)
		self.hitung = ""

	def tombolHapusOnButtonClick( self, event ):
		event.Skip()

	def tombol7OnButtonClick(self,event):
		self.hitung = self.hitung + "7"
		self.hitung2 = self.hitung2 + "7"
		self.setValueperhitungan(self.hitung2)

	def tombol8OnButtonClick(self,event):
		self.hitung = self.hitung + "8"
		self.hitung2 = self.hitung2 + "8"
		self.setValueperhitungan(self.hitung2)

	def tombol9OnButtonClick(self,event):
		self.hitung = self.hitung + "9"
		self.hitung2 = self.hitung2 + "9"
		self.setValueperhitungan(self.hitung2)

	def tombolKaliOnButtonClick(self,event):
		self.hitung2 = self.hitung2 + ' / '
		self.hasil = float(self.hasil) * float(self.hitung)
		self.setValueHasil()
		self.setValueperhitungan(self.hitung2)
		self.hitung = ""

	def tombolKomaOnButtonClick( self, event ):
		event.Skip()

	def minesPlusOnButtonClick(self,event):
		event.Skip()

	def tombol0OnButtonClick(self,event):
		self.hitung = self.hitung + "0"
		self.hitung2 = self.hitung2 + "0"
		self.setValueperhitungan(self.hitung2)

	def tombolKurangOnButtonClick(self,event):
		self.hitung2 = self.hitung2 + ' - '
		self.hasil = float(self.hasil) - float(self.hitung)
		self.setValueHasil()
		self.setValueperhitungan(self.hitung2)
		self.hitung = ""

	def tombolTambahOnButtonClick(self,event):
		self.hitung2 = self.hitung2 + ' + '
		self.hasil = float(self.hasil) + float(self.hitung)
		self.setValueHasil()
		self.setValueperhitungan(self.hitung2)
		self.hitung = ""

	def tombolSamaDenganOnButtonClick( self, event ):
		self.setValueHasil()


app = wx.App()
frame = subClass(parent=None)
frame.Show()

app.MainLoop()
