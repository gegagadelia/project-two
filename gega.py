from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def programming_language():

    programming_languages = [
    {'name': 'python', 'description': 'blablabla', 'link': "https://www.python.org/"},
    {'name': 'PHP', 'description': 'blablabla', 'link': "https://www.php.net/"},
    {'name': 'java', 'description': 'blablabla', 'link': "https://www.java.com/"},
    {'name': 'C#', 'description': 'blablabla', 'link': "https://en.wikipedia.org/wiki/C_Sharp_(programming_language)"},
    {'name': 'ruby', 'description': 'blablabla', 'link': "https://www.ruby-lang.org/en/"}
    
    ]

    return render_template('gegaindex.html', programming_languages=programming_languages)
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)