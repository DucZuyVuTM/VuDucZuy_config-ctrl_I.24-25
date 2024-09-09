## Задача 1
```bash
cut –d: -f1 /etc/passwd | sort
```
![Screenshot 2024-09-02 164331](https://github.com/user-attachments/assets/3542cffe-5c7b-4bfe-b1e6-55902c64ef3a)

## Задача 2
```bash
cat /etc/protocols | awk ‘{print $2, $1}’ | sort –nr head –n 5
```
![Screenshot 2024-09-02 165248](https://github.com/user-attachments/assets/e4ad7a92-ebb9-4ed4-90a3-7a578b1209ea)

## Задача 3

```bash
#!/bin/bash

msg="$1"
length=${#msg}
border=$(printf "+%$((length + 2))s+" | tr ' ' '-')

echo "$border"
echo "| $msg |"
echo "$border"

```
![Screenshot 2024-09-03 155717](https://github.com/user-attachments/assets/d2d74ca3-4c3d-4a84-9784-be48a8fb579f)

## Задача 4

```bash
grep -o ‘\b[a-zA-Z0-9_]*\b’ hello.c | sort | uniq
```
![Screenshot 2024-09-03 153025](https://github.com/user-attachments/assets/a45a3c6b-f262-4ff7-bd7a-26f346a43793)

## Задача 5

```bash
#!/bin/bash
chmod +x "$1"
sudo cp "$1" /usr/local/bin/
```
![Screenshot 2024-09-03 160047](https://github.com/user-attachments/assets/302d9635-2d4c-4d37-b176-be154f6ed910)

## Задача 6

```bash
#!/bin/bash

for file in "$@"; do
    if [[ "$file" =~ \.(c|js)$ ]]; then
        first_line=$(head -n 1 "$file") 
        if [[ "$first_line" =~ ^// ]]; then
            echo "$file has a comment in the first line."
        else
            echo "$file does not have a comment in the first line."
        fi
    elif [[ "$file" =~ \.py$ ]]; then 
        first_line=$(head -n 1 "$file")
        if [ "$first_line" =~ ^# ]]; then
            echo "$file has a comment in the first line."
        else
            echo "$file does not have a comment in the first line."
        fi
    fi
done

```
![Screenshot 2024-09-03 163537](https://github.com/user-attachments/assets/b936cc22-167b-476f-805b-06193e92c357)

## Задача 7

```bash
#!/bin/bash

find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -d
```
![Screenshot 2024-09-09 185656](https://github.com/user-attachments/assets/4e629506-252d-49e6-b2c2-49a4dbc5d579)

## Задача 8

```bash
#!/bin/bash

find . -name "*.$1" -print0 | xargs -0 tar -czvf archive.tar.gz
```
![Screenshot 2024-09-03 172537](https://github.com/user-attachments/assets/85ed2821-6e49-422d-baad-a2294ad7d35d)

## Задача 9

```bash
#!/bin/bash

sed 's/    /\t/g' "$1" > "$2"
```
![Screenshot 2024-09-09 191829](https://github.com/user-attachments/assets/fba3ebd2-3f7b-470a-bd97-615ff5cd64ba)
![Screenshot 2024-09-09 191812](https://github.com/user-attachments/assets/5e9e37ff-e227-4da7-b0d9-e0e9f9c93138)
![Screenshot 2024-09-09 191847](https://github.com/user-attachments/assets/7b729000-9efe-4ade-91ad-e987bd822f2b)

## Задача 10

```bash
#!/bin/bash

find "$1" -type f -name "*.txt" -exec test ! -s {} \; -print
```
![Screenshot 2024-09-03 174123 (1)](https://github.com/user-attachments/assets/707a779a-5e4d-476b-8dd4-f5e944325f67)
