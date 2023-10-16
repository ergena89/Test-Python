import datetime
from datetime import datetime
import fnmatch
import os

def list():
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
    
# 20231016230000
# 20231016230000.csv
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

def update():
    print('');

def delete():
    print('');
