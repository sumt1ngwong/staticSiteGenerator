from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is empty, all ParentNode's must have tag") 
        elif self.children is None:
            raise ValueError("Children is empty, all ParentNode must have children")
        else:
            if len(self.children) > 1:
                for x in self.children:
                    self.to_html


                    #UNFINFIHSED NEEDS COMPLTEING 