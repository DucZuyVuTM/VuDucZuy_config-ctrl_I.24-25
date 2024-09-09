## Задача 1
```bash
cut –d: -f1 /etc/passwd | sort
```
![Screenshot 2024-09-02 164331](https://github.com/user-attachments/assets/3542cffe-5c7b-4bfe-b1e6-55902c64ef3a)


## Задача 2
```bash
cat /etc/protocols | awk ‘{print $2, $1}’ | sort –nr head –n 5
```

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
## Задача 4

```bash
grep -o ‘\b[a-zA-Z0-9_]*\b’ hello.c | sort | uniq
```


## Задача 5

```bash
#!/bin/bash
chmod +x "$1"
sudo cp "$1" /usr/local/bin/

```

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

## Задача 7

```bash
find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -d
```

## Задача 8

```bash
#!/bin/bash

find . -name "*.$1" -print0 | xargs -0 tar -czvf archive.tar.gz
```

## Задача 9

```bash
#!/bin/bash

sed 's/ /\t/g' "$1" > "$2"
```

## Задача 10

```bash
#!/bin/bash

find "$1" -type f -name "*.txt" -exec test ! -s {} \; -print
```
