from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError(f"Tag is required {self.__repr__()}")
        if not self.children:
            raise ValueError(f"Children property is required {self.__repr__()}")

        final = ""
        for node in self.children:
            final += node.to_html()

        return f"<{self.tag}>{final}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode(tag:{self.tag},  children: {self.children}, props:{self.props})"
