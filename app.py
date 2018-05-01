####### IMPORTING DEPENDENCIES #########
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

app = Flask(__name__)

# MYSQL CONFIGURATION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'mitch'
app.config['MYSQL_PASSWORD'] = 'mlembke1'
app.config['MYSQL_DB'] = 'entries'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# INITIATE MYSQL
mysql = MySQL(app)


######## SERVER SIDE VALIDATION FOR FORM ######
class newEntryForm(Form):
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
def journal_entries():
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

#  UPDATE A JOURNAL ENTRY
@app.route('/update')
def update():
    return render_template('update.html')

#  DELETE A JOURNAL ENTRY
# @app.route('/delete')
# def about():
#     DELETE FROM table_name
#     WHERE condition;
#     return render_template('delete.html')

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

        flash('You have posted a new journal entry!', 'success')
        redirect('/read')

    return render_template('create.html', form=form)

#  UPDATE A SPECIFIC JOURNAL ENTRY
# @app.route('/update', methods=['GET', 'POST'])
# def updateEntry():
#     form = updateEntryForm(request.form)
#     # if request.method == 'POST' and form.validate():
#
#     return render_template('update.html', form=form)


############## RUN THE APP ###############
if __name__ == '__main__':
    app.secret_key='supersecret'
    app.run(debug=True)
