documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2', '5455 028765'],
  '2': ['10006'],
  '3': []
}


def main():
  while True:
    user_input = input('Введите команду: ').lower()
    if user_input == 'p':
      person(documents)
    elif user_input == 's':
      shelf(directories)
    elif user_input == 'l':
      documents_list(documents)
    elif user_input == 'd':
      delete(documents, directories)
    elif user_input == 'a':
      add_document(documents, directories)
    elif user_input == 'd':
      delete(documents, directories)
    elif user_input == 'as':
      add_shelf(directories)
    elif user_input == 'q':
      break

# def check_number(directories):
#   '''
#   проверка ввода - запрашивает номер документа, до тех пор когда не будет введён номер существующего документа
#   '''
  

#   # for shelf, doc in directories.items():
#   #   if user_input_number in doc:
#   #     return user_input_number

#   while user_input_number not in list(directories.values()):
#     user_input_number = input('Документа с таким номером не существует!\nНомер документа: ')
#   return user_input_number
      
# def check_shelf(directories):
#   '''
#   проверка ввода - запрашивает номер полки, до тех пор когда не будет введён номер существующей полки
#   '''
#   user_input_shelf = input('Номер полки: ')

#   for shelf in directories.keys():
#     if user_input_shelf in shelf:
#       return user_input_shelf

#   while user_input_shelf not in shelf:
#     user_input_shelf = input('Полки с таким номером не существует!\nНомер полки: ')

def person(data_base):
  '''
  p – people – команда, которая спросит номер документа
   и выведет имя человека, которому он принадлежит
  '''  
  user_input = input('Номер документа: ')
  for client in data_base:
    if client['number'] == user_input:
      print(client['name'])

def shelf(directories):
  '''
  s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
  '''
  user_input_number = input('Номер полки: ')
  for key, value in directories.items():
    # print(value)
    if user_input_number in value:
      print(f'Документа находится на полке №{key}')
      break
  else:
    print('Такого документа нет')

def documents_list(documents):
  '''
  l– list – команда, которая выведет список всех документов
   в формате passport "2207 876234" "Василий Гупкин";
  '''
  for client in documents:
    print(f'{client["type"]} "{client["number"]}" "{client["name"]}"')

def add_document(documents, directories):
    '''
    a – add – команда, которая добавит новый документ
    в каталог и в перечень полок, спросив его номер,
    тип, имя владельца и номер полки, на котором
    он будет храниться. Корректно обработайте ситуацию,
    когда пользователь будет пытаться добавить документ
    на несуществующую полку.
    '''
    user_input_type = input('Тип документа: ')
    user_input_number = input('Номер документа: ')
    user_input_name = input('Имя и Фамилия: ')
    

    new_client = {"type": user_input_type, 
    "number": user_input_number, "name": user_input_name}
    
    documents.append(new_client)

    user_input_shelf = input('Номер полки: ')

    while user_input_shelf not in directories.keys():
        user_input_shelf = input('Полки с таким номером не существует! \nВведите номер полки: ')
    
    directories[user_input_shelf].append(user_input_number)

    print('Документ добавлен!')

def delete(documents, directories):
  '''
  d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ
   '''
  user_input_number = input('Номер документа: ')



  for key, value in directories.items():
    if user_input_number in value:
      value.remove(user_input_number)
    else:
      pass

  for client in documents:
    if user_input_number == client['number']:
      documents.remove(client)

def add_shelf(directories):
  user_input_shelf = input('Номер новой полки: ')

  while user_input_shelf in directories.keys():
    user_input_shelf = input('Полка с таким номером уже существует! \nВведите другой номер: ')

  directories.setdefault(user_input_shelf, [])

def move():
  '''
  m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
  '''
  

main()

print(directories)
print(documents)