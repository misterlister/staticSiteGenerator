from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

BLOCK_TYPE_PARAGRAPH = "paragraph"
BLOCK_TYPE_HEADING = "heading"
BLOCK_TYPE_CODE = "code"
BLOCK_TYPE_QUOTE = "quote"
BLOCK_TYPE_U_LIST = "unordered_list"
BLOCK_TYPE_O_LIST = "ordered_list"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        html_node = block_to_html_node(block)
        child_nodes.append(html_node)
    return ParentNode("div", child_nodes)

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    non_empty_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if len(stripped_block) > 0:
            non_empty_blocks.append(stripped_block)
    return non_empty_blocks

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BLOCK_TYPE_PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BLOCK_TYPE_HEADING:
        return heading_to_html_node(block)
    if block_type == BLOCK_TYPE_CODE:
        return code_to_html_node(block)
    if block_type == BLOCK_TYPE_QUOTE:
        return quote_to_html_node(block)
    if block_type == BLOCK_TYPE_U_LIST:
        return u_list_to_html_node(block)
    if block_type == BLOCK_TYPE_O_LIST:
        return o_list_to_html_node(block)
    raise ValueError("Error: Invalid block type")

def block_to_block_type(block):
    lines = block.split("\n")
    
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return BLOCK_TYPE_HEADING
    
    if (
        len(lines) > 1
        and lines[0].startswith("```")
        and lines[-1].startswith("```")
    ):
        return BLOCK_TYPE_CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_U_LIST
    
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_U_LIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BLOCK_TYPE_PARAGRAPH
            i += 1
        return BLOCK_TYPE_O_LIST
    
    return BLOCK_TYPE_PARAGRAPH
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    child_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        child_nodes.append(html_node)
    return child_nodes    
    
def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    child_nodes = text_to_children(paragraph)
    return ParentNode("p", child_nodes)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level > 6:
        raise ValueError(f"Error: Invalid header - level {level}")
    if level + 1 == len(block):
        raise ValueError("Error: Empty heading")
    text = block[level + 1 :]
    child_nodes = text_to_children(text)
    return ParentNode(f"h{level}", child_nodes)
            
def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Error: Invalid code block")
    text = block[4:-3]
    child_nodes = text_to_children(text)
    code_node = ParentNode("code", child_nodes)
    return ParentNode("pre", [code_node])

def quote_to_html_node(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Error: Invalid quote block")
        stripped_lines.append(line.lstrip(">").strip())
    text = " ".join(stripped_lines)
    child_nodes = text_to_children(text)
    return ParentNode("blockquote", child_nodes)

def u_list_to_html_node(block):
    lines = block.split("\n")
    list_marker = block[0]
    list_items = []
    if list_marker != "*" and list_marker != "-":
        raise ValueError(f"Error: Invalid unordered list marker ({list_marker})")
    for line in lines:
        if not line.startswith(list_marker):
            raise ValueError("Error: Invalid unordered list block")
        stripped_item = line.lstrip(list_marker).strip()
        list_item = text_to_children(stripped_item)
        list_items.append(ParentNode("li", list_item))
    return ParentNode("ul", list_items)

def o_list_to_html_node(block):
    lines = block.split("\n")
    list_items = []
    i = 1
    for line in lines:
        if not line.startswith(f"{i}. "):
            raise ValueError("Error: Invalid ordered list block")
        stripped_item = line.lstrip(f"{i}.").strip()
        list_item = text_to_children(stripped_item)
        list_items.append(ParentNode("li", list_item))
        i += 1
    return ParentNode("ol", list_items)