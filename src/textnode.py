from enum import Enum

class TextType(Enum):
    PLAIN = 'plain'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class MarkdownType(Enum):
    PLAIN = ""
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    
    LINK = 'link'
    IMAGE = 'image'

TEXT_REPLACEMENT_KEYWORD = "TEXT_HERE"

class TextNode:
    def __init__(self, text: str, text_type: str, url:str):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value: TextNode):
        return self.text == value.text and self.text_type.value == value.text_type.value and self.url == value.url

    def __repr__(self):
        return f"{type(self).__name__}({self.text}, {self.text_type.value}, {self.url})"

    def getTextWrapper(self, text: str, type: TextType, url: str):
        match type:
            case 'plain' | 'bold' | 'italic' | 'code':
                return self.simpleTextWrapper(self.text, self.text_type)
            case 'link':
                return f"[{text}]({url})"
            case 'image':
                return f"![{text}]({url})"

    def simpleTextWrapper(self, text: str, type: str):
        return "{0}{1}{0}".format(TextType[type].value, text)
         

                