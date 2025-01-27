from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    text_node = TextNode("Hello", TextType.NORMAL, "https://example.com")
    html_node = HTMLNode(
        "a", None, None, {"href": "https://www.google.com", "target": "_blank"}
    )
    leaf_node = LeafNode("p", "This is a paragraph of text.")
    print(text_node.__repr__())
    print(html_node.__repr__())
    print(html_node.props_to_html())
    print(leaf_node.to_html())
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())


if __name__ == "__main__":
    main()
