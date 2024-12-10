import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

try:
    # Conexión a MongoDB Atlas (ya configurada con la URI)
    client = MongoClient("mongodb+srv://Jhosuan:Jhosuan@cluster.ftalklb.mongodb.net/Sistema", 
                         tls=True, tlsAllowInvalidCertificates=True)
    client.server_info()
    print("Conexión exitosa a la base de datos MongoDB")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")

db = client['Sistema']

from routes.inventarioRoutes import inventario_blueprint
from routes.facturasRoutes import facturas_blueprint
from routes.clientes import clientes_blueprint
from routes.usuarioRoutes import usuarios_blueprint
app.register_blueprint(inventario_blueprint, url_prefix='/api/inventario')
app.register_blueprint(facturas_blueprint, url_prefix='/api/facturas')
app.register_blueprint(clientes_blueprint, url_prefix='/api/clientes')
app.register_blueprint(usuarios_blueprint, url_prefix='/api/usuarios')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

