class HTMLNode:
    def __init__(self, tag=None, attributes=None, children=None, props=None):
        self.tag = tag
        self.attributes = attributes
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # return a string of HTML attributes
        if self.props is None:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.attributes}, {self.children}, {self.props})"
