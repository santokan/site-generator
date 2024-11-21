import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_props_to_html(self):
        node = HTMLNode(
            "a", {"href": "https://example.com"}, ["Example"], {"class": "link"}
        )
        expected_html = '<a href="https://example.com" class="link">Example</a>'
        self.assertEqual(node.props_to_html(), expected_html)

        node = HTMLNode("div", {"id": "main"}, ["Content"], {"class": "container"})
        expected_html = '<div id="main" class="container">Content</div>'
        self.assertEqual(node.props_to_html(), expected_html)

        node = HTMLNode("p", {"class": "paragraph"}, ["This is a paragraph."], {})
        expected_html = '<p class="paragraph">This is a paragraph.</p>'
        self.assertEqual(node.props_to_html(), expected_html)
