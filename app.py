from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Create a list to store the todos
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST']) #for add in todo app
def add():
    todo = request.form['todo']
    todos.append(todo)
    return redirect('/')

@app.route('/delete', methods=['POST']) # for delete in todo app
def delete():
    todo = request.form['todo']
    todos.remove(todo)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

