import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
