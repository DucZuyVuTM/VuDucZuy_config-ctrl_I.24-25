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
Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными. Найти минимальное решение для суммы 3 цифр.

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
![Screenshot 2024-09-23 170610](https://github.com/user-attachments/assets/8d637db8-d660-4bfa-845d-e7868be27161)

## Задача 5
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного в постановке задачи.

```mzn
include "globals.mzn";

% 1. Định nghĩa các phiên bản của các gói
enum Versions_menu = {m1_0_0, m1_1_0, m1_2_0, m1_3_0, m1_4_0, m1_5_0};
enum Versions_dropdown = {d1_8_0, d2_0_0, d2_1_0, d2_2_0, d2_3_0};
enum Versions_icons = {i1_0_0, i2_0_0};
enum Versions_root = {r1_0_0};

% 2. Khai báo biến cho mỗi gói phần mềm
var Versions_menu: menu_version;
var Versions_dropdown: dropdown_version;
var Versions_icons: icons_version;
var Versions_root: root_version;

% 3. Thiết lập các ràng buộc phụ thuộc
% Ràng buộc giữa root và menu
constraint
  root_version == r1_0_0 -> menu_version == m1_5_0;

% Ràng buộc giữa menu và dropdown
constraint
  (menu_version == m1_5_0 -> dropdown_version == d2_3_0) /\
  (menu_version == m1_4_0 -> dropdown_version == d2_2_0) /\
  (menu_version == m1_3_0 -> dropdown_version == d2_1_0) /\
  (menu_version == m1_2_0 -> dropdown_version == d2_0_0) /\
  (menu_version == m1_1_0 -> dropdown_version == d2_0_0) /\
  (menu_version == m1_0_0 -> dropdown_version == d1_8_0);

% Ràng buộc giữa dropdown và icons
constraint
  dropdown_version == d2_3_0 -> icons_version == i2_0_0;

% 4. Tối ưu hóa hoặc giải pháp
solve satisfy;

% 5. Hiển thị kết quả
output ["menu version: ", show(menu_version), "\ndropdown version: ", show(dropdown_version), "\nicons version: ", show(icons_version)];

```
![Screenshot 2024-09-23 181146](https://github.com/user-attachments/assets/0b0d9783-e244-4352-9daf-697a76898191)

## Задача 6
Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```

Решение:

```
include "globals.mzn";

% 1. Định nghĩa các phiên bản của các gói
enum Versions_root = {root_1_0_0};
enum Versions_foo = {foo_1_0_0, foo_1_1_0};
enum Versions_left = {left_1_0_0};
enum Versions_right = {right_1_0_0};
enum Versions_shared = {shared_1_0_0, shared_2_0_0};
enum Versions_target = {target_1_0_0, target_2_0_0};

% 2. Khai báo biến cho mỗi gói phần mềm
var Versions_root: root_version;
var Versions_foo: foo_version;
var Versions_left: left_version;
var Versions_right: right_version;
var Versions_shared: shared_version;
var Versions_target: target_version;

% 3. Thiết lập các ràng buộc phụ thuộc
% Ràng buộc giữa root và foo
constraint
  (root_version == root_1_0_0 -> foo_version in {foo_1_0_0, foo_1_1_0}) /\
  (root_version == root_1_0_0 -> target_version == target_2_0_0);

% Ràng buộc giữa foo và left, right
constraint
  (foo_version == foo_1_1_0 -> left_version == left_1_0_0) /\
  (foo_version == foo_1_1_0 -> right_version == right_1_0_0);

% Ràng buộc giữa left và shared
constraint
  (left_version == left_1_0_0 -> shared_version in {shared_1_0_0, shared_2_0_0});

% Ràng buộc giữa right và shared
constraint
  (right_version == right_1_0_0 -> shared_version == shared_1_0_0);

% Ràng buộc giữa shared và target
constraint
  (shared_version == shared_1_0_0 -> target_version in {target_1_0_0, target_2_0_0});

% 4. Tối ưu hóa hoặc giải pháp
solve satisfy;

% 5. Hiển thị kết quả
output ["root version: ", show(root_version), "\nfoo version: ", show(foo_version), 
        "\nleft version: ", show(left_version), "\nright version: ", show(right_version),
        "\nshared version: ", show(shared_version), "\ntarget version: ", show(target_version)];

```
![image](https://github.com/user-attachments/assets/c0f7319b-4c00-4897-9b1b-0b18a1e1a538)

## Задача 7
Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему граничений надо построить автоматически, по метаданным.

```metadata.py
# metadata.py

package_metadata = {
    "root": {
        "1.0.0": {
            "dependencies": {"foo": "^1.0.0", "target": "^2.0.0"}
        }
    },
    "foo": {
        "1.1.0": {
            "dependencies": {"left": "^1.0.0", "right": "^1.0.0"}
        },
        "1.0.0": {
            "dependencies": {}
        }
    },
    "left": {
        "1.0.0": {
            "dependencies": {"shared": ">=1.0.0"}
        }
    },
    "right": {
        "1.0.0": {
            "dependencies": {"shared": "<2.0.0"}
        }
    },
    "shared": {
        "2.0.0": {
            "dependencies": {}
        },
        "1.0.0": {
            "dependencies": {"target": "^1.0.0"}
        }
    },
    "target": {
        "2.0.0": {
            "dependencies": {}
        },
        "1.0.0": {
            "dependencies": {}
        }
    }
}

```

```generate_mzn.py
# generate_mzn.py
import metadata

def generate_mzn_constraints(metadata):
    constraints = []
    package_vars = {}

    # Tạo biến cho mỗi package
    for package, versions in metadata.items():
        package_var = f"{package}_version"
        package_vars[package] = package_var
        version_enum = ', '.join([f"{package}_{v.replace('.', '_')}" for v in versions])
        constraints.append(f"enum Versions_{package} = {{{version_enum}}};")
        constraints.append(f"var Versions_{package}: {package_var};")

    # Tạo ràng buộc cho các dependencies
    for package, versions in metadata.items():
        package_var = package_vars[package]
        for version, data in versions.items():
            version_name = f"{package}_{version.replace('.', '_')}"
            deps = data.get("dependencies", {})

            for dep_pkg, dep_version in deps.items():
                dep_var = package_vars[dep_pkg]

                if dep_version.startswith('^'):
                    min_version = dep_version[1:].replace('.', '_')
                    constraint = f"constraint ({package_var} == {version_name} -> {dep_var} >= {dep_pkg}_{min_version});"
                elif dep_version.startswith('>='):
                    min_version = dep_version[2:].replace('.', '_')
                    constraint = f"constraint ({package_var} == {version_name} -> {dep_var} >= {dep_pkg}_{min_version});"
                elif dep_version.startswith('<'):
                    max_version = dep_version[1:].replace('.', '_')
                    constraint = f"constraint ({package_var} == {version_name} -> {dep_var} < {dep_pkg}_{max_version});"
                else:
                    exact_version = dep_version.replace('.', '_')
                    constraint = f"constraint ({package_var} == {version_name} -> {dep_var} == {dep_pkg}_{exact_version});"

                constraints.append(constraint)

    return '\n'.join(constraints)

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    # Tạo hệ thống ràng buộc dựa trên metadata
    mzn_constraints = generate_mzn_constraints(metadata.package_metadata)

    # Ghi ra file .mzn
    write_to_file("dependencies.mzn", mzn_constraints)
    print("MiniZinc model generated and saved to dependencies.mzn")

```

```dependencies.mzn
enum Versions_root = {root_1_0_0};
var Versions_root: root_version;

enum Versions_foo = {foo_1_0_0, foo_1_1_0};
var Versions_foo: foo_version;

enum Versions_left = {left_1_0_0};
var Versions_left: left_version;

enum Versions_right = {right_1_0_0};
var Versions_right: right_version;

enum Versions_shared = {shared_1_0_0, shared_2_0_0};
var Versions_shared: shared_version;

enum Versions_target = {target_1_0_0, target_2_0_0};
var Versions_target: target_version;

constraint (root_version == root_1_0_0 -> foo_version >= foo_1_0_0);
constraint (root_version == root_1_0_0 -> target_version >= target_2_0_0);
constraint (foo_version == foo_1_1_0 -> left_version >= left_1_0_0);
constraint (foo_version == foo_1_1_0 -> right_version >= right_1_0_0);
constraint (left_version == left_1_0_0 -> shared_version >= shared_1_0_0);
constraint (right_version == right_1_0_0 -> shared_version < shared_2_0_0);
constraint (shared_version == shared_1_0_0 -> target_version >= target_1_0_0);

solve satisfy;

```
![image](https://github.com/user-attachments/assets/9c9bd48d-6f7f-4926-9b55-ed9c39f7e3c1)
