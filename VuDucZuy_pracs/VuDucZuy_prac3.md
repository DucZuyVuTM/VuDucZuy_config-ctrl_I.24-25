# Задача №1

Создадим файл Ex1.jsonnet и запишем в него следующий код:
```
local Group(digits) = 'ИКБО-' + digits;

local groups = [
  Group(i + '-20')
  for i in std.range(1, 24)
] + [
  Group('10-23'),
];

local Student(age, groupId, name) = {
  age: age,
  group: groups[groupId],
  name: name,
};

{
  groups: groups,
  students: [
    Student(19, 3, 'Сидиков Н.А.'),
    Student(18, 4, 'Петров В.П.'),
    Student(18, 4, 'Иванов А.С.'),
    Student(19, std.length(groups) - 1, 'Путин В.В.'),
  ],
  subject: 'Конфигурационное управление',
}
```

Первым делом установим Jsonnet с помощью команды, приведенной ниже:
```bash
pacman -S mingw-w64-x86_64-python-jsonnet
```

Далее создадим файл Ex1.jsonnet, запишем в него код из задания. Далее скомпилируем этот файл в Json:
```bash
jsonnet Ex1.jsonnet -o Ex1jn.json
```

Содержимое файла json (Ex1.json):

![circular-linked-list](https://github.com/user-attachments/assets/27384466-6dd5-4f23-bedf-b7a4785e6195)

# Задача №2

Создадим файл Ex2.dhall и запишем в него следующий код:
```
let List = https://prelude.dhall-lang.org/v23.0.0/List
let Text = https://prelude.dhall-lang.org/v23.0.0/Text
let Natural = https://prelude.dhall-lang.org/v23.0.0/Natural

let Group = \(i : Natural) -> "ИКБО-" ++ Natural/show i ++ "-20"

let groups =
      List/map Natural Text (\(i : Natural) -> Group i) (Natural/enumerate 24)

let Student = \(age : Natural) -> \(group : Text) -> \(name : Text) -> { age, group, name }

let students = [
      Student 19 "ИКБО-4-20" "Иванов И.И.",
      Student 18 "ИКБО-5-20" "Петров П.П.",
      Student 18 "ИКБО-5-20" "Сидоров С.С.",
      Student 20 "ИКБО-6-20" "Новиков А.А." -- (bạn có thể thêm thông tin học sinh thứ 4 ở đây)
]

let subject = "Конфигурационное управление"

in { groups, students, subject }
```

Установим Dhall с помощью команды, приведенной ниже:
```bash
sudo apt install dhall
```

Скомпилируем файл в файл "json":
```bash
dhall --output json --file Ex2.dhall
```

Создадим файл convert.py и запишем в него следующий код:
```
import re

def convert_dhall_to_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Thêm dấu ngoặc kép cho các khóa (keys)
    content = re.sub(r'(\b[a-zA-Z_][a-zA-Z0-9_]*\b)\s*=', r'"\1":', content)

    # Định dạng lại dấu ngoặc cho JSON
    content = content.replace('=', ':').replace('Some ', '')

    # Ghi ra file mới
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

# File input và output
input_file = 'json'  # File gốc
output_file = 'Ex2.json'  # File JSON mới

# Chuyển đổi
convert_dhall_to_json(input_file, output_file)
print(f"File đã được chuyển đổi và lưu tại {output_file}")
```

Наконец просто запустить эту Python программу:

![image](https://github.com/user-attachments/assets/a372fe2d-8ad7-44fa-b49f-dcad4b64d4b0)

Содержимое файла Ex2.json:

![pr3-ex2-json](https://github.com/user-attachments/assets/091045cb-6e33-4564-aef6-0252a72023ee)

# Задача №3

Создадим файл Ex3.py и реализуем в нем грамматику языка нулей и единиц:
```
import random

def parse_bnf(text):
    '''
    Chuyển đổi văn bản BNF thành một cấu trúc ngữ pháp Python (từ điển).
    '''
    grammar = {}
    rules = [line.split('::=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.strip().split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Tạo ngẫu nhiên một chuỗi nhị phân dựa trên ngữ pháp.
    '''
    if start in grammar:
        sequence = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, token) for token in sequence)
    return start


# Ngữ pháp BNF
BNF = '''
<start> ::= <binary>
<binary> ::= "0" | "1" | "10" | "11" | "100" | "101101" | "000"
'''

# Phân tích cú pháp BNF
grammar = parse_bnf(BNF)

# Tạo 10 chuỗi nhị phân ngẫu nhiên
for _ in range(10):
    print(generate_phrase(grammar, '<start>'))
```

Результат запуска:

![image](https://github.com/user-attachments/assets/73fcdc8a-82ab-4a5d-a802-29c4164e49d8)

# Задача №4

Создадим файл Ex4.py и реализуем в нем грамматику языка правильно расставленных скобок двух видов:
```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


# Грамматика языка правильно расставленных скобок
BNF = """
E = P E | F E | P | F 
P = ( P ) | ( ) 
F = { F } | {}
"""

if __name__ == "__main__":
    # Генерация 10 случайных строк из грамматики
    for i in range(10):
        print(generate_phrase(parse_bnf(BNF), 'E'))
```

Результат запуска:

![image](https://github.com/user-attachments/assets/486123ee-21e5-4e96-b85e-755f1537f918)

# Задача №5

Создадим файл Ex5.py и реализуем в нем грамматику языка выражений алгебры логики:
```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start, max_depth=10, current_depth=0):
    '''
    Сгенерировать случайную фразу с ограничением по глубине рекурсии.
    '''
    if current_depth > max_depth:
        return ""
    # Если start - это правило в грамматике
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name, max_depth, current_depth + 1) for name in seq)
    # Если start - это переменная (не правило), возвращаем её как строку
    return str(start)


# Грамматика языка алгебры логики
BNF = '''
E = L | E & L | E | E | E
L = x | y | ( E ) | ~ L | ( E ) | ~ L
'''

if __name__ == "__main__":
    # Генерация 10 случайных логических выражений
    for i in range(10):
        print(generate_phrase(parse_bnf(BNF), 'E'))
```

Результат запуска:

![image](https://github.com/user-attachments/assets/49e78f96-0d38-4db4-a10e-616f02ed4334)
