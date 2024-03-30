import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)

from textnode import (
    TextNode,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_CODE,
    TEXT_TYPE_IMAGE,
    TEXT_TYPE_LINK
)


class TestTextNode(unittest.TestCase):
    
    # Delimiter
    
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TEXT_TYPE_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("bolded", TEXT_TYPE_BOLD),
                TextNode(" word", TEXT_TYPE_TEXT),
            ],
            new_nodes
            )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("bolded", TEXT_TYPE_BOLD),
                TextNode(" word and ", TEXT_TYPE_TEXT),
                TextNode("another", TEXT_TYPE_BOLD),
            ],
            new_nodes
            )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("bolded word", TEXT_TYPE_BOLD),
                TextNode(" and ", TEXT_TYPE_TEXT),
                TextNode("another", TEXT_TYPE_BOLD),
            ],
            new_nodes
            )
        
    def test_delim_bold_empty(self):
        node = TextNode(
            "This is text with a **bolded word** and ****nothing", TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("bolded word", TEXT_TYPE_BOLD),
                TextNode(" and ", TEXT_TYPE_TEXT),
                TextNode("nothing", TEXT_TYPE_TEXT),
            ],
            new_nodes
            )
        
    def test_delim_bold_start(self):
        node = TextNode(
            "**This** is text with a **bolded word** at the start", TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        self.assertListEqual(
            [
                TextNode("This", TEXT_TYPE_BOLD),
                TextNode(" is text with a ", TEXT_TYPE_TEXT),
                TextNode("bolded word", TEXT_TYPE_BOLD),
                TextNode(" at the start", TEXT_TYPE_TEXT)
            ],
            new_nodes
            )
        
        

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TEXT_TYPE_TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TEXT_TYPE_ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TEXT_TYPE_TEXT),
                TextNode("italic", TEXT_TYPE_ITALIC),
                TextNode(" word", TEXT_TYPE_TEXT),
            ],
            new_nodes
            )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TEXT_TYPE_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TEXT_TYPE_CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("code block", TEXT_TYPE_CODE),
                TextNode(" word", TEXT_TYPE_TEXT),
            ],
            new_nodes
            )
    
    # Images and Links
    
    def test_image_extraction(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        images = extract_markdown_images(text)
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("another", "https://i.imgur.com/dfsdkjfd.png")
            ],
            images
        )
        
    def test_link_extraction(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        images = extract_markdown_links(text)
        self.assertListEqual(
            [("link", "https://www.example.com"),
            ("another", "https://www.example.com/another")
            ],
            images
        )
        
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TEXT_TYPE_TEXT),
                TextNode("image", TEXT_TYPE_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TEXT_TYPE_IMAGE, "https://www.example.com/image.png"),
            ],
            new_nodes
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TEXT_TYPE_TEXT),
                TextNode("image", TEXT_TYPE_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TEXT_TYPE_TEXT),
                TextNode(
                    "second image", TEXT_TYPE_IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("link", TEXT_TYPE_LINK, "https://boot.dev"),
                TextNode(" and ", TEXT_TYPE_TEXT),
                TextNode("another link", TEXT_TYPE_LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TEXT_TYPE_TEXT),
            ],
            new_nodes
        )
        
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        textnodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TEXT_TYPE_TEXT),
                TextNode("text", TEXT_TYPE_BOLD),
                TextNode(" with an ", TEXT_TYPE_TEXT),
                TextNode("italic", TEXT_TYPE_ITALIC),
                TextNode(" word and a ", TEXT_TYPE_TEXT),
                TextNode("code block", TEXT_TYPE_CODE),
                TextNode(" and an ", TEXT_TYPE_TEXT),
                TextNode("image", TEXT_TYPE_IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TEXT_TYPE_TEXT),
                TextNode("link", TEXT_TYPE_LINK, "https://boot.dev")
            ],
            textnodes
        )

if __name__ == "__main__":
    unittest.main()