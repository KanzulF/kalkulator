import wx
import Main

class subClass(Main.Kalkulator):
	def __init__(self,parent):
		self.hasil = "0"
		self.hitung = ""
		self.operator = ""
		self.perhitungan = []
		self.isi = ""
		Main.Kalkulator.__init__(self,parent)	

	def setValueHasil(self):
		self.Hasil.SetValue(str(self.hasil))

	def setValueperhitungan(self,tambahan):
		for i in self.perhitungan:
			self.isi = self.isi + i
		self.isi = str(self.isi) + str(tambahan)
		self.Perhitungan.SetValue(str(self.isi))
		self.isi = ""

	def eksekusi(self):
		try:
			if self.operator == "√":
				self.hasil = float(self.hasil)**(1/float(self.hitung))
			elif self.operator == "^":
				self.hasil = float(self.hasil)**float(self.hitung)
			elif self.operator == "+":
				self.hasil = float(self.hasil)+float(self.hitung)
			elif self.operator == "-":
				self.hasil = float(self.hasil)-float(self.hitung)
			elif self.operator == "/":
				self.hasil = float(self.hasil)/float(self.hitung)
			elif self.operator == "*":
				self.hasil = float(self.hasil)*float(self.hitung)
			else:
				self.hasil = float(self.hitung)
			self.setValueHasil()
			self.hitung = ""
		except:
			pass
#override
#angka
	def tombol1OnButtonClick(self,event):
		self.hitung = str(self.hitung + "1")
		self.setValueperhitungan(self.hitung)

	def tombol2OnButtonClick(self,event):
		self.hitung = str(self.hitung + "2")
		self.setValueperhitungan(self.hitung)

	def tombol3OnButtonClick(self,event):
		self.hitung = str(self.hitung + "3")
		self.setValueperhitungan(self.hitung)

	def tombol4OnButtonClick(self,event):
		self.hitung = str(self.hitung + "4")
		self.setValueperhitungan(self.hitung)

	def tombol5OnButtonClick(self,event):
		self.hitung = str(self.hitung + "5")
		self.setValueperhitungan(self.hitung)

	def tombol6OnButtonClick(self,event):
		self.hitung = str(self.hitung + "6")
		self.setValueperhitungan(self.hitung)

	def tombol7OnButtonClick(self,event):
		self.hitung = str(self.hitung + "7")
		self.setValueperhitungan(self.hitung)

	def tombol8OnButtonClick(self,event):
		self.hitung = str(self.hitung + "8")
		self.setValueperhitungan(self.hitung)

	def tombol9OnButtonClick(self,event):
		self.hitung = str(self.hitung + "9")
		self.setValueperhitungan(self.hitung)

	def tombol0OnButtonClick(self,event):
		self.hitung = self.hitung + "0"
		self.setValueperhitungan(self.hitung)

#operator
	def tombolBagiOnButtonClick(self,event):
		self.perhitungan.append(self.hitung)
		self.perhitungan.append(" / ")
		self.setValueperhitungan("")
		self.eksekusi()
		self.operator = "/"

	def tombolHapusOnButtonClick( self, event ):
		self.hitung = self.hitung[:-1]
		self.setValueperhitungan(self.hitung)

	def tombolAkarOnButtonClick(self,event):
		self.perhitungan.append(self.hitung)
		self.perhitungan.append("√ ")
		self.setValueperhitungan("")
		self.eksekusi()
		self.operator = "√"

	def tombolKuadratOnButtonClick(self,event):
		self.perhitungan.append(self.hitung)
		self.perhitungan.append("^")
		self.setValueperhitungan("")
		self.eksekusi()
		self.operator = "^"

	def tombolKaliOnButtonClick(self,event):
		self.perhitungan.append(self.hitung)
		self.perhitungan.append(" * ")
		self.setValueperhitungan("")
		self.eksekusi()
		self.operator = "*"

	def tombolKomaOnButtonClick( self, event ):
		if self.hitung == "":
			self.hitung = "0"
		self.hitung = self.hitung + "."
		self.setValueperhitungan(self.hitung)

	def minesPlusOnButtonClick(self,event):
		self.hitung = str(int(self.hitung) * (-1))
		self.setValueperhitungan(self.hitung)


	def tombolKurangOnButtonClick(self,event):
		self.perhitungan.append(self.hitung)
		self.perhitungan.append(" - ")
		self.setValueperhitungan("")
		self.eksekusi()
		self.operator = "-"

	def tombolTambahOnButtonClick(self,event):
		self.perhitungan.append(self.hitung)
		self.perhitungan.append(" + ")
		self.setValueperhitungan("")
		self.eksekusi()
		self.operator = "+"

	def tombolSamaDenganOnButtonClick( self, event ):
		self.perhitungan.append(self.hitung)
		self.perhitungan.append(" = ")
		self.eksekusi()
		self.setValueperhitungan(self.hasil)
		self.hasil = "0"
		self.hitung = ""
		self.operator = ""
		self.perhitungan = []
		self.isi = ""



app = wx.App()
frame = subClass(parent=None)
frame.Show()

app.MainLoop()
