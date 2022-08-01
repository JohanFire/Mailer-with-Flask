from distutils.log import error
import email
from sqlite3 import connect
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for
)
from mailer.db import get_db

bp = Blueprint("mail", __name__, url_prefix="/")

@bp.route("/", methods=["GET"])
def index():
    db, c = get_db()
    c.execute(
        "SELECT * FROM email"
    )
    mails = c.fetchall()

    print(mails)
    return render_template("mails/index.html", mails=mails)

@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []

        if not email:
            errors.append("Ingresa un correo")
        if not subject:
            errors.append("El asunto es obligatorio")
        if not content:
            errors.append("El contenido es obligatorio")


        if len(errors) == 0:
            db, c = get_db()
            c.execute(
                "INSERT INTO email (email, subject, content) VALUES (%s, %s, %s)", (email, subject, content)
            )
            db.commit()

            return redirect(url_for("mail.index"))
        else:
            print(errors)
            for error in errors:
                flash(error)

        # print(email, subject, content)

    return render_template("mails/create.html")