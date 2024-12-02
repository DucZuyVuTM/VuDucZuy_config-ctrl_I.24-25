import unittest
from unittest.mock import patch
from dependency_visualizer import get_dependencies, build_mermaid_graph

class TestDependencyVisualizer(unittest.TestCase):

    @patch('subprocess.run')
    def test_get_dependencies(self, mock_run):
        # Mô phỏng kết quả trả về khi gọi lệnh apt-cache depends
        mock_run.return_value.stdout = (
            "  Depends: libc6\n  Depends: libssl3t64\n  Depends: libgcc-s1\n"
            "  Depends: gcc-14-base\n  Depends: libc6\n"
        )
        mock_run.return_value.stderr = ""
        mock_run.return_value.returncode = 0
        
        # Kiểm tra hàm get_dependencies
        result = get_dependencies('openssl')
        expected_result = ['libc6', 'libssl3t64', 'libgcc-s1', 'gcc-14-base']
        
        # Sử dụng assertCountEqual để so sánh danh sách mà không quan tâm đến thứ tự
        self.assertCountEqual(result, expected_result)

    @patch('subprocess.run')
    def test_get_dependencies_with_meta_package(self, mock_run):
        # Mô phỏng kết quả trả về khi gọi lệnh apt-cache depends với một gói meta-package
        mock_run.return_value.stdout = "  Depends: libc6\n"
        mock_run.return_value.stderr = ""
        mock_run.return_value.returncode = 0
        
        result = get_dependencies('libc6')
        expected_result = ['libc6']
        self.assertEqual(result, expected_result)

    @patch('subprocess.run')
    def test_build_mermaid_graph(self, mock_run):
        # Mô phỏng kết quả trả về của lệnh apt-cache depends
        mock_run.return_value.stdout = (
            "  Depends: libc6\n  Depends: libssl3t64\n  Depends: libgcc-s1\n"
            "  Depends: gcc-14-base\n  Depends: libc6\n"
        )
        mock_run.return_value.stderr = ""
        mock_run.return_value.returncode = 0

        # Kiểm tra hàm build_mermaid_graph
        graph = build_mermaid_graph('openssl', 'http://archive.ubuntu.com/ubuntu')
        # Kiểm tra xem đồ thị có chứa các phụ thuộc đúng không
        self.assertIn('openssl --> libc6', graph)
        self.assertIn('openssl --> libssl3t64', graph)
        self.assertIn('openssl --> libgcc-s1', graph)
        self.assertIn('openssl --> gcc-14-base', graph)

if __name__ == '__main__':
    unittest.main()
