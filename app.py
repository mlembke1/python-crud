####### IMPORTING DEPENDENCIES #########
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Entries
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

Entries = Entries()

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
    return render_template('journal_entry.html', id=id)


#  CREATE A NEW JOURNAL ENTRY
@app.route('/create', methods=['GET', 'POST'])
def createNewEntry():
    form = newEntryForm(request.form)
    # if request.method == 'POST' and form.validate():

    return render_template('create.html', form=form)


############## RUN THE APP ###############
if __name__ == '__main__':
    app.run(debug=True)
