from flask import Flask


def create_app():
    app=Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='dev'
    )

    # Registrar Blueprint
    from . import loteria
    app.register_blueprint(loteria.bp)
    

    @app.route('/')
    def index():
        return 'Hola mundo'


    return app


