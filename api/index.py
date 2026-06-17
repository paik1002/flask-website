from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/about")
def about():

    return "About Page"


# Vercel 실행용
def handler(request):
    return app(request.environ, lambda status, headers: None)
