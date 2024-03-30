from textnode import (
    TextNode,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_CODE,
    TEXT_TYPE_IMAGE,
    TEXT_TYPE_LINK
)

import re


def text_to_textnodes(text):
    nodes = [TextNode(text, TEXT_TYPE_TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TEXT_TYPE_BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TEXT_TYPE_ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TEXT_TYPE_CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TEXT_TYPE_TEXT:
            if delimiter in node.text:
                split_text = node.text.split(delimiter)
                if len(split_text) % 2 == 0:
                    raise ValueError(f"Error: Invalid Markdown syntax. Formatted section: ({delimiter}) not closed.")
                for i in range(len(split_text)):
                    if split_text[i] != "":
                        if i % 2 == 0:
                            new_nodes.append(TextNode(split_text[i], node.text_type))
                        else:
                            new_nodes.append(TextNode(split_text[i], text_type))
            else:
                new_nodes.append(node)
                
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    images = re.findall(pattern, text)
    return images

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    links = re.findall(pattern, text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TEXT_TYPE_TEXT:
            text = node.text
            images = extract_markdown_images(text)
            if len(images) == 0:
                new_nodes.append(node)
            else:
                for tuple in images:
                    split_text = text.split(f"![{tuple[0]}]({tuple[1]})", 1)
                    if len(split_text) != 2:
                        raise ValueError("Error: Invalid Markdown syntax. Image section not closed.")
                    if split_text[0] != "":
                        new_nodes.append(TextNode(split_text[0], TEXT_TYPE_TEXT))
                    new_nodes.append(TextNode(tuple[0], TEXT_TYPE_IMAGE, tuple[1]))
                    text = split_text[1]
                if text != "":
                    new_nodes.append(TextNode(text, TEXT_TYPE_TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TEXT_TYPE_TEXT:
            text = node.text
            links = extract_markdown_links(text)
            if len(links) == 0:
                new_nodes.append(node)
            else:
                for tuple in links:
                    split_text = text.split(f"[{tuple[0]}]({tuple[1]})", 1)
                    if len(split_text) != 2:
                        raise ValueError("Error: Invalid Markdown syntax. Link section not closed.")
                    if split_text[0] != "":
                        new_nodes.append(TextNode(split_text[0], TEXT_TYPE_TEXT))
                    new_nodes.append(TextNode(tuple[0], TEXT_TYPE_LINK, tuple[1]))
                    text = split_text[1]
                if text != "":
                    new_nodes.append(TextNode(text, TEXT_TYPE_TEXT))
        else:
            new_nodes.append(node)
    return new_nodes
