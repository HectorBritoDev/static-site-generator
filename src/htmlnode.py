class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list['HTMLNode'] | None = None,
        props: dict | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        
        final: str = ''

        if not self.props:
            return final

        for propKey in self.props:
            final +=  f' {propKey}="{self.props[propKey]}"'

        return final

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"