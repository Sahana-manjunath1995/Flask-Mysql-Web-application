# from distutils.log import debug
import logging
from flask import Flask, render_template, jsonify
import config
from flask import request


app = Flask(__name__)

logger = logging.getLogger()

conn =  config.connect()
cur = conn.cursor()


@app.route('/columns', methods=['GET'])
def get_column():
    table_name = "movieref_table"
    cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_lis = []
    for row in cur:
        for x in row:
            app.logger.info('Value of row accessed')
        column_lis.append(str(x))
    print(column_lis)
    resp = jsonify(column_lis)
    print(resp)

    return resp


class Queries:
    Movie = "select title from movie_title where type = 'Movie' and title like '%{}%' limit 5"
    Director = "select director from movie_director where director like '%{}%' limit 5"
    Actor = "select cast from movie_cast where cast like '%{}%' limit 5"
    TV_show = "select title from movie_title where type = 'TV Show' and title like '%{}%' limit 5"


class Final_query:
    Movie = "select show_id, type, title from movie_title where type = 'Movie' and title like '%{}%'"
    " order by {column_name} {sort_column}  limit 10"
    Director = "select movie_title.show_id, movie_title.type, movie_title.title, movie_director.director from movie_title join movie_director on movie_title.show_id = movie_director.show_id where movie_director.director like '%{}%'  order by {column_name} {sort_column} limit 10"
    Actor = "select movie_title.show_id, movie_title.type, movie_title.title, movie_cast.cast from movie_title join movie_cast on movie_title.show_id = movie_cast.show_id where movie_cast.cast like '%{}%'  order by {column_name} {sort_column} limit 10"
    TV_show = "select show_id, type, title from movie_title where type = 'TV Show' and title like '%{}%' order by {column_name} {sort_column} limit 10"



@app.route('/')
def index():
    return render_template('movie.html')


@app.route('/search', methods=['GET', 'POST'])
def movies():
    search = request.form.get("search")
    type = request.form.get("type")
    query = getattr(Queries, type )

    cur.execute(query.format(search))
    result = cur.fetchall()
    return jsonify(result)


@app.route('/datasearch', methods=['GET', 'POST'])
def search_data():
    search = request.form.get("search")
    app.logger.info('The value of the search is accessed')
    type = request.form.get("type")
    app.logger.info('The value of the type is accessed')
    sorted = request.form.get("sorted")
    app.logger.info('The value of the sorted is accessed')
    columns = request.form.get("columns")
    app.logger.info('The value of the columns is accessed')

    query = getattr(Final_query, type )

    cur.execute(query.format(search, column_name = columns, sort_column = sorted))
    result = cur.fetchall()
    app.logger.info('sorted result is accessed')
    return jsonify(result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



