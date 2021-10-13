from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    
    were_in = False
    
    def __init__(self):
        self.data = []
        super().__init__()
    
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            out = any("sphx-glr-script-out" in a for a in attr if a is not None)
            if "class" in attr and out:
                self.were_in = True

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.were_in:
            self.data.append(data)
            self.were_in = False

    def handle_comment(self, data):
        pass

    def handle_entityref(self, name):
        pass

    def handle_charref(self, name):
        pass

    def handle_decl(self, data):
        pass
