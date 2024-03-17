import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    # Equal

    def test_eq_empty(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(dir(node), dir(node2))

    def test_eq_None_arguments(self):
        node = HTMLNode(None, None, None, None)
        node2 = HTMLNode()
        self.assertEqual(dir(node), dir(node2))

    def test_eq_tag(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("h1")
        self.assertEqual(node.tag, node2.tag)

    def test_eq_value(self):
        node = HTMLNode(None, "This is text")
        node2 = HTMLNode(None, "This is text")
        self.assertEqual(node.value, node2.value)

    def test_eq_props(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props, node2.props)

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        converted_string = node.props_to_html()
        expected_string = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(converted_string, expected_string)

    # Not Equal

    def test_different_tag(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("h2")
        self.assertNotEqual(node.tag, node2.tag)

    def test_different_tag_space(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("h1 ")
        self.assertNotEqual(node.tag, node2.tag)

    def test_different_value(self):
        node = HTMLNode(None, "This is text")
        node2 = HTMLNode(None, "This iss text")
        self.assertNotEqual(node.value, node2.value)

    def test_different_props(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(None, None, None, {"href": "https://www.googlez.com", "target": "_blank"})
        self.assertNotEqual(node.props, node2.props)