import unittest

from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BLOCK_TYPE_PARAGRAPH,
    BLOCK_TYPE_HEADING,
    BLOCK_TYPE_CODE,
    BLOCK_TYPE_QUOTE,
    BLOCK_TYPE_U_LIST,
    BLOCK_TYPE_O_LIST
)

class TestMarkdownBlocks(unittest.TestCase):
    
    # Markdown to Blocks
    
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            ["This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"],
            blocks
        )
        
    def test_markdown_to_blocks_newlines(self):
        markdown = """
This is **bolded** paragraph



This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line






* This is a list
* with items

"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            ["This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"],
            blocks
        )
        
    def test_markdown_to_blocks_spaces(self):
        markdown = """
This is **bolded** paragraph 

 

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items     

 
"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            ["This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"],
            blocks
        )
        
    # Block to Block Type - Correct types
    
    def test_block_to_heading_1(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_HEADING)
        
    def test_block_to_heading_6(self):
        block = "###### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_HEADING)
        
    def test_block_to_code(self):
        block = "```\ncode\n``` "
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_CODE)
        
    def test_block_to_quote(self):
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_QUOTE)
        
    def test_block_to_multiline_quote(self):
        block = "> This is a quote\n> With more text"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_QUOTE)
        
    def test_block_to_nospace_quote(self):
        block = ">This is a quote\n>With more text"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_QUOTE)
        
    def test_block_to_unordered_list_dash(self):
        block = "- This is a list\n- With another item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_U_LIST)
        
    def test_block_to_unordered_list_star(self):
        block = "* This is a list\n* With another item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_U_LIST)
        
    def test_block_to_ordered_list(self):
        block = "1. First item\n2. Second item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_O_LIST)
        
    # Block to Block Type - Incorrect formatting
    
    def test_block_to_incorrectly_formatted_heading_1(self):
        block = "#This is an incorrectly formatted heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_PARAGRAPH)
        
    def test_block_to_incorrectly_formatted_heading_7(self):
        block = "####### This is an incorrectly formatted heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_PARAGRAPH)
        
    def test_block_to_incorrectly_formatted_code(self):
        block = "```\nIncorrectly formatted code``` "
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_PARAGRAPH)
        
    def test_block_to_incorrectly_formatted_quote(self):
        block = "<This is an incorrectly formatted quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_PARAGRAPH)
        
    def test_block_to_incorrectly_formatted_multiline_quote(self):
        block = "> This is a quote\n> With more text\n And incorrectly formatted text"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_PARAGRAPH)
        
    def test_block_to_incorrectly_formatted_unordered_list_dash(self):
        block = "- This is a list\n- With another item\n And an incorrectly formatted item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_PARAGRAPH)
        
    def test_block_to_incorrectly_formatted_unordered_list_star(self):
        block = "* This is a list\n* With another item\n- And an incorrectly formatted item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_PARAGRAPH)
        
    def test_block_to_incorrectly_formatted_ordered_list(self):
        block = "1. First item\n2. Second item\n3.incorrectly formatted item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BLOCK_TYPE_PARAGRAPH)
        
if __name__ == "__main__":
    unittest.main()