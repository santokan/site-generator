from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    text_node = TextNode("Hello", TextType.NORMAL, "https://example.com")
    html_node = HTMLNode(
        "a", None, None, {"href": "https://www.google.com", "target": "_blank"}
    )
    print(text_node.__repr__())
    print(html_node.__repr__())
    print(html_node.props_to_html())


if __name__ == "__main__":
    main()
