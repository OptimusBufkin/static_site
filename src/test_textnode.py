import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        self.assertEqual(node, node2)
    
    def test_eq_diff_1(self):
        node = TextNode("This is a text node", TextType.CODE, "www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        self.assertNotEqual(node, node2)
    
    def test_eq_diff_2(self):
        node = TextNode("This is a text node, yes", TextType.CODE, "www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        self.assertNotEqual(node, node2)

    def test_eq_diff_3(self):
        node = TextNode("This is a text node, yes", TextType.CODE, "www.testing.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()