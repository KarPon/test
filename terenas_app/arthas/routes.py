from arthas import app

@app.route('/')
@app.route('/index')
def index():
   return "Let them come!"
