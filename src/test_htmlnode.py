import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_create_leafnode_with_value_no_tag(self):
        node = LeafNode(value="Hello, World!")
        self.assertEqual(node.value, "Hello, World!")
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_create_leafnode_with_value_and_tag(self):
        node = LeafNode(tag="p", value="Hello, World!")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.tag, "p")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html_with_value_no_tag(self):
        node = LeafNode(value="Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")

    def test_to_html_with_value_and_tag(self):
        node = LeafNode(tag="p", value="Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_to_html_without_value_raises_valueerror(self):
        node = LeafNode(tag="p", value="Valid value")
        node.value = None
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
