from flask import Flask, render_template, request

app = Flask(__name__)
# This is a small change to trigger GitHub Actions
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        return f"<h2>Welcome to Learn DevOps, {username}!</h2>"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
