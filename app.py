from flask import Flask, render_template, request, redirect, session, url_for, flash
import sqlite3
from datetime import datetime
from functools import wraps
import os

# ============================================================
#  BIN KHALID DAIRY FARM — Flask Application
# ============================================================

app = Flask(__name__)

# ── Security ────────────────────────────────────────────────
app.secret_key = os.environ.get("SECRET_KEY", "bkdf-change-this-in-production-2025!")

# ── Credentials (use env vars in production) ────────────────
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "1234")


# ============================================================
#  CONTEXT PROCESSOR — inject `now` into every template
# ============================================================

@app.context_processor
def inject_now():
    return {"now": datetime.now()}


# ============================================================
#  DATABASE
# ============================================================

def get_db() -> sqlite3.Connection:
    """Return a database connection with Row factory."""
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ============================================================
#  AUTH DECORATOR
# ============================================================

def login_required(f):
    """Redirect to login if user is not authenticated."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


# ============================================================
#  AUTH ROUTES
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("home"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["logged_in"] = True
            session["username"]  = username
            flash("Welcome back!", "success")
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password. Please try again."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out successfully.", "info")
    return redirect(url_for("login"))


# ============================================================
#  DASHBOARD / HOME
# ============================================================

@app.route("/")
@login_required
def home():
    search = request.args.get("search", "").strip()
    db     = get_db()

    # ── Fetch vouchers ───────────────────────────────────────
    if search:
        vouchers = db.execute(
            "SELECT * FROM vouchers WHERE name LIKE ? ORDER BY date DESC",
            (f"%{search}%",)
        ).fetchall()
    else:
        vouchers = db.execute(
            "SELECT * FROM vouchers ORDER BY date DESC"
        ).fetchall()

    # ── Latest voucher per customer ──────────────────────────
    latest: dict = {}
    for v in vouchers:
        name   = v["name"]
        v_date = datetime.strptime(v["date"], "%Y-%m-%d")
        if name not in latest or v_date > datetime.strptime(latest[name]["date"], "%Y-%m-%d"):
            latest[name] = v

    customers = list(latest.values())

    # ── Monthly summary ──────────────────────────────────────
    month  = datetime.now().strftime("%Y-%m")
    report = db.execute(
        """SELECT
              COALESCE(SUM(amount), 0)     AS income,
              COALESCE(SUM(total_milk), 0) AS milk,
              COUNT(*)                     AS total_vouchers
           FROM vouchers WHERE date LIKE ?""",
        (f"{month}%",)
    ).fetchone()

    # ── Total distinct customers ─────────────────────────────
    total_customers = db.execute(
        "SELECT COUNT(DISTINCT name) AS cnt FROM vouchers"
    ).fetchone()["cnt"]

    # ── Recent 5 vouchers ────────────────────────────────────
    recent = db.execute(
        "SELECT * FROM vouchers ORDER BY id DESC LIMIT 5"
    ).fetchall()

    return render_template(
        "index.html",
        customers       = customers,
        income          = report["income"],
        milk            = report["milk"],
        total_vouchers  = report["total_vouchers"],
        total_customers = total_customers,
        recent          = recent,
        search          = search,
        current_month   = datetime.now().strftime("%B %Y"),
    )


# ============================================================
#  SHARED FORM PARSER
# ============================================================

def _parse_voucher_form(form) -> dict:
    """Extract and compute all voucher fields from a POST form."""
    days  = int(form["days"])
    rate  = float(form["rate"])
    daily = float(form["daily"])
    extra = float(form["extra"])
    used  = float(form["used"])
    due   = float(form["due"])

    total_milk = (daily * days) + extra - used
    amount     = total_milk * rate
    final_bill = amount + due

    return dict(
        name       = form["name"].strip(),
        date       = form["date"],
        days       = days,
        rate       = rate,
        daily      = daily,
        extra      = extra,
        used       = used,
        due        = due,
        total_milk = round(total_milk, 2),
        amount     = round(amount, 2),
        final_bill = round(final_bill, 2),
    )


# ============================================================
#  VOUCHER — ADD
# ============================================================

@app.route("/add_voucher", methods=["POST"])
@login_required
def add_voucher():
    try:
        v  = _parse_voucher_form(request.form)
        db = get_db()
        db.execute(
            """INSERT INTO vouchers
               (name,date,days,rate,daily,extra,used,due,total_milk,amount,final_bill)
               VALUES (:name,:date,:days,:rate,:daily,:extra,:used,:due,
                       :total_milk,:amount,:final_bill)""",
            v
        )
        db.commit()
        flash(f"Voucher for <strong>{v['name']}</strong> added successfully!", "success")
    except (ValueError, KeyError) as e:
        flash(f"Error adding voucher: {e}", "danger")

    return redirect(url_for("home"))


# ============================================================
#  VOUCHER — EDIT / UPDATE
# ============================================================

@app.route("/edit/<int:voucher_id>")
@login_required
def edit(voucher_id: int):
    db   = get_db()
    data = db.execute("SELECT * FROM vouchers WHERE id = ?", (voucher_id,)).fetchone()
    if not data:
        flash("Voucher not found.", "warning")
        return redirect(url_for("home"))
    return render_template("edit.html", data=data)


@app.route("/update/<int:voucher_id>", methods=["POST"])
@login_required
def update(voucher_id: int):
    try:
        v  = _parse_voucher_form(request.form)
        db = get_db()
        db.execute(
            """UPDATE vouchers SET
               name=:name, date=:date, days=:days, rate=:rate,
               daily=:daily, extra=:extra, used=:used, due=:due,
               total_milk=:total_milk, amount=:amount, final_bill=:final_bill
               WHERE id=:id""",
            {**v, "id": voucher_id}
        )
        db.commit()
        flash(f"Voucher for <strong>{v['name']}</strong> updated successfully!", "success")
    except (ValueError, KeyError) as e:
        flash(f"Error updating voucher: {e}", "danger")

    return redirect(url_for("home"))


# ============================================================
#  VOUCHER — DELETE
# ============================================================

@app.route("/delete/<int:voucher_id>", methods=["POST"])
@login_required
def delete(voucher_id: int):
    db  = get_db()
    row = db.execute("SELECT name FROM vouchers WHERE id = ?", (voucher_id,)).fetchone()
    if row:
        db.execute("DELETE FROM vouchers WHERE id = ?", (voucher_id,))
        db.commit()
        flash(f"Voucher for <strong>{row['name']}</strong> deleted.", "info")
    else:
        flash("Voucher not found.", "warning")
    return redirect(url_for("home"))


# ============================================================
#  BILL VIEW
# ============================================================

@app.route("/bill/<int:voucher_id>")
@login_required
def bill(voucher_id: int):
    db   = get_db()
    data = db.execute("SELECT * FROM vouchers WHERE id = ?", (voucher_id,)).fetchone()
    if not data:
        flash("Voucher not found.", "warning")
        return redirect(url_for("home"))
    return render_template("bill.html", data=data)


# ============================================================
#  HISTORY — all vouchers for one customer
# ============================================================

@app.route("/history/<string:customer_name>")
@login_required
def history(customer_name: str):
    db      = get_db()
    records = db.execute(
        "SELECT * FROM vouchers WHERE name = ? ORDER BY date DESC",
        (customer_name,)
    ).fetchall()
    if not records:
        flash(f"No records found for '{customer_name}'.", "warning")
        return redirect(url_for("home"))
    return render_template("history.html", records=records, customer_name=customer_name)


# ============================================================
#  RUN
# ============================================================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)