from flask import Flask, render_template, request, redirect
from flask import session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Jump Man', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS4')
jogo3 = Jogo('Mortal Kombat 2', 'Fight', 'PS2')
lista = [jogo1, jogo2, jogo3]


# Novo objeto sendo instanciado
app = Flask(__name__)
app.secret_key = 'Rsant'


@app.route('/')
def index():
    return render_template('Lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


#Tela de Login
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '1234' == request.form['senha']:

        session['usuario_logado'] = request.form['usuario']

        flash(session['usuario_logado'] + ' Logado com SUCESSO!')
        return redirect('/')

    else:
        flash('Usuário não logado')
        return redirect('/login')


@app.route('/logout')
def logout():
    # Deslogar da Sessão
    session['usuario_logado'] = None
    flash('Logout efetuado com Sucesso!')
    return redirect('/')


#Rodar a aplicação
app.run(debug=True, host='0.0.0.0', port=8080)