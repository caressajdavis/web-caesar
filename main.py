from flask import Flask, request
from caesar import rotate_string, rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

# rotation = "rot"
# string_input = ""

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action='/encrypt' method='POST'>

        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0">
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Submit">
      </form>
    </body>
</html>"""



@app.route("/encrypt", methods=['POST'])
def encrypt():
    text=request.form['text']
    rotation=int(request.form['rot'])

    encrypted_text=rotate_string(text, rotation)
    encrypted_string= form.format(encrypted_text)

    return encrypted_string

@app.route("/")
def index():
    encrypt_string = ""
    return form.format(encrypt_string)

app.run()