import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError,LeafNode)

    def test_to_html(self):
        self.assertEqual(
            LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"}).to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

        self.assertEqual(
           LeafNode(tag="p", value="This is a paragraph of text.").to_html(),
            "<p>This is a paragraph of text.</p>" 
        )
    
        self.assertEqual(
           LeafNode(tag="div", value="This is a div.").to_html(),
            "<div>This is a div.</div>" 
        )

        self.assertEqual( LeafNode(tag="h1", value="H1 text.").to_html(),
            "<h1>H1 text.</h1>" 
        )

    def test_props_to_html(self):
        leaf = LeafNode(value=None)
        self.assertRaises(ValueError, leaf.to_html)
    
    
    

if __name__ == '__main__':
    unittest.main()