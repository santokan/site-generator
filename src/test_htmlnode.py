import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):

    def test_create_parentnode_with_children(self):
        child1 = LeafNode(tag="p", value="Child 1")
        child2 = LeafNode(tag="p", value="Child 2")
        parent = ParentNode(tag="div", children=[child1, child2])
        self.assertEqual(parent.tag, "div")
        self.assertEqual(parent.children, [child1, child2])
        self.assertIsNone(parent.value)
        self.assertIsNone(parent.props)

    def test_to_html_with_children(self):
        child1 = LeafNode(tag="p", value="Child 1")
        child2 = LeafNode(tag="p", value="Child 2")
        parent = ParentNode(tag="div", children=[child1, child2])
        expected_html = "<div><p>Child 1</p><p>Child 2</p></div>"
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_without_tag_raises_valueerror(self):
        child1 = LeafNode(tag="p", value="Child 1")
        parent = ParentNode(tag=None, children=[child1])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_with_child_without_value_raises_valueerror(self):
        child1 = LeafNode(tag="p", value=None)
        parent = ParentNode(tag="div", children=[child1])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", value="grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
