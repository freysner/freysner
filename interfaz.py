import tkinter as tk
from tkinter import ttk, BOTH
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import kmp_final as kmp
import rk_final as rk
import nw_final as nw
import re
import time
import numpy as np
from Bio import pairwise2
from Bio.Seq import Seq

class ExactoFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(width="800",height="500")
        
        self.cargar_button = ttk.Button(
            self, text="Cargar secuencia", command=self.cargarArchivo)
        self.cargar_button.place(x=15,y=5)
        
        self.cargar_label = ttk.Label(self,text="?")
        self.cargar_label.place(x=150,y=5)
        
        self.pat_label = ttk.Label(self,text="Ingresar Patrón: ")
        self.pat_label.place(x=15,y=40)
        
        self.name_entry = ttk.Entry(self)
        self.name_entry.place(x=150,y=40,width="250")
        
        self.emp_kmp_button = ttk.Button(
            self, text="Búsqueda Knuth-Morris-Pratt", command=self.busquedaKMP)
        self.emp_kmp_button.place(x=15,y=75)
        
        self.emp_rk_button = ttk.Button(
            self, text="Búsqueda Rabin-Karp", command=self.busquedaRK)
        self.emp_rk_button.place(x=250,y=75)

        self.resultado = tk.Text(self, height=16, width=33)
        self.resultado.place(x=1,y=110)
        quote = """"""
        self.resultado.insert(tk.END, quote)
        
        self.secuencia = tk.Text(self, height=16, width=76)
        self.secuencia.place(x=282,y=110)
        quote = """"""
        self.secuencia.insert(tk.END, quote)

    
    def cargarArchivo(self):
        filetypes = (
        ('text files', '*.fasta'),
        ('All files', '*')
        )

        filename = fd.askopenfilename(
        title='Abrir un archivo',
        initialdir='/home/freysner/codigos/tesis',
        filetypes=filetypes)

        showinfo(title='Seleccionar un archivo',message=filename)
        self.cargar_label["text"] = "{}".format(filename)
        f=open(filename,'r')
        self.secuencia.insert(tk.END,f.read())
        f.close()
    
    def busquedaKMP(self):
        txt=''
        filename=self.cargar_label["text"]
        for _ in range(100):
           f=open(filename,'r')
           for i in f:
              txt+=i.strip()
        f.close()
        #pat="GATGATC"
	#self.resultado.delete(tk.FIRST,tk.END)
	#pat='TTTAGTAGTGCTATCCCCATGTGATTTTAATAGCTTCTTAGGAGAATGACAAAAAAAAAAAAAAAA'
        pat=self.name_entry.get()
        inicio=time.time_ns()
        mensaje='\nKMP encontro '+str(len(kmp.KMPSearch(pat, txt)))
        mensaje+='\ntiempo en ns '+str(time.time_ns()-inicio)
	#self.resultado.insert(tk.END,mensaje)
        inicio=time.time_ns()
        resultado=[]
        x=0
        while True:
           x=txt.find(pat,x+1)
           if x==-1:
              break
           resultado.append(x)
        mensaje+='\nFind encontro '+str(len(resultado))
        mensaje+='\ntiempo en ns '+str(time.time_ns()-inicio)
        inicio=time.time_ns()
        a=re.compile(pat)
        b=a.finditer(txt)
        resultado=[]
        for i in b:
           resultado.append(i.start())
        mensaje+='\nRE encontro '+str(len(resultado))
        mensaje+='\ntiempo en ns '+str(time.time_ns()-inicio)
	#self.resultado.delete(tk.FIRST,tk.END)
        self.resultado.insert(tk.END,mensaje)

    def busquedaRK(self):
        txt=''
        filename=self.cargar_label["text"]
        for _ in range(100):
           f=open(filename,'r')
           for i in f:
              txt+=i.strip()
        f.close()
        #pat="GATGATC"
        #self.resultado.delete(tk.FIRST,tk.END)
        #pat='TTTAGTAGTGCTATCCCCATGTGATTTTAATAGCTTCTTAGGAGAATGACAAAAAA
        pat=self.name_entry.get()
        inicio=time.time_ns()
        mensaje='\nRK encontro '+str(len(rk.rabinKarp(pat, txt)))
        mensaje+='\ntiempo en ns '+str(time.time_ns()-inicio)
        self.resultado.insert(tk.END,mensaje)
	

class AlineacionFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width="800",height="500")
        
        self.pat_label = ttk.Label(self,text="Secuencia 1: ")
        self.pat_label.place(x=15,y=5)
        
        self.seq1_entry = ttk.Entry(self)
        self.seq1_entry.place(x=150,y=5,width="350")
        
        self.pat_label = ttk.Label(self,text="Secuencia 2: ")
        self.pat_label.place(x=15,y=40)
        
        self.seq2_entry = ttk.Entry(self)
        self.seq2_entry.place(x=150,y=40,width="350")
        
        self.emp_rk_button = ttk.Button(
            self, text="Alineamiento Needleman-Wunsch", command=self.alinearNW)
        self.emp_rk_button.place(x=150,y=75)

        self.resultado = tk.Text(self, height=16, width=65)
        self.resultado.place(x=15,y=110)
        quote = """"""
        self.resultado.insert(tk.END, quote)
        
    def alinearNW(self):
        txt=''
	#filename=self.cargar_label["text"]
        s1=self.seq1_entry.get()
        s2=self.seq2_entry.get()
        inicio=time.time_ns()
        a1,a2=nw.needlemanWunsch(s1,s2)
        mensaje=a1+'\n'+a2
        mensaje+='\ntiempo en ns '+str(time.time_ns()-inicio)

        seq1 = Seq(s1)
        seq2 = Seq(s2)

        inicio=time.time_ns()
        alignments = pairwise2.align.globalxx(seq1, seq2)

        for match in alignments:
           mensaje+='\n'+str(match)

        mensaje+='\nBiopython tiempo en ns'+str(time.time_ns()-inicio)
	
        self.resultado.insert(tk.END,mensaje)
        
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("PROTOTIPO")
        self.notebook = ttk.Notebook(self)
        
        self.label = ttk.Label(self,text="EMPAREJAMIENTO DE SECUENCIAS DE ADN")
        self.label.pack()
        
        self.exacto_frame = ExactoFrame(self.notebook)
        self.notebook.add(
            self.exacto_frame, text="BÚSQUEDA", padding=15)
        
        self.alineacion_frame = AlineacionFrame(self.notebook)
        self.notebook.add(
            self.alineacion_frame, text="ALINEACIÓN", padding=15)
        
        self.notebook.pack(fill=BOTH,expand=1)
        self.pack()

main_window = tk.Tk()
main_window.geometry("800x520")
app = Application(main_window)
app.mainloop()
