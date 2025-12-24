from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        # отдаём шаблон из папки templates
        return render_template("index.html")

    @app.route("/health")
    def health():
        return "ok", 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
