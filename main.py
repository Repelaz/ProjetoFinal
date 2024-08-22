from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jogos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        jogos.append({"nome": nome, "genero": genero})
        return redirect(url_for('index'))

    return render_template('index.html', jogos=jogos)

@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar(index):
    jogo = jogos[index]
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        jogos[index] = {"nome": nome, "genero": genero}
        return redirect(url_for('index'))

    return render_template('edit.html', jogo=jogo)

@app.route('/deletar/<int:index>', methods=['GET'])
def deletar(index):
    jogos.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)