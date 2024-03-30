from htmlnode import LeafNode

TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node):
        if self.text != node.text:
            return False
        if self.text_type != node.text_type:
            return False
        if self.url != node.url:
            return False
        return True
    
    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TEXT_TYPE_LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TEXT_TYPE_IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Error: Invalid text type: {text_node.text_type}")

