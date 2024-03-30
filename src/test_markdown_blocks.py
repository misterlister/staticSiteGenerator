import unittest

from markdown_blocks import (
    markdown_to_html_node,
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
    
    # Markdown to HTMLNode
    
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
    
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