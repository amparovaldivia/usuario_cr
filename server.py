from doctest import debug
from tabla_usuarios import app
from tabla_usuarios.controllers import controlador
if __name__=='__main__':
    app.run(debug=True)