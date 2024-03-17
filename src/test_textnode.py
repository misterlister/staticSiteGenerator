import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):

    # Equal
    
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This has no URL", "normal", None)
        node2 = TextNode("This has no URL", "normal")
        self.assertEqual(node, node2)

    # Not Equal

    def test_url_scheme(self):
        node = TextNode("This has no URL", "normal", "https://test.com")
        node2 = TextNode("This has no URL", "normal", "http://test.com")
        self.assertNotEqual(node, node2)

    def test_url_domain(self):
        node = TextNode("This has no URL", "normal", "http://test.com")
        node2 = TextNode("This has no URL", "normal", "http://tests.com")
        self.assertNotEqual(node, node2)

    def test_url_subdomain(self):
        node = TextNode("This has no URL", "normal", "http://info.test.com")
        node2 = TextNode("This has no URL", "normal", "http://infom.test.com")
        self.assertNotEqual(node, node2)

    def test_url_tld(self):
        node = TextNode("This has no URL", "normal", "http://test.com")
        node2 = TextNode("This has no URL", "normal", "http://test.org")
        self.assertNotEqual(node, node2)

    def test_text_space_start(self):
        node = TextNode("This is text", "normal")
        node2 = TextNode(" This is text", "normal")
        self.assertNotEqual(node, node2)

    def test_text_space_mid(self):
        node = TextNode("This is text", "normal")
        node2 = TextNode("This  is text", "normal")
        self.assertNotEqual(node, node2)

    def test_text_space_end(self):
        node = TextNode("This is text", "normal")
        node2 = TextNode("This is text ", "normal")
        self.assertNotEqual(node, node2)

    def test_text_character_start(self):
        node = TextNode("This is text", "normal")
        node2 = TextNode("This is text.", "normal")
        self.assertNotEqual(node, node2)

    def test_text_character_mid(self):
        node = TextNode("This is text", "normal")
        node2 = TextNode("This, is text", "normal")
        self.assertNotEqual(node, node2)

    def test_text_character_end(self):
        node = TextNode("This is text", "normal")
        node2 = TextNode("-This is text", "normal")
        self.assertNotEqual(node, node2)

    def test_text_case(self):
        node = TextNode("This is text", "normal")
        node2 = TextNode("this is text", "normal")
        self.assertNotEqual(node, node2)

    def test_text_type(self):
        node = TextNode("This has no URL", "jtalic")
        node2 = TextNode("This has no URL", "italic")
        self.assertNotEqual(node, node2)

    def test_text_type_case(self):
        node = TextNode("This has no URL", "Italic")
        node2 = TextNode("This has no URL", "italic")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
