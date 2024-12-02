import subprocess
import argparse
import sys


def get_dependencies(package_name):
    """
    Lấy danh sách phụ thuộc của gói bằng lệnh apt-cache.
    Trả về danh sách các gói phụ thuộc mà không có phần tử trùng lặp.
    """
    try:
        result = subprocess.run(
            ['apt-cache', 'depends', package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        dependencies = set()  # Sử dụng set để loại bỏ phần tử trùng lặp
        for line in result.stdout.splitlines():
            if "Depends:" in line:
                dep = line.split(":")[1].strip()
                # Kiểm tra xem phụ thuộc có phải là meta-package
                show_result = subprocess.run(
                    ['apt-cache', 'show', dep],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                if show_result.returncode == 0 and show_result.stdout.strip():
                    dependencies.add(dep)  # Thêm vào set để tự động loại bỏ trùng lặp
                else:
                    print(f"Lưu ý: Gói {dep} có thể là meta-package hoặc không tồn tại.")
        return list(dependencies)  # Chuyển lại thành list
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi lấy phụ thuộc của gói <{package_name}>: {e}")
        return []

def build_mermaid_graph(package_name, repo_url):
    """
    Xây dựng đồ thị phụ thuộc dưới dạng Mermaid.
    """
    # Khởi tạo đồ thị Mermaid
    graph = ["graph TD"]

    # Đệ quy để lấy phụ thuộc bắc cầu
    def add_dependencies(package, visited):
        if package not in visited:
            visited.add(package)
            dependencies = get_dependencies(package)
            for dep in dependencies:
                graph.append(f"  {package} --> {dep}")
                add_dependencies(dep, visited)

    # Bắt đầu từ gói chính
    visited = set()
    add_dependencies(package_name, visited)

    # Thêm liên kết tới URL kho lưu trữ
    graph.append(f"  Repo[{repo_url}]")

    # Trả về đồ thị Mermaid dưới dạng chuỗi
    return "\n".join(graph)

def main():
    parser = argparse.ArgumentParser(description='Công cụ hiển thị đồ thị phụ thuộc cho các gói Ubuntu')
    parser.add_argument('visualizer_path', help='Đường dẫn tới chương trình trực quan hóa đồ thị')
    parser.add_argument('package', help='Tên gói cần phân tích')
    parser.add_argument('repo_url', help='URL kho lưu trữ')

    args = parser.parse_args()

    # Tạo đồ thị phụ thuộc
    graph = build_mermaid_graph(args.package, args.repo_url)

    # Hiển thị đồ thị ra màn hình
    print(graph)

    # Lưu đồ thị vào file graph.mmd
    with open("graph.mmd", "w") as f:
        f.write(graph)

    # Gọi trình trực quan hóa để hiển thị đồ thị
    subprocess.run(["/usr/local/bin/mmdc", "-i", "graph.mmd", "-o", "graph.png"])

if __name__ == "__main__":
    main()
