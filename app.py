from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app=Flask(__name__,template_folder='TEMPLATE')

MySQL= MySQL()
app.config ['MYSQL_DATABASE_HOST']= 'Localhost'
app.config ['MYSQL_DATABASE_USER']= 'root'
app.config ['MYSQL_DATABASE_PASSWORD']= ''
app.config ['MYSQL_DATABASE_BD']= 'productos_demeter'
MySQL.init_app(app)







@app.route('/')
def index():
    sql= "SELECT * FROM productos_demeter.vinos;"
    conn = MySQL.connect()
    cursor = conn.cursor() 
    cursor.execute(sql) 
    productos = cursor.fetchall() 
    cursor.close()
    
    
    
    return render_template('VINOS/Indexx.html',vinos=productos)
 

if __name__=='__main__':
    app.run(debug=True)
    

    
