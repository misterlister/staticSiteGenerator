from textnode import (
    TextNode,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_CODE,
)



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            if delimiter in node.text:
                split_text = node.text.split(delimiter)
                if len(split_text) % 3 == 0:
                    for i in range(0, len(split_text), 3):
                        new_nodes.append(TextNode(split_text[i]), node.text_type)
                        new_nodes.append(TextNode(split_text[i+1]), text_type)
                        new_nodes.append(TextNode(split_text[i+2]), node.text_type)
                else:
                    raise Exception(f"Error: Delimiter '{delimiter}' must occur in pairs. Text contains invalid Markdown syntax.")
        else:
            new_nodes.append(node)
    return new_nodes
