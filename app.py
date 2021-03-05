
# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'escritorio1000'
app.config['MYSQL_DB'] = 'foro'
mysql = MySQL(app)


# starting the app
if __name__ == "__main__":
    app.run(port=80, debug=True)