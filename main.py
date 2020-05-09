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
      shelf()
    elif user_input == 'l':
      documents_list()
    elif user_input == 'a':
      add_document()
    elif user_input() == 'q':
      break

def person(data_base):
  '''
  p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
  '''  
  user_input = input('Номер документа: ')
  for client in data_base:
    if client['number'] == user_input:
      print(client['name'])

def shelf():
  '''
  s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
  Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ
'''

def documents_list():
  '''
  l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
  '''


def add_document():
  '''
  a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
  '''

main()