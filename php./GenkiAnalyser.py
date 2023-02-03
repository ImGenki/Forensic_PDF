import PyPDF2
import requests
import sys
from pysafebrowsing import SafeBrowsing
import psutil
import time
import oletools.olevba as olevba
from fpdf import FPDF
import subprocess
import os

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=30)
pdf.cell(200, 10, txt="Genki Analyser", ln=1, align="C")
pdf.cell(200, 10, txt="", ln=1, align="L")
pdf.set_font("Arial", size=20)
pdf.cell(200, 10, txt=sys.argv[1], ln=1, align="C")
pdf.cell(200, 10, txt="", ln=1, align="L")
def analyze_link():
	pdf.set_font("Arial", size=20)
	pdf.cell(100, 10, txt="ANALYSE DE LIENS MALVEILLANTS \n ", ln=1, align="L")
	pdf.set_font("Arial", size=12)
	pdf.cell(200, 10, txt="", ln=1, align="L")
	KEY="AIzaSyA8GTzrZmSOON8xL4mgX68nIe0efFOQUBU"
	# API Key pour utiliser Google Safe Browsing
	API_KEY = "AIzaSyA8GTzrZmSOON8xL4mgX68nIe0efFOQUBU"
	# Ouvrir le fichier PDF
	pdf_file = open(sys.argv[1], "rb")
	pdf_reader = PyPDF2.PdfFileReader(pdf_file)

	# Parcourir chaque page du PDF
	for page_num in range(pdf_reader.numPages):
    		page = pdf_reader.getPage(page_num)

    		# Extraire les liens de la page
    		links = page.get("/Annots", [])
    		for link in links:
        		link_obj = pdf_reader.getObject(link)
        		if "/A" in link_obj:
            			link_url = link_obj["/A"].get("/URI", None)
            			if link_url:
                			#Verifier si le lien est malveillant en utilisant Google Safe Browsing
                			try:
                	
                				s = SafeBrowsing(KEY)
                				r = s.lookup_urls([link_url])
                				# Analyser la réponse de l'API
                				if(r[link_url]['malicious']):
                					print(r)
                					pdf.cell(200, 10, txt=r, ln=1, align="L")
                			except(Exception):
                				print("une exeption a été levéé")
	# Fermer le fichier PDF
	pdf_file.close()
	
# Fonction pour obtenir la liste des processus en cours d'exécution
def get_process_list():
    process_list = []
    for proc in psutil.process_iter():
        try:
            process_list.append(proc.name())
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_list

def process_comp():
	pdf.set_font("Arial", size=20)
	pdf.cell(200, 10, txt="", ln=1, align="L")
	pdf.cell(200, 10, txt="ANALYSE DES PROCESSUS", ln=1, align="L")
	pdf.set_font("Arial", size=10)
	pdf.cell(200, 10, txt="", ln=1, align="L")
	print("**************ANALYSE DES PROCESSUS**********************")
	# Enregistrer la liste des processus en cours d'exécution avant d'ouvrir le fichier PDF
	before_process_list = get_process_list()

	# Ouvrir le fichier PDF
	pdf_file = open(sys.argv[1], "rb")
	pdf_reader = PyPDF2.PdfFileReader(pdf_file)

	# Attendre quelques secondes pour laisser le temps au logiciel d'affichage de PDF de se lancer
	time.sleep(5)

	# Enregistrer la liste des processus en cours d'exécution après l'ouverture du fichier PDF
	after_process_list = get_process_list()

	# Comparer les deux listes pour trouver les processus qui ont été lancés
	new_processes = set(after_process_list) - set(before_process_list)

	# Afficher les processus qui ont été lancés
	for process in new_processes:
	    pdf.cell(200, 10, txt=process, ln=1, align="L")
	    print("Processus lancé :", process)

	# Fermer le fichier PDF
	pdf_file.close()
	
def check_for_javascript():
    print("**************ANALYSE DU HEADERS**********************")
    
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 10, txt="", ln=1, align="L")
    pdf.cell(10, 10, txt="ANALYSE DES HEADERS", ln=1, align="L")
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="", ln=1, align="L")
    # Ouvrir le fichier PDF
    pdf_file = open(sys.argv[1], "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
   
    result = subprocess.run(["pdfid", sys.argv[1]], capture_output=True, text=True)
    output = result.stdout
    # Écriture du résultat dans un fichier
    with open("pdfid_output.txt", "w") as f:
    	f.write(output)
    pdf.multi_cell(100, 10, txt=output,align="L")
    tem=str(result)
   
    print(tem)
    #pdf.multi_cell(25, 10, txt=tem,align="L")

    # Fermer le fichier PDF
    pdf_file.close()

def analyze_embedded_objects():
    print("**************ANALYSE DES OBJETS EMBARQUEES**********************")
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 10, txt="", ln=1, align="L")
    pdf.cell(200, 10, txt="ANALYSE DES OBJETS EMBARQUEES", ln=1, align="L")
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="", ln=1, align="L")
    # Ouvrir le fichier PDF
    pdf_file = open(sys.argv[1], "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf.multi_cell(200, 10, txt=str(pdf_reader.resolvedObjects), align="L")
    print(pdf_reader.resolvedObjects)
    pdf_file.close()
    

def detect_vba():
	pdf.set_font("Arial", size=20)
	pdf.cell(200, 10, txt="", ln=1, align="L")
	pdf.multi_cell(200, 10, txt="ANALYSE DU VBA", align="L")
	pdf.set_font("Arial", size=10)
	pdf.cell(200, 10, txt="", ln=1, align="L")
	# Ouvrir le fichier PDF avec PyPDF
	pdf_file = open(sys.argv[1], "rb")
	pdf_reader = PyPDF2.PdfFileReader(pdf_file)
	# Extraire le cotenu du PDF
	content = sys.argv[1]+" "
	for page in range(pdf_reader.getNumPages()):
            content += pdf_reader.getPage(page).extractText()
            f=open("newtext.txt","w")
            f.write(content)
	pdf_file.close()
        
	# Utiliser oletools pour analyser le contenu et détecter les macros VBA
	vba_parser = olevba.VBA_Parser("newtext.txt")
	if vba_parser.detect_vba_macros():
            print("Macros VBA détectées dans le fichier " + sys.argv[1])
            #pdf.cell(200, 10, txt="Macros VBA détectées dans le fichier" , ln=1, align="L")
            for (subfilename, stream_path, vba_filename, vba_code) in vba_parser.extract_macros():
                if 'VBA' in vba_code:
                	pdf.cell(200, 10, txt=vba_filename , ln=1, align="L")
                	print(" - " + vba_filename)
                else:
                	print("Aucune macro VBA n'a été détectée dans le fichier " + sys.argv[1])
                	pdf.cell(200, 10, txt="Aucune macro VBA n'a été détectée dans le fichier" , ln=1, align="L")

	f.close()
        
if sys.argv[1]=='':
	print ("entrer un nom de PDF pour l'analyser")
else:
	process_comp()
	analyze_link()
	analyze_embedded_objects()
	check_for_javascript()
	detect_vba()
	nnomf=sys.argv[1]
	nnomf=nnomf.replace("./PDFA/","")
	nomf="./PDFR/Rapport-"+nnomf
	pdf.output(nomf)


