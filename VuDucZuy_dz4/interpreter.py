import sys
import yaml

def convert_bin_to_hex(binary_file, result_file, log_file):
    # Đọc file nhị phân
    with open(binary_file, "rb") as bin_file:
        binary = bin_file.read()

    # Chuyển các byte trong binary sang dạng hex
    hex_values = [f"0x{byte:02X}" for byte in binary]

    # Ghi kết quả vào file .yaml
    with open(result_file, "w") as result:
        yaml.dump({"LOAD_CONST": hex_values[:4]}  , result)
        yaml.dump({"READ_MEM"  : hex_values[4:8]} , result)
        yaml.dump({"WRITE_MEM" : hex_values[8:12]}, result)
        yaml.dump({"MULTIPLY"  : hex_values[12:]} , result)

    log_data = {
        "status": "success",
        "binary_file": binary_file,
        "result_file": result_file,
        "converted_data": hex_values,
        "log_message": "Converted successfully from binary to hex and write into YAML file."
    }

    # Ghi log vào file log.yaml
    with open(log_file, "w") as log:
        yaml.dump(log_data, log)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 interpreter.py <input.bin> <output.yaml> <log.yaml>")
        sys.exit(1)

    convert_bin_to_hex(sys.argv[1], sys.argv[2], sys.argv[3])
