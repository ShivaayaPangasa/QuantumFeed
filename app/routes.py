from flask import Blueprint, render_template, redirect, url_for
from app import get_articles
import subprocess
import os

main = Blueprint("main", __name__)

@main.route("/")
def index():
    articles = get_articles()
    return render_template("index.html", articles=articles, year=2025)

@main.route("/refresh")
def refresh():
    fetcher_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "services", "fetcher.py"))
    python_executable = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "venv", "Scripts", "python"))

    # Pass the current environment to the subprocess
    env = os.environ.copy()

    result = subprocess.run([python_executable, fetcher_path], capture_output=True, text=True, env=env)

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    return redirect(url_for("main.index"))