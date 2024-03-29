class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        prop_string = ""
        if self.props != None:
            for prop in self.props:
                prop_string += f" {prop}=\"{self.props[prop]}\""
        return prop_string
    
    def __repr__(self) -> str:
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nproperties: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None) -> None:
        children = None
        super().__init__(tag, value, children, props)

    def to_html(self):
        try:
            if self.value == None:
                raise ValueError("Error: Invalid HTML: no value")
            if self.tag == None:
                return self.value
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        except Exception as e:
            return e
        
    def __repr__(self) -> str:
        return f"tag: {self.tag}\nvalue: {self.value}\nproperties: {self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None) -> None:
        value = None
        super().__init__(tag, value, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Error: Node has no tag")
        if self.children == None:
            raise ValueError("Error: Empty children attribute")
        html_string = f"<{self.tag}>"
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"
        return html_string