from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is empty, all leaf nodes must have a value.")
        elif self.tag is None:
            return self.value
        else:
            if self.props is None:        
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                #add space here between the tag 
                return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
         


