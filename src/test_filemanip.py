import unittest

from filemanip import (
    extract_title
)

from main import (
    content_path
)

class TestFileManip(unittest.TestCase):
    
    def test_title_extraction(self):
        file = """
# This is a title        
"""
        extracted_title = extract_title(file)
        self.assertEqual(extracted_title, "This is a title")
    
    def test_title_extraction_blank_lines(self):
        file = """



# This is a title        
"""
        extracted_title = extract_title(file)
        self.assertEqual(extracted_title, "This is a title")
        
    def test_title_extraction_extra_space(self):
        file = """
#      This is a title        
"""
        extracted_title = extract_title(file)
        self.assertEqual(extracted_title, "This is a title")
        
        
if __name__ == "__main__":
    unittest.main()