import unittest
import os
from visualizer import generate_mermaid_code


class TestVisualizer(unittest.TestCase):
    def test_generate_mermaid_code(self):
        graph = [
            ("abc1234", ["file1.txt", "file2.txt"]),
            ("def5678", ["file3.txt"]),
        ]
        expected_output = (
            "graph TD\n"
            'abc1234["abc1234\\nfile1.txt\\nfile2.txt"]\n'
            'def5678["def5678\\nfile3.txt"]\n'
            "abc1234 --> def5678"
        )
        self.assertEqual(generate_mermaid_code(graph), expected_output)


if __name__ == "__main__":
    unittest.main()
