from tabla_usuarios.configuracion.mysqlconnection import BaseDeDatos
class Cliente:
    def __init__(self,data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.creado_en=data['creado_en']
        self.actualizado_en=data['actualizado_en']
    @classmethod
    def create(cls,data):
        query='INSERT INTO datos_clientes(nombre,apellido,email)values(%(nombre)s,%(apellido)s,%(email)s);'
        resultado = BaseDeDatos('clientes').query_db(query, data)
        return resultado

    @classmethod
    def read_clientes(cls):
        query = 'SELECT * FROM datos_clientes;'
        resultados = BaseDeDatos('clientes').query_db(query)
        clientes = []
        for resultado in resultados:
            clientes.append(cls(resultado))
        return clientes

    @classmethod
    def update(cls, data):
        query = 'UPDATE datos_clientes SET nombre=%(nombre)s, apellido=%(apellido)s,email=%(email)s, creado_en=%(creado_en)s, usuarios_id=%(usuarios_id)s WHERE id=%(id)s ;'
        resultado = BaseDeDatos('clientes').query_db(query, data)
        return resultado

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM recetas WHERE id=%(id)s;'
        resultado = BaseDeDatos('clientes').query_db(query, {'id': data})
        return resultado
