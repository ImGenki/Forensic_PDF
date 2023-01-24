import PyPDF2
import requests
import sys
from pysafebrowsing import SafeBrowsing
import psutil
import time
import oletools.olevba as olevba

def analyze_link():
	print("**************ANALYSE DES LIENS**********************")
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
	    print("Processus lancé :", process)

	# Fermer le fichier PDF
	pdf_file.close()
	
def check_for_javascript():
    print("**************ANALYSE DU JS**********************")
    # Ouvrir le fichier PDF
    pdf_file = open(sys.argv[1], "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Vérifier si le fichier contient des actions JavaScript
    if '/JS' in pdf_reader.trailer["/Root"]:
        print("Le fichier {file_name} contient du JScript")
    else:
        print("Le fichier {file_name} ne contient pas de JScript")
    if '/JavaScript' in pdf_reader.trailer["/Root"]:
        print("Le fichier {file_name} contient du JavaScript")
    else:
        print("Le fichier {file_name} ne contient pas de JavaScript")
    if '/Action' in pdf_reader.trailer["/Root"]:
        print("Le fichier {file_name} contient du balise action")
    else:
        print("Le fichier {file_name} ne contient Action")
    if '/AA' in pdf_reader.trailer["/Root"]:
        print("Le fichier {file_name} contient AA")
    else:
        print("Le fichier {file_name} ne contient pas AA")
    if '/OpenAction' in pdf_reader.trailer["/Root"]:
        print("Le fichier {file_name} contient OpenAction")
    else:
        print("Le fichier {file_name} ne contient pas OpenAction")

    # Fermer le fichier PDF
    pdf_file.close()

def analyze_embedded_objects():
    print("**************ANALYSE DES OBJETS EMBARQUEES**********************")
    # Ouvrir le fichier PDF
    pdf_file = open(sys.argv[1], "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    print(pdf_reader.resolvedObjects)
    pdf_file.close()
    

def detect_vba():
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
            for (subfilename, stream_path, vba_filename, vba_code) in vba_parser.extract_macros():
                if 'VBA' in vba_code:
                	print(" - " + vba_filename)
                else:
                	print("Aucune macro VBA n'a été détectée dans le fichier " + sys.argv[1])

        f.close()
        
if sys.argv[1]=='':
	print ("entrer un nom de PDF pour l'analyser")
else:
	process_comp()
	analyze_link()
	analyze_embedded_objects()
	check_for_javascript()
	detect_vba()


