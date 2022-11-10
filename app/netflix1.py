from distutils.log import debug
from socket import socket
from flask import Flask, render_template, jsonify
# import pymysql.cursors
import mysql.connector
from flask import request


app = Flask(__name__)

# conn = pymysql.connect(
#     host='db',
#     user='root',
#     password='root',
#     port=3306,
#     database='Movies'

# )
conn = mysql.connector.connect(
    host='db',
    user='root',
    password='root',
    port=3306,
    database='Movies'
)
cur = conn.cursor()

@app.route('/columns', methods=['GET'])
def get_column():
    table_name = "movieref_table"
    cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
    column_lis = []
    for row in cur:
        for x in row:
            print(x)
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
    print(search)
    type = request.form.get("type")
    print(type)
    sorted = request.form.get("sorted")
    print(sorted)
    columns = request.form.get("columns")
    print(columns)

    query = getattr(Final_query, type )

    cur.execute(query.format(search, column_name = columns, sort_column = sorted))
    result = cur.fetchall()
    print(result)
    return jsonify(result)




if __name__ == "__main__":

   app.run(host="0.0.0.0", debug=True)



