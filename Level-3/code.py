import os
from flask import Flask, request  

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

def valid_path(path=None):
    return os.path.exists(path)

def accessible_file(path=None):
    return path in ["assets/tax_form.pdf", "assets/prof_picture.png"]

class TaxPayer:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set        
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass
        
        # defends against path traversal attacks
        if not valid_path(path) or not accessible_file(path):
            raise Exception("Error: Invalid or Inaccessible path")
        
        # builds path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))
        
        with open(prof_picture_path, 'rb') as pic:
            picture = bytearray(pic.read())

        # assume that image is returned on screen after this
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None
        
        if not path:
            raise Exception("Error: Tax form is required for all users")
       
        # defends against path traversal attacks
        if not valid_path(path) or not accessible_file(path):
            raise Exception("Error: Invalid or Inaccessible path")

        with open(path, 'rb') as form:
            tax_data = bytearray(form.read())

        # assume that taxa data is returned on screen after this
        return path