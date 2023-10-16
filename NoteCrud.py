from datetime import datetime

def list():
    print('Список заметок');

def create(head, body):
    print("head: ", head)
    print("body: ", body)
    current_datetime = datetime.now()
    # print("текущее время:", current_datetime)
    id = current_datetime.strftime("%Y%m%d%H%M%S")
    filename = id + '.csv'
    file = open(filename, "w")
    file.write(head + ';')
    file.write(id + ';')
    file.write(body + ';')
    file.close()
    
# 20231016230000
# 20231016230000.csv
def read():
    print('');

def update():
    print('');

def delete():
    print('');
