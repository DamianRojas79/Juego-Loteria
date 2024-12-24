from flask import Blueprint

#bp=Blueprint('loteria',__name__, url_prefix='/loteria')
bp=Blueprint('loteria',__name__)


@bp.route('/list')
def index():
    return 'Lista de lineas jugadas'

@bp.route('/jugadores')
def lista_jugadores():
    return 'Lista jugadores'


