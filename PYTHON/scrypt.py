import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook
from docx import Document
import mysql.connector
import csv
import sqlite3
import datetime
# create an instance of the webdriver (in this example, we are using Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# navigate to the webpage
url = "http://consulta.siiau.udg.mx/wco/sspseca.forma_consulta"
driver.get(url)
time.sleep(1)
select_element = Select(driver.find_element(By.ID,"cicloID"))
# select_element.select_by_value("option_value")
select_element.select_by_visible_text("202310 - Calendario 23 A")
select_element = driver.find_element(By.NAME,"cup")
# create a Select object and select an option by its name
select = Select(select_element)
select.select_by_visible_text("D - C.U. DE CS. EXACTAS E ING.")
# # select the button element
button =  driver.find_element(By.ID, 'idConsultar')
# # click the button
button.click()
time.sleep(1)
rows = []
def getDataTable():

    table_elements = driver.find_elements(By.TAG_NAME,'table')
    # Iterate over the table elements to find the unique table
    print(len(table_elements))
    for table_element in table_elements:
        # Extract the HTML content of the table
        table_html = table_element.get_attribute('outerHTML')
        soup = BeautifulSoup(table_html, 'html.parser')
        
        # Find the tbody element by its position relative to other elements in the table
        tbody_element = soup.find_all('table')[0] # Replace the index with the position of the tbody element relative to other elements in the table
        # Check if the table is unique by counting the number of tbody elements
        # if len(soup.find_all('tbody')) == 1:
        # Create a pandas DataFrame from the table data

        
        i = 0
        for row in tbody_element.find_all('tr'):
            i+=1
            if i<=2:
                continue
            cells = []
            optimized = row.find_all('td', class_='tddatos')
            Ses = ''
            Prof = '' 
            for j,cell in enumerate(optimized):
                if j == len(optimized) - 1:
                    for row1 in cell.find_all('tr'):
                        for i1,cell1 in enumerate(row1.find_all('td')):
                            if i1 == 0:
                                Ses = cell1.text
                            else:
                                Prof = cell1.text
                            #cells.append(cell1.text)
                    break
                cells.append(cell.text)
            tab1 = row.find_all('table', class_='td1')
            soup1 = BeautifulSoup(str(tab1), 'html.parser')
            tab1R = soup1.find_all('tr')
            yep = False
            c = 0 
            for j,row1 in enumerate(tab1R):
                if j == 1 and yep == True:
                    for i1 in range(8):
                        cells.pop()
                else:
                 if yep == False and j==1:
                    for i1 in range(c):
                        cells.pop()
                c = 0
                yep = False
                for cell1 in row1.find_all('td'):
                    if cell1.string is not None and cell1.string.strip() == '':
                        # print("Columns error",str(c))
                        yep = False
                        break
                    c += 1
                    cells.append(cell1.text)
                    yep = True
                if yep and c==6:
                    cells.append(Ses)
                    cells.append(Prof)
                    #print(cells)
                    rows.append(cells.copy())
        # df = pd.DataFrame(rows)

        #     # Save the DataFrame to an Excel file
        # df.to_excel('table.xlsx', index=False)
        

        # Save the DataFrame to a CSV file
        
            # Exit the loop after finding the unique table
        break

def insertData():
    ctn = mysql.connector.connect(
            host = 'localhost',
            user='username',
            password='password',
            database='SIIAU2'
        ) 
    sql = ctn.cursor()
    # INSERT INTO Profesor(ID, Nombre) VALUES(3,'Juan')
    sentenceProfesor = """INSERT INTO Profesor
                          (ID, Nombre) 
                          VALUES (%s, %s)"""
    sentenceCurso = """INSERT INTO Curso
                       (NRC,Clave, Materia, Sec, CR, CUP, DIS) 
                       VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    sentenceEdificio = """INSERT INTO Edificio
                         (ID,Nombre) 
                         VALUES(%s,%s)"""
    sentenceAula = """INSERT INTO Aula
                          (ID,Nombre,Edificio_ID) 
                          VALUES (%s,%s,%s)"""
    sentenceHorario = """INSERT INTO Horario
                          (ID,Dia,Hora_inicio,Hora_fin) 
                          VALUES (%s,%s,%s,%s)"""
    sentenceCursoHorario = """INSERT INTO Curso_Horario
                          (Curso_Clave,Horario_ID,Aula_ID) 
                          VALUES (%s,%s,%s)"""
    sentenceCursoProfesor = """INSERT INTO Curso_Profesor
                          (Curso_Clave,Profesor_ID) 
                          VALUES (%s,%s)"""
    
    insertsProfesor = []
    insertHorario = []
    insertEdificio = []
    insertCursoProfesor = []
    insertCursoHorario = []
    insertCurso = []
    insertAula=[]
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header row
        next(reader)
        # Iterate over the remaining rows and insert them into the database
        
        for i,row in enumerate(reader):
            #print(i)
            enc=False
            for reg in insertsProfesor:
                if reg[1] == row[14]:
                    enc=True
                    break
            if not enc:
                insertsProfesor.append((i,row[14]))
            day = row[9].replace('.', '').replace(' ', '')
            Edif = row[10]
            NRC = row[0]+day+Edif+row[11]
            insertCurso.append((NRC,row[1],row[2],row[3],row[4],row[5],row[6]))
            enc=False
            for reg in insertEdificio:
                if reg[1] == Edif:
                    enc=True
                    break
            if not enc:
                insertEdificio.append((i,Edif))
            tim = row[8]
            start, end = tim.split("-")
            startO = datetime.datetime.strptime(start, "%H%M").time()
            endO = datetime.datetime.strptime(end, "%H%M").time()

            startS = startO.strftime("%H:%M:%S")
            endS = endO.strftime("%H:%M:%S")

            #print(startS)
            #print(endS) 
            enc=False
            for reg in insertHorario:
                if reg[1] == day and reg[2] == startS and reg[3] == endS:
                    enc=True
                    break
            if not enc:
                insertHorario.append((i,day,startS,endS))
        #Adding Aula
        print("***********************************************************************************************************************************")
        print(sql.rowcount," inserted")
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for i2,row2 in enumerate(reader):
            idEdificio = ''
            for reg in insertEdificio:
                if reg[1] == row2[10]:
                    idEdificio = reg[0]
                    break
            enc =False
            for reg1 in insertAula:
                print(row2[11]," - ",reg1[1])
                if row2[11] == reg1[1] and reg1[2] == idEdificio:
                    enc= True
            if not enc:
                insertAula.append((i2,row2[11],idEdificio))
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for i2,row2 in enumerate(reader):
            day = row2[9].replace('.', '').replace(' ', '')
            Edif = row2[10]
            NRC = row2[0]+day+Edif+row2[11]#THis is cursso_clave
            teachID=''
            for reg in insertsProfesor:
                if reg[1] == row2[14]:
                    teachID = reg[0]
                    break
            insertCursoProfesor.append((NRC,teachID))
            #GET ID HORARIO
            tim = row2[8]
            start, end = tim.split("-")
            startO = datetime.datetime.strptime(start, "%H%M").time()
            endO = datetime.datetime.strptime(end, "%H%M").time()
            startS = startO.strftime("%H:%M:%S")
            endS = endO.strftime("%H:%M:%S")
            IDHor = ''#This is the idHorario
            for reg in insertHorario:
                if reg[1] == day and startS == reg[2] and endS == reg[3]:
                    IDHor = reg[0]
                    break
            #Getting Haula_ID
            AulaID = ''
            for reg in insertAula:
                if reg[1] == row2[11]:
                    for reg2 in insertEdificio:
                        if row[10] == reg2[1]:
                            AulaID = reg[0]
                            break
                if len(str(AulaID)+"") > 0:
                    break
            insertCursoHorario.append((NRC,IDHor,AulaID))
    sql.executemany(sentenceProfesor,insertsProfesor)
    sql.executemany(sentenceCurso,insertCurso)
    sql.executemany(sentenceEdificio,insertEdificio)
    sql.executemany(sentenceAula,insertAula)
    sql.executemany(sentenceHorario,insertHorario)
    sql.executemany(sentenceCursoHorario,insertCursoHorario)
    sql.executemany(sentenceCursoProfesor,insertCursoProfesor)

    ctn.commit()

    sql.close()

getDataTable()
df = pd.DataFrame(rows)
df.to_csv('data.csv', index=False)
insertData()
time.sleep(1)


driver.quit()