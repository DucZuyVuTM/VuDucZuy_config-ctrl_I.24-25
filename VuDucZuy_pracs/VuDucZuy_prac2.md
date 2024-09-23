## Задача 1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета.

```bash
git clone https://github.com/matplotlib/matplotlib.git
```
![Screenshot 2024-09-23 093130](https://github.com/user-attachments/assets/c04ede33-b5af-4d25-b026-8aa13a913e2b)

```bash
pip show matplotlib
```
![Screenshot 2024-09-23 095020](https://github.com/user-attachments/assets/2cbb1802-ed15-4fd8-b62a-0efb9f818e86)

## Задача 2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета.

```bash
git clone https://github.com/expressjs/express.git
```
![Screenshot 2024-09-23 095304](https://github.com/user-attachments/assets/d143b7d3-353b-4e59-94f8-f835a322abef)

```bash
npm info express
```
![Screenshot 2024-09-23 095732](https://github.com/user-attachments/assets/12882f79-fe27-4174-bcc0-9ac77b670c7f)
![Screenshot 2024-09-23 095759](https://github.com/user-attachments/assets/f4d91e24-75ca-4a3f-88d0-fb35648bfab3)

## Задача 3
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

```bash
echo 'digraph G { node [shape=box]; matplotlib [label="matplotlib"]; numpy [label="numpy"]; pillow [label="pillow"]; cycler [label="cycler"]; matplotlib -> numpy; matplotlib -> pillow; matplotlib -> cycler; }' > matplotlib.dot
echo 'digraph G { node [shape=box]; express [label="express"]; accepts [label="accepts"]; array_flatten [label="array-flatten"]; content_type [label="content-type"]; express -> accepts; express -> array_flatten; express -> content_type; }' > express.dot
dot -Tpng matplotlib.dot -o matplotlib.png
fim matplotlib.png
dot -Tpng express.dot -o matplotlib.png
fim matplotlib.png

```
![Screenshot 2024-09-23 100537](https://github.com/user-attachments/assets/c95bb8b3-6694-459a-8eef-500eb25c6ea7)
![Screenshot 2024-09-23 100351](https://github.com/user-attachments/assets/4ee3545b-5667-42cd-8cce-0481cd96e831)

## Задача 4
