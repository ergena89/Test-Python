import sys
import NoteCrud as notes


if len(sys.argv) > 1:
    for arg in range(1, len(sys.argv)):
        print(sys.argv[arg])
        if sys.argv[arg] == "list":
            if len(sys.argv) == 2:
                notes.list()
            elif len(sys.argv) == 3:
                filter = sys.argv[2]
                notes.list(filter)                
            else:
                print("Для команды list можно указать 1 аргумент (дату) или не указывать вообще")
            break            
        elif sys.argv[arg] == "create":
            if len(sys.argv) < 4:
                print("Для создания заметки ввести: заголовок, тело заметки.")
            else:
                notes.create(sys.argv[2], sys.argv[3])
            break
        elif sys.argv[arg] == "read":
            if len(sys.argv) < 3:
                print("Для чтения заметки, необходимо указать id")
            else:
                notes.read(sys.argv[2])
            break

        elif sys.argv[arg] == "update":
            if len(sys.argv) < 5:
                print("Для изменения заметки, необходимо указать id, заголовок, тело заметки")
            else:
                notes.update(sys.argv[2], sys.argv[3], sys.argv[4])
            break

        elif sys.argv[arg] == "delete":
            if len(sys.argv) < 3:
                print("Для удаления заметки, необходимо указать id")
            else:
                notes.delete(sys.argv[2])
            break
        else:
            print(" other command then list was send")

actions = ["list", "create", "read", "update", "delete"]