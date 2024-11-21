from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    text_node = TextNode("Hello", TextType.NORMAL, "https://example.com")
    html_node = HTMLNode(
        "a", {"href": text_node.url}, [text_node.text], {"class": "link"}
    )
    print(text_node.__repr__())
    print(html_node.__repr__())


if __name__ == "__main__":
    main()
