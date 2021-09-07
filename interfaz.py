import tkinter as tk
from tkinter import ttk, BOTH
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import kmp_final as kmp
import kmp_menosuno as kmp2
import rk_final as rk
import bm as bm
import skip_search as ss
import nw_final as nw
import re
import time
import numpy as np
from Bio import pairwise2
from Bio import SeqIO
from Bio.Seq import Seq

class ExactoFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(width="800",height="500")
        
        self.cargar_button = ttk.Button(self, text="Cargar secuencia", command=self.cargarArchivo)
        self.cargar_button.place(x=5,y=5)
        
        self.cargar_label = ttk.Label(self,text="?")
        self.cargar_label.place(x=150,y=5)
        
        self.pat_label = ttk.Label(self,text="Ingresar Patrón")
        self.pat_label.place(x=5,y=40)
        
        self.name_entry = ttk.Entry(self)
        self.name_entry.place(x=5,y=70,width="250")
        
        self.pat_label = ttk.Label(self,text="Elegir algoritmo")
        self.pat_label.place(x=5,y=100)
        
        self.emp_kmp_button = ttk.Button(self, text="Buscar", command=self.busqueda)
        self.emp_kmp_button.place(x=5,y=160)
        
        self.combo = ttk.Combobox(self)
        self.combo.place(x=5, y=130)
        self.combo["values"] = ["Knuth-Morris-Pratt", "Rabin-Karp", "Boyre-Moore", "Skip-Search"]

        self.resultado = tk.Text(self, height=10, width=30)
        self.resultado.place(x=1,y=200)
        self.resultado.insert(tk.END, "")

	
        self.ini_label = ttk.Label(self,text="Pos.Inicial")
        self.ini_label.place(x=282,y=40)
        
        self.ini_entry = ttk.Entry(self)
        self.ini_entry.place(x=282,y=70,width="90")
        
        self.secuencia = tk.Text(self, height=16, width=76)
        
        self.fin_label = ttk.Label(self,text="Pos.Fin")
        self.fin_label.place(x=380,y=40)
        
        self.fin_entry = ttk.Entry(self)
        self.fin_entry.place(x=380,y=70,width="90")
        
        self.emp_kmp_button = ttk.Button(self, text="Mostrar", command=self.mostrar)
        self.emp_kmp_button.place(x=500,y=67)
        
        self.emp_kmp_button = ttk.Button(self, text="Limpiar", command=self.limpiar)
        self.emp_kmp_button.place(x=600,y=67)


        self.sec_label = ttk.Label(self,text="*")
        self.sec_label.place(x=480,y=5)
	
        self.secuencia.place(x=282,y=110)
        self.secuencia.insert(tk.END, "")

    
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
        secADN=SeqIO.read(filename,"fasta")
        secSeq=secADN.seq
        self.secuencia.delete("1.0","end")
        self.resultado.delete("1.0","end")
        mensaje="Longitud: "
        mensaje+=str(len(secSeq))+"\n"
        mensaje+="Contenido GC: "
        mensaje+=str(100 * float(secSeq.count("G") + secSeq.count("C")) / len(secSeq))
        self.sec_label["text"]=mensaje
    
    def busqueda(self):
        txt=self.secuencia.get("1.0","end")
        pat=self.name_entry.get()
        inicio=time.time_ns()
        opcion=self.combo.get()
        if(opcion=="Knuth-Morris-Pratt"):
           mensaje='\nKMP encontro '+str(len(kmp2.KMP(pat, txt)))
        if(opcion=="Rabin-Karp"):
           mensaje='\nRK encontro '+str(len(rk.rabinKarp(pat, txt)))
        if(opcion=="Boyre-Moore"):
           mensaje='\nBM encontro '+str(len(bm.BM(pat, txt)))
        if(opcion=="Skip-Search"):
           mensaje='\nSkip-Search encontro '+str(len(ss.SKIP(pat, txt)))
	
        mensaje+='\ntiempo en ns '+str(time.time_ns()-inicio)
        self.resultado.insert(tk.END,mensaje)


    def mostrar(self):
        ini=self.ini_entry.get()
        fin=self.fin_entry.get()
        filename=self.cargar_label["text"]
        secADN=SeqIO.read(filename,"fasta")
        secSeq=secADN.seq
        mensaje=secSeq[int(ini):int(fin)]
        self.secuencia.insert(tk.END,mensaje)

    def limpiar(self):
        self.secuencia.delete("1.0","end")
	

class FragmentacionFrame(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config(width="800",height="500")
        
        self.cargar_button = ttk.Button(
            self, text="Secuencia Referencia", command=self.cargarReferencia)
        self.cargar_button.place(x=5,y=5)
        
        self.cargar1_label = ttk.Label(self,text="?")
        self.cargar1_label.place(x=200,y=5)
        
        self.cargar_button = ttk.Button(self, text="Secuencia a fragmentar", command=self.cargarFragmentar)
        self.cargar_button.place(x=5,y=40)
        
        self.cargar2_label = ttk.Label(self,text="?")
        self.cargar2_label.place(x=200,y=40)
        
        self.tamano_label = ttk.Label(self,text="Tamaño de fragmentos")
        self.tamano_label.place(x=5,y=80)
        
        self.tamano_entry = ttk.Entry(self)
        self.tamano_entry.place(x=160,y=80,width="90")
        
        self.emparejar_button = ttk.Button(self, text="Alineamiento exacto de Fragmentos", command='')
        self.emparejar_button.place(x=280,y=78)
        
        self.secuencia = tk.Text(self, height=13, width=70)
        self.secuencia.place(x=5,y=120)
        self.secuencia.insert(tk.END, "")
        
	
    def cargarReferencia(self):
        filetypes = (
        ('text files', '*.fasta'),
        ('All files', '*')
        )

        filename = fd.askopenfilename(
        title='Abrir un archivo',
        initialdir='/home/freysner/codigos/tesis',
        filetypes=filetypes)

        showinfo(title='Seleccionar un archivo',message=filename)
        self.cargar1_label["text"] = "{}".format(filename)
    
    def cargarFragmentar(self):
        filetypes = (
        ('text files', '*.fasta'),
        ('All files', '*')
        )

        filename = fd.askopenfilename(
        title='Abrir un archivo',
        initialdir='/home/freysner/codigos/tesis',
        filetypes=filetypes)

        showinfo(title='Seleccionar un archivo',message=filename)
        self.cargar2_label["text"] = "{}".format(filename)

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
        
        self.emp_kmp_button = ttk.Button(self, text="Limpiar", command=self.limpiar)
        self.emp_kmp_button.place(x=400,y=75)

        self.resultado = tk.Text(self, height=16, width=65)
        self.resultado.place(x=15,y=110)
        self.resultado.insert(tk.END, "")
        
    def alinearNW(self):
        txt=''
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
    

    def limpiar(self):
        self.resultado.delete("1.0","end")
        
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("PROGRAMA DEMOSTRATIVO")
        self.notebook = ttk.Notebook(self)
        
        self.label = ttk.Label(self,text="EMPAREJAMIENTO DE SECUENCIAS DE ADN")
        self.label.pack()
        
        self.exacto_frame = ExactoFrame(self.notebook)
        self.notebook.add(self.exacto_frame, text="BÚSQUEDA", padding=15)
        
        self.fragmentacion_frame = FragmentacionFrame(self.notebook)
        self.notebook.add(self.fragmentacion_frame, text="FRAGMENTACIÓN", padding=15)
        
        self.alineacion_frame = AlineacionFrame(self.notebook)
        self.notebook.add(self.alineacion_frame, text="ALINEACIÓN", padding=15)
        
        self.notebook.pack(fill=BOTH,expand=1)
        self.pack()

main_window = tk.Tk()
main_window.geometry("800x520")
app = Application(main_window)
app.mainloop()
