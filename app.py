from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, News, Tender, Headlines

# bind our database to a engine that we can perform operation.
engine = create_engine('sqlite:///semari.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)


@app.route("/")
def index():
    session = DBSession()
    newsCursor = session.query(News).order_by(News.id.desc()).limit(6).all()
    tenderCursor = session.query(Tender).order_by(Tender.id.desc()).limit(4).all()
    headlinesCursor = session.query(Headlines).order_by(Headlines.id.desc()).limit(4).all()
    session.close()
    return render_template('index.html', news=newsCursor, tender=tenderCursor, headlines=headlinesCursor)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/schemes")
def scheme():
    return render_template("schemes.html")


@app.route("/rules")
def rules():
    return render_template("rules.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/news")
def news():
    return render_template("post.html", data="news")


@app.route("/tender")
def tender():
    return render_template("post.html", data="tender")


@app.route("/headlines")
def headlines():
    return render_template("post.html", data="headlines")


@app.route("/dbentry", methods=["GET", "POST"])
def dbentry():
    if (request.method == "POST"):
        if request.form['datatype'] == 'news':
            session = DBSession()
            newsObj = News(link=request.form['link'], post=request.form['post'])
            session.add(newsObj)
            session.commit()
            session.close()
            return redirect(url_for("index"))
        if request.form['datatype'] == 'tender':
            session = DBSession()
            tenderObj = Tender(link=request.form['link'], post=request.form['post'])
            session.add(tenderObj)
            session.commit()
            session.close()
            return redirect(url_for("index"))
        if request.form['datatype'] == 'headlines':
            session = DBSession()
            headObj = Headlines(link=request.form['link'], post=request.form['post'])
            session.add(headObj)
            session.commit()
            session.close()
            return redirect(url_for("index"))
    else:
        return render_template("dbentry")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
