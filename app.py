from flask import Flask

app = Flask(__name__)

@app.route("/user")
def hello_world():
    return "<p>Hello, World!</p><h1>Hello, User</h1>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f"""<table>
        <th>
            <td>
              player
            </td>
            <td>
                runs
            </td>
        </th>
        <tr>
            <td>
                {username}</td><td>100</td></tr></table>"""   


if __name__ == "__main__":
    app.run(debug=True, port=8000)