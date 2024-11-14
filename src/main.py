from textnode import TextNode, TextType


def main():
    text_node = TextNode("Hello", TextType.NORMAL, "https://example.com")
    print(text_node.__repr__())


if __name__ == "__main__":
    main()
