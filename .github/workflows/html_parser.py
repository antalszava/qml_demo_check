from html.parser import HTMLParser
from html.entities import name2codepoint

class DemoOutputParser(HTMLParser):
    """An HTML parser class that helps parse the output of demonstrations from
    the QML repository."""
    
    is_demo_output = False
    '''Specifies whether the tag that is being parsed is the output of a cell
    in the demo.'''
    
    def __init__(self):
        self.data = []
        '''Stores the output data of demonstrations extracted from the HTML
        file of a demonstration.'''

        self.is_demo_output = False
        '''Specifies whether the tag that is being parsed is the output of a cell
        in the demo.'''

        super().__init__()
    
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            sphinx_script_output_tag = "sphx-glr-script-out"
            out = any(sphinx_script_output_tag in a for a in attr if a is not None)

            # The HTML produced by Sphinx has class HTML tags and the
            # sphx-glr-script-out attribute
            if "class" in attr and out:
                self.is_demo_output = True

    def handle_data(self, data):
        if self.is_demo_output:
            self.data.append(data)
            self.is_demo_output = False
