import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    # HTMLNode

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

    # LeafNode

    def test_empty_value_leaf(self):
        node = LeafNode(None, None)
        html_string = node.to_html()
        error_string = html_string.args[0]
        expected_string = "Error: Invalid HTML: no value"
        self.assertEqual(error_string, expected_string)

    def test_p_tag_leaf(self):
        node = LeafNode("p", "This is a leaf")
        html_string = node.to_html()
        expected_string = "<p>This is a leaf</p>"
        self.assertEqual(html_string, expected_string)

    def test_a_tag_leaf(self):
        node = LeafNode("a", "This is a link", {"href": "https://www.test.com"})
        html_string = node.to_html()
        expected_string = "<a href=\"https://www.test.com\">This is a link</a>"
        self.assertEqual(html_string, expected_string)

    # ParentNode
        
    def test_parentNode_html_single_child(self):
        node = ParentNode("p", 
                          [
                              LeafNode("b", "Bold text")
                          ])
        html_string = node.to_html()
        expected_string = "<p><b>Bold text</b></p>"
        self.assertEqual(html_string, expected_string)

    def test_parentNode_html_multiple_children(self):
        node = ParentNode("p", 
                          [
                              LeafNode("b", "Bold text"),
                              LeafNode("i", "italic text"),
                              LeafNode(None, "Regular text")
                          ])
        html_string = node.to_html()
        expected_string = "<p><b>Bold text</b><i>italic text</i>Regular text</p>"
        self.assertEqual(html_string, expected_string)

    def test_parentNode_html_single_nest(self):
        node = ParentNode("div", 
                          [
                              ParentNode("p", [
                                  LeafNode("b", "Bold text")
                                  ])
                          ])
        html_string = node.to_html()
        expected_string = "<div><p><b>Bold text</b></p></div>"
        self.assertEqual(html_string, expected_string)

if __name__ == "__main__":
    unittest.main()