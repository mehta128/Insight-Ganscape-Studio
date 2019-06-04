from flask import Flask, render_template, request

# Create the application object
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home_page():
    return render_template('index.html')  # render a template


@app.route('/output')
def tag_output():
    #
    # Pull input
    some_input = request.args.get('user_input')

    # Case if empty
    if some_input == '':
        return render_template("index.html",
                               my_input=some_input,
                               my_form_result="Empty")
    else:
        some_output = "yeay!"
        some_number = 3
        some_image = "giphy.gif"
        return render_template("index.html",
                               my_input=some_input,
                               my_output=some_output,
                               my_number=some_number,
                               my_img_name=some_image,
                               my_form_result="NotEmpty")


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)  # will run locally http://127.0.0.1:5000/

