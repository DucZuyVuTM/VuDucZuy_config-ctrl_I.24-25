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


```mzn
include "globals.mzn";  % Thêm dòng này để sử dụng hàm all_different

% 1. Định nghĩa biến cho 6 chữ số (mỗi chữ số nằm trong khoảng từ 0 đến 9)
array[1..6] of var 0..9: digits;

% 2. Đặt ràng buộc: Tất cả các chữ số phải khác nhau
constraint all_different(digits);

% 3. Đặt ràng buộc: Tổng của 3 chữ số đầu tiên phải bằng tổng của 3 chữ số cuối cùng
constraint digits[1] + digits[2] + digits[3] = digits[4] + digits[5] + digits[6];

% 4. Tối ưu hóa: Tìm tổng của 3 chữ số đầu tiên là nhỏ nhất
solve minimize digits[1] + digits[2] + digits[3];

% 5. Hiển thị kết quả
output ["Các chữ số của vé số: \(digits)\n"];

```
![Screenshot 2024-09-23 140555](https://github.com/user-attachments/assets/d2620166-085b-4df6-829a-fe37f4f8d322)
