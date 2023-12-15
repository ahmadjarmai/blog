from flask import Flask
app = Flask(__name__)

@app.route('/')
def list():
    return 'Hello World!'

@app.route('/detail/<int:id>/')
def detail(id):
    return 'welcome to details'

@app.route('/create', methods=['GET', 'POST'])
def create():
    return 'welcome to create'

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    return 'welcome to update'

@app.route('/delete/<int:id>/', methods=['POST'])
def delete():
    return 'welcome to delete'

if __name__ == '__main__':
    app.run(debug=True)