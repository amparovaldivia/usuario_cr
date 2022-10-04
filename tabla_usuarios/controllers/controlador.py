from tabla_usuarios import app
from flask import render_template,redirect,request
from tabla_usuarios import modelo
from tabla_usuarios.modelo.cliente import Cliente


@app.route('/')
def ver_clientes():
    clientes=Cliente.read_clientes()
    return render_template('leer.html',datos=clientes)

@app.route('/',methods=['POST'])
def agregar_clientes():
    print(request.form)
    data={
        'nombre':request.form['nombre'],
        'apellido':request.form['apellido'],
        'email':request.form['email']
        
    }    
    Cliente.create(data)
    return redirect('/')

@app.route('/users/new')
def  traer():
    return render_template('crear.html')   