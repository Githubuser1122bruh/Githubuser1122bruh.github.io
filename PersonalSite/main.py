from flask import Flask, render_template, request

app = Flask(__name__)


sections = {
    "about_me": ["This is the About Me section."],
    "adventures": ["Juice", "Sock", "15 Days in Public"],
    "projects": ["Project 1", "Project 2", "Project 3"],
    "contact": ["Contact me at example@example.com"]
}

@app.route('/')
def home():

    section = request.args.get('section', 'about_me')
    items = sections.get(section, ["Section not found."])
    return render_template('index.html', items=items, section=section, sections=sections)
@app.route('/juice')
def juice():
    return render_template('juice.html')
@app.route('/about_me')
def about_me():
    return render_template('about_me.html')
if __name__ == '__main__':
    app.run(debug=True, port=5000)