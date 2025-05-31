import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        #test cases
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
       
    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is some text.",
            None, 
            {"animal": "dog"})
        
        self.assertEqual(node.__repr__(), "HtmlNode(p, This is some text., None, {'animal': 'dog'})")

    def test_values(self):
        node = HTMLNode("h1", "THIS IS TEXT")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "THIS IS TEXT" )

if __name__ == "__main__":
    unittest.main()