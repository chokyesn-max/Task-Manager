from flask import Flask, render_template, request, redirect
from manager import TaskManager

app = Flask(__name__)
m = TaskManager()

@app.route("/")
def index():
    priority = request.args.get("priority")
    if priority:
        tasks = m.get_tasks_by_priority(priority)
    else:
        tasks = m.get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title").strip()
    priority = request.form.get("priority")
    deadline = request.form.get("deadline")
    if title:
        m.add_task(title, priority, deadline)
    return redirect("/")
    
@app.route("/done/<task_id>", methods=["POST"])
def done(task_id):
    m.mark_done_by_id(task_id)
    return redirect("/")

@app.route("/delete_done", methods=["POST"])
def delete_done():
    m.delete_done()
    return redirect("/")

@app.route("/edit/<task_id>", methods=["GET"])
def edit(task_id):
    task = m.get_task_by_id(task_id)
    print(f"Task: {task}")
    return render_template("edit.html", task=task)

@app.route("/edit/<task_id>", methods=["POST"])
def edit_post(task_id):
    title = request.form.get("title").strip()
    priority = request.form.get("priority")
    deadline = request.form.get("deadline")
    if title:
        m.edit_task(task_id, title, priority, deadline)
    return redirect("/")

    


if __name__ == "__main__":
    app.run(debug=True)