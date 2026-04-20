from os import getcwd
from json import loads

class ThemeEngine:
    def __init__(self):
        super(ThemeEngine, self).__init__()
        
        self.path = f"{getcwd()}/themes/default.json"
        self.colors = None
        self.params = ["primary-color", "secondary-color", "primary-hover-color", "danger-color", "secondary-background", "primary-background", "success-color"]
        
        
        with open(self.path, "r") as colors_file:
            colors = colors_file.read()
            self.colors = loads(colors)
            
            
    def prepare_sheet(self):

        with open("./themes/default.css") as sheet:
            style_ = sheet.read()

        for param in self.params:
            style_ = style_.replace(f"${param}", self.colors[param])

        return style_
    
    def get_color(self, name: str):
        if name not in self.params:
            raise Exception("Invalid property")
        
        else:
            return self.colors[name]
