import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):

    def test_textnode_equality(self):
        node1 = TextNode("Hello", TextType.NORMAL, "http://example.com")
        node2 = TextNode("Hello", TextType.NORMAL, "http://example.com")
        self.assertEqual(node1, node2)

    def test_textnode_inequality_different_text(self):
        node1 = TextNode("Hello", TextType.NORMAL, "http://example.com")
        node2 = TextNode("Hi", TextType.NORMAL, "http://example.com")
        self.assertNotEqual(node1, node2)

    def test_textnode_inequality_different_text_type(self):
        node1 = TextNode("Hello", TextType.NORMAL, "http://example.com")
        node2 = TextNode("Hello", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node1, node2)

    def test_textnode_inequality_different_url(self):
        node1 = TextNode("Hello", TextType.NORMAL, "http://example.com")
        node2 = TextNode("Hello", TextType.NORMAL, "http://example.org")
        self.assertNotEqual(node1, node2)

    def test_textnode_repr(self):
        node = TextNode("Hello", TextType.NORMAL, "http://example.com")
        expected_repr = "TextNode(Hello, normal, http://example.com)"
        self.assertEqual(repr(node), expected_repr)


class TestTextNodeToHtmlNode(unittest.TestCase):

    def test_text_node_to_html_node_invalid_type(self):
        text_node = TextNode("Invalid Text", TextType.NORMAL)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )


if __name__ == "__main__":
    unittest.main()
