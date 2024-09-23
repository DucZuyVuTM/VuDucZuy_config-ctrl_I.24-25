import os
import zipfile
import sys

class VShell:
    def __init__(self, zip_file):
        self.current_path = '/'  # Đường dẫn hiện tại
        self.zip_file = zip_file
        self.zip = zipfile.ZipFile(zip_file, "r")
        self.file_list = self.zip.namelist()  # Lấy danh sách tất cả các file trong file zip

    def pwd(self):
        """Lệnh pwd hiển thị đường dẫn hiện tại"""
        print(self.current_path)

    def ls(self):
        """Lệnh ls liệt kê các file trong thư mục hiện tại"""
        files_in_dir = [f for f in self.file_list if f.startswith(self.current_path[1:]) and f != self.current_path]
        subdirs = set()
        for f in files_in_dir:
            relative_path = f[len(self.current_path[1:]):].strip('/')
            subdir = relative_path.split('/')[0]
            subdirs.add(subdir)
        print('  '.join(sorted(subdirs)))

    def cd(self, path):
        """Lệnh cd thay đổi thư mục hiện tại"""
        if path == '/':
            self.current_path = '/'
        elif path == '..':
            if self.current_path != '/':
                self.current_path = '/'.join(self.current_path.rstrip('/').split('/')[:-1])
                if not self.current_path:
                    self.current_path = '/'
        else:
            new_path = os.path.normpath(os.path.join(self.current_path, path))
            if any(f.startswith(new_path.lstrip('/') + '/') for f in self.file_list):
                self.current_path = new_path
            else:
                print(f"No such directory: {path}")

    def cat(self, file_names):
        """Lệnh cat hiển thị nội dung của file"""
        for file_name in file_names:
            full_path = os.path.normpath(os.path.join(self.current_path.lstrip('/'), file_name))
            if full_path in self.file_list:
                with self.zip.open(full_path) as f:
                    content = f.read().decode('utf-8')
                    print(content)
            else:
                print(f"File {file_name} not found.")

    def run_script(self, script_file):
        """Chạy các lệnh từ file script"""
        with open(script_file, 'r') as script:
            for line in script:
                self.execute_command(line.strip())

    def execute_command(self, command):
        """Xử lý lệnh của người dùng"""
        parts = command.split()
        if not parts:
            return
        cmd = parts[0]
        args = parts[1:]

        if cmd == 'pwd':
            self.pwd()
        elif cmd == 'ls':
            if args:
                if len(args) == 1:
                    CurrentPath = self.current_path
                    self.cd(args[0])
                    self.ls()
                    self.cd(CurrentPath)
                else:
                    print("cd: too many arguments")
            else:
                self.ls()
        elif cmd == 'cd':
            if args:
                if len(args) == 1:
                    self.cd(args[0])
                else:
                    print("cd: too many arguments")
            else:
                print("cd: missing argument")
        elif cmd == 'cat':
            if args:
                for arg in args:
                    # Tách các thành phần của đường dẫn
                    path_list = arg.strip('/').split('/')
                    if len(path_list) == 1:
                        # Nếu chỉ có tên file mà không có thư mục, gọi trực tiếp cat
                        self.cat([arg])
                    else:
                        # Nếu có đường dẫn, chuyển đến thư mục chứa file
                        CurrentPath = self.current_path
                        pathToGo = "/".join(path_list[:-1])
                        self.cd(pathToGo)
                        self.cat([path_list[-1]])  # Lấy file cuối cùng trong đường dẫn
                        self.cd(CurrentPath)
            else:
                print("cat: missing argument")
        else:
            print(f"Command not found: {cmd}")

    def close(self):
        """Đóng file zip"""
        self.zip.close()

def test_commands(vshell):
    """
    Test all implemented commands.
    """
    print("Testing commands...")
    print("======================================")

    # Test ls
    print("Testing ls command:")
    vshell.execute_command("ls")
    vshell.execute_command("ls /test_fs/dir1")
    print("======================================")

    # Test cd
    print("Testing cd command:")
    vshell.execute_command("cd /test_fs/dir1")
    vshell.execute_command("pwd")
    vshell.execute_command("cd /")
    print("======================================")

    # Test pwd
    print("Testing pwd command:")
    vshell.execute_command("cd /test_fs")
    vshell.execute_command("pwd")
    vshell.execute_command("cd /")
    print("======================================")
        
    # Test cat
    print("Testing cat command:")
    vshell.execute_command("cat Main.java")
    vshell.execute_command("cat /test_fs/dir1/file1.txt")
    vshell.execute_command("cat /test_fs/dir1/file1.txt /test_fs/dir1/file2.txt")
    print("======================================")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: vshell.py <zip_file> [--script script_file]")
        sys.exit(1)

    zip_file = sys.argv[1]
    vshell = VShell(zip_file)

    test_commands(vshell)

    # Nếu có tùy chọn --script, chạy các lệnh từ script
    if len(sys.argv) == 4 and sys.argv[2] == '--script':
        script_file = sys.argv[3]
        vshell.run_script(script_file)
    else:
        # Chạy lệnh tương tác
        while True:
            try:
                command = input(f"vshell:{vshell.current_path}$ ")
                if command == 'exit':
                    break
                vshell.execute_command(command)
            except (KeyboardInterrupt, EOFError):
                print("\nExiting vshell...")
                break

    vshell.close()