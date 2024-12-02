import re
import yaml
import sys

class ConfigParser:
    def __init__(self):
        self.constants = {}

    def parse_line(self, line):
        line = line.strip()

        # Bỏ qua dòng trống hoặc chú thích
        if not line or line.startswith("#"):
            return None

        # Xử lý khai báo hằng số
        if line.startswith("var"):
            match = re.match(r"var\s+([A-Za-z_][A-Za-z0-9_]*)\s+(.*)", line)
            if not match:
                raise ValueError(f"Invalid constant declaration: {line}")
            name, value = match.groups()
            self.constants[name] = self.evaluate_value(value)
            return None

        # Thay thế hằng số
        line = self.replace_constants(line)

        # Xử lý tên và giá trị
        match = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s+(.*)", line)
        if not match:
            raise ValueError(f"Invalid line: {line}")
        name, value = match.groups()
        return name, self.evaluate_value(value)

    def replace_constants(self, line):
        def replace_match(match):
            const_name = match.group(1)
            if const_name not in self.constants:
                raise ValueError(f"Undefined constant: {const_name}")
            return str(self.constants[const_name])

        # Thay thế các hằng số trong dạng #(CONSTANT)
        return re.sub(r"#\(([A-Za-z_][A-Za-z0-9_]*)\)", replace_match, line)

    def evaluate_value(self, value):
        value = value.strip()

        # Thay thế tất cả các hằng số
        value = self.replace_constants(value)

        # Xử lý mảng
        if value.startswith("<<") and value.endswith(">>"):
            items = value[2:-2].split(",")
            return [self.evaluate_value(item.strip()) for item in items]

        # Xử lý chuỗi
        if value.startswith("[[") and value.endswith("]]"):
            return value[2:-2]

        # Xử lý số
        if re.match(r"^-?\d+(\.\d+)?$", value):
            return float(value) if "." in value else int(value)

        return value

    def parse(self, input_text):
        result = {}
        for line in input_text.splitlines():
            try:
                parsed = self.parse_line(line)
                if parsed:
                    name, value = parsed
                    result[name] = value
            except ValueError as e:
                raise ValueError(f"Error processing line: {line}\n{e}")
        return result

def main():
    # Đọc dữ liệu từ stdin
    input_text = sys.stdin.read()

    # Xử lý
    parser = ConfigParser()
    try:
        parsed_data = parser.parse(input_text)
        yaml_output = yaml.dump(parsed_data, allow_unicode=True, default_flow_style=False)
        print(yaml_output)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
