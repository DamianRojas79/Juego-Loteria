from flask import Flask, render_template

from . import auth


def create_app():
    app=Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='dev'
    )

    # Registrar Blueprint modulo lotería
    from . import loteria
    app.register_blueprint(loteria.bp)

    # Registrar Blueprint modulo auth
    from . import auth
    app.register_blueprint(auth.bp)


    @app.route('/')
    def index():
        return render_template ('index.html')


    return app


