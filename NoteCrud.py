import datetime
from datetime import datetime
import fnmatch
import os

def list(filter = ""):
    print('Список заметок:');
    listOfFiles = os.listdir(".")
    pattern = "*.csv"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            #print(entry);
            file = open(entry, "r")
            content = file.read()
            file.close()
            #print("content:", content)
            parts = content.split(";")
            #print("parts:", parts)
            head = parts[0]

            if not filter:
                print(entry[0:-4], head)
            else:
                #Обработка исключения при преобразовании строки фильтра в дату       
                filter_as_datetime_obj = 0
                try:
                    filter_as_datetime_obj = datetime.strptime(filter, '%Y-%m-%d')
                except:
                    print("Неверный формат введённой в качестве фильтра даты!")
                    return
                #Обработка исключения при преобразовании строки из Заметки в дату
                date_time_obj = 0
                try:
                    date_time_obj = datetime.strptime(parts[1][0:10], '%Y-%m-%d')
                except:
                    print("Неверный формат даты в заметке ", entry)
                    return
                
                # print(parts[1][0:10])
                # print(filter_as_datetime_obj)
                # print(date_time_obj)
                if filter_as_datetime_obj == date_time_obj:
                    print(entry[0:-4], head)
            

def create(head, body):
    print("head: ", head)
    print("body: ", body)
    current_datetime = datetime.now()
    # print("текущее время:", current_datetime)
    id = current_datetime.strftime("%Y%m%d%H%M%S")
    date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    filename = id + '.csv'
    file = open(filename, "w")
    file.write(head + ';')
    file.write(date + ';')
    file.write(body + ';')
    file.close()
    
def read(id):
    file = open(id + ".csv", "r")
    content = file.read()
    file.close()
    parts = content.split(";")
    head = parts[0]
    body = parts[2]
    print("Заметка №", id)
    print("Заголовок", head)
    print("Содержание ", body) 

def update(id, head, body):
    file = open(id + ".csv", "w")
    file.write(head + ';')
    file.write(body + ';')
    file.close()
    print(f"Заметка № {id} обновлена");

def delete(id):
    os.remove(id + ".csv")
    print(f"Заметка № {id} удалена ")
