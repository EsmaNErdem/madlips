from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "Smokeythewetnosekitty"
debug = DebugToolbarExtension(app)

@app.route('/')
def select_story():
    """Shows story options"""

    return render_template("stories.html", stories = stories.values())

@app.route("/answer")
def fill_answer():
    """Shows the  prompt answer form"""
    story_id = request.args['story_id']
    story = stories[story_id]
    
    return render_template("answer.html", story_id = story_id, title= story.title, prompts = story.prompts)

@app.route("/your_story")
def get_story():
    """Generates the story and shows on the browser"""
    story_id = request.args['story_id']
    story = stories[story_id]
    text = story.generate(request.args)
    return render_template("your_story.html",
                           title=story.title,
                           text=text)

    
