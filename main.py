import flask
import replit
from dictionary import search

#from allwords  import words_all
#words_all()

app = flask.Flask(__name__)

def file_open(filename):
  with open(filename) as f:
    return str(f.read())
    
@app.route("/")
@app.route("/home")
def index():
  return file_open('index.html')

@app.route("/icon.png")
@app.route("/favicon.ico")
@app.route("/icon")
@app.route("/favicon")
def icon():
  return flask.send_file("icon.png")
  
@app.route("/file")
def file():
  name = flask.request.args.get('name')
  type = flask.request.args.get('type')
  if name:
    if type == "image":
      return flask.send_file(name)
    return file_open(name)
  return flask.redirect("/home")
  
@app.route("/about")
def about():
  content = "This Application is for the compliance of our subject HCI101 <br> Made by Canoy, Dupay, & Tabigne <br> Submitted to Sir Wilz<br>Source Code: <a style='color: black' href='https://github.com/frannytabigs/dictionary' target='/'>https://github.com/frannytabigs/dictionary (Click Me!)</a><br>Contact Us through <a href='https://www.facebook.com/franny.bolantoy' target='/' style='color: black' >FB! (Click Me!)</a>"  index = file_open("index.html")
  index = index.replace('Click the image to load all the words! Loading may take a while<img src="/icon.png" style="width: 100%;" onclick="explore(\'open\')">',content,1)
  return index

@app.route('/results')
def results():
  word = flask.request.args.get('word')
  if not word:
    return flask.redirect("/home")
  
  try:
    content = search(word).replace("\n","<br>")
  except:
    content = "Oops, word not found <br>" + word.upper() + " not found"
  desc = content.replace('<br>','\n')
  index = file_open("index.html")
  index = index.replace('Click the image to load all the words! Loading may take a while<img src="/icon.png" style="width: 100%;" onclick="explore(\'open\')">',content,1)
  index = index.replace('placeholder="Search for a word"','placeholder="'+word.upper()+'"',1)
  index = index.replace("content='Search for the meaning, synonym, and antonym of a word'", f"content='{desc}'",1)
  index = index.replace("<title>Dictionary</title>",f"<title>Dictionary | {word.upper()}</title>",1)
  return index
  
@app.route("/allwords")
def test(): 
  return file_open("allwords.html")
  
@app.errorhandler(500)
def errorweb(error):
  with open('errors.txt',"r") as f:
    x = str(f.read())
  with open('errors.txt',"w") as f:
    f.write(x + f"\n\n {error}" )
  
  return flask.redirect("/home")

@app.errorhandler(404)
def unknown(error):
  return errorweb(error)

replit.web.run(app)

