####### IMPORTING DEPENDENCIES #########
import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_json import FlaskJSON, json_response
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

app = Flask(__name__)
json = FlaskJSON(app)


# # MYSQL CONFIGURATION LOCAL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'mitch'
# app.config['MYSQL_PASSWORD'] = 'mlembke1'
# app.config['MYSQL_DB'] = 'entries'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# SET SECRET KEY
app.secret_key=os.environ.get('SECRET_KEY')

# MYSQL CONFIGURATION DEPLOYED
app.config['MYSQL_HOST'] = 'us-cdbr-iron-east-04.cleardb.net'
app.config['MYSQL_USER'] = 'b43c45647f5a8f'
app.config['MYSQL_PASSWORD'] = '23cb224a'
app.config['MYSQL_DB'] = 'heroku_48ce68a75f1876f.entries'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# INITIATE MYSQL
mysql = MySQL(app)



######## SERVER SIDE VALIDATION FOR FORM ######
class newEntryForm(Form):
    author = StringField('Author', [validators.Length(min=1, max=50)])
    title  = StringField('Title', [validators.Length(min=4, max=50)])
    journal_entry  = StringField('Journal Entry', [validators.Length(min=4, max=500)])

class updateEntryForm(Form):
    author = StringField('Author', [validators.Length(min=1, max=50)])
    title  = StringField('Title', [validators.Length(min=4, max=50)])
    journal_entry  = StringField('Journal Entry', [validators.Length(min=4, max=500)])


############# ROUTES #############
# GET HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')




# VIEW ALL JOURNAL ENTRIES
@app.route('/read')
def read():
        #  CREATE CURSOR
        cur = mysql.connection.cursor()

        # EXECUTE QUERY
        cur.execute('''SELECT * FROM entries''')

        #  COMMIT TO DATABASE
        mysql.connection.commit()

        Entries = cur.fetchall()

        # CLOSE THE CONNECTION
        cur.close()

        return render_template('journal_entries.html', entries = Entries)

 # UPDATE A JOURNAL ENTRY
@app.route('/update/<string:id>', methods=['PUT', 'GET'])
def update(id):
    form = updateEntryForm(request.form)
    if request.method == 'PUT':
        title = form.title.data
        author = form.author.data
        journal_entry = form.journal_entry.data
        # CREATE CURSOR
        cur = mysql.connection.cursor()

        # EXECUTE QUERIES
        cur.execute ('''UPDATE entries SET title = %s, author = %s, journal_entry = %s WHERE id=%s''', (title, author, journal_entry, id))

        #  COMMIT TO DATABASE
        mysql.connection.commit()

        # CLOSE THE CONNECTION
        cur.close()

        return json_response(message='success')

    # CREATE CURSOR
    cur = mysql.connection.cursor()

    # EXECUTE QUERIES
    cur.execute('''SELECT * FROM entries WHERE id=%s''', [id])

    #  COMMIT TO DATABASE
    mysql.connection.commit()

    Entry = cur.fetchall()

    # CLOSE THE CONNECTION
    cur.close()

    return render_template('update.html', entry = Entry[0])


 # DELETE A JOURNAL ENTRY
@app.route('/delete/<string:id>', methods=['GET', 'DELETE'])
def delete(id):
    if request.method == 'DELETE':
        # CREATE CURSOR
        cur = mysql.connection.cursor()

        # EXECUTE QUERIES
        cur.execute ('''DELETE FROM entries WHERE id=%s''', [id])

        #  COMMIT TO DATABASE
        mysql.connection.commit()

        # CLOSE THE CONNECTION
        cur.close()

        return json_response(message='success')

    # CREATE CURSOR
    cur = mysql.connection.cursor()

    # EXECUTE QUERIES
    cur.execute('''SELECT * FROM entries WHERE id=%s''', [id])

    #  COMMIT TO DATABASE
    mysql.connection.commit()

    Entry = cur.fetchall()

    # CLOSE THE CONNECTION
    cur.close()

    return render_template('delete.html', entry = Entry[0])



#  ABOUT ME
@app.route('/about')
def about():
    return render_template('about.html')







#  GET SPECIFIC JOURNAL ENTRY BY ITS ID
@app.route('/journal_entry/<string:id>/')
def journal_entry(id):
    #  CREATE CURSOR
    cur = mysql.connection.cursor()

    # EXECUTE QUERY
    cur.execute('''SELECT * FROM entries WHERE id = %s''', [id])

    #  COMMIT TO DATABASE
    mysql.connection.commit()

    entry = cur.fetchall()

    # CLOSE THE CONNECTION
    cur.close()
    return render_template('journal_entry.html', entry = entry[0])




#  CREATE A NEW JOURNAL ENTRY
@app.route('/create', methods=['GET', 'POST'])
def createNewEntry():
    form = newEntryForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        author = form.author.data
        journal_entry = form.journal_entry.data

        #  CREATE CURSOR
        cur = mysql.connection.cursor()

        # EXECUTE QUERY
        cur.execute('''INSERT INTO entries(title, author, journal_entry) VALUES(%s, %s, %s)''', (title, author, journal_entry))

        #  COMMIT TO DATABASE
        mysql.connection.commit()

        # CLOSE THE CONNECTION
        cur.close()

        return redirect('/read')

    return render_template('create.html', form=form)








#  # UPDATE A SPECIFIC JOURNAL ENTRY
# @app.route('/update', methods=['GET', 'POST'])
# def updateEntry():
#     form = newEntryForm(request.form)
#     if request.method == 'POST' and form.validate():
#         title = form.title.data
#         author = form.author.data
#         journal_entry = form.journal_entry.data
#
#         #  CREATE CURSOR
#         cur = mysql.connection.cursor()
#
#         # EXECUTE QUERY
#         cur.execute('''INSERT INTO entries(title, author, journal_entry) VALUES(%s, %s, %s)''', (title, author, journal_entry))
#         cursor.execute ("""
#            UPDATE entries
#            SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s
#            WHERE id=%s
#         """, (Year, Month, Day, Hour, Minute, id))
#
#         #  COMMIT TO DATABASE
#         mysql.connection.commit()
#
#         # CLOSE THE CONNECTION
#         cur.close()
#
#         flash('You have updated the journal entry!', 'success')
#         redirect('/read')
#     return render_template('update.html', form=form)








############## RUN THE APP ###############
if __name__ == '__main__':
    app.secret_key=os.environ.get('SECRET_KEY')
    app.run(debug=True)
