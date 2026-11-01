from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str | None = None, props = None) -> str:
        super().__init__(tag=tag, value=value,props= props)
    
    def to_html(self):
        if not self.value:
            raise ValueError(f"Value property is required {self.__repr__()}")
        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag:{self.tag}, value:{self.value}, props:{self.props})"
