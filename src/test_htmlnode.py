import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode(
                "a",
                "test",
                None,
                {"href": "https://www.google.com", "target": "_blank"},
            )
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(
            "a", "test", None, {"href": "https://www.google.com", "target": "_blank"}
        )
        expected_value = ' href="https://www.google.com" target="_blank"'
        actual_value = node.props_to_html()
        self.assertEqual(actual_value, expected_value)

    def test_props_to_html_one_prop(self):
        node = HTMLNode("a", "test", None, {"href": "https://www.google.com"})
        expected_value = ' href="https://www.google.com"'
        actual_value = node.props_to_html()
        self.assertEqual(actual_value, expected_value)


if __name__ == "__main__":
    unittest.main()
