from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str | None = None, props = None) -> str:
        super().__init__(tag, value, tag, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        
        if not self.tag:
            return self.value
        
        final = f'<{self.tag}'

        final += super().props_to_html()

        return final + f'>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
