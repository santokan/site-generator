import re
from textnode import TextNode, TextType


def text_to_textnodes(text):
    # Start with a single TextNode containing the entire text
    nodes = [TextNode(text, TextType.TEXT)]
    # split everything
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes


def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimeter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown syntax")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue
        last_index = 0
        for alt_text, url in images:
            start_index = text.find(f"![{alt_text}]({url})", last_index)
            if start_index > last_index:
                new_nodes.append(TextNode(text[last_index:start_index], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))
            last_index = start_index + len(f"![{alt_text}]({url})")
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue
        last_index = 0
        for link_text, url in links:
            start_index = text.find(f"[{link_text}]({url})", last_index)
            if start_index > last_index:
                new_nodes.append(TextNode(text[last_index:start_index], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
            last_index = start_index + len(f"[{link_text}]({url})")
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
