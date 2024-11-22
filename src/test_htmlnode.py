import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"class": "test-class"})
        self.assertEqual(node.props_to_html(), ' class="test-class"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(
            props={"id": "test-id", "class": "test-class", "data-role": "test-role"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' id="test-id" class="test-class" data-role="test-role"',
        )


if __name__ == "__main__":
    unittest.main()
