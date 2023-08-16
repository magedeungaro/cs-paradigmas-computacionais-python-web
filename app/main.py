from flask import Flask, request, render_template
 
app = Flask(__name__)
app.debug = True
 
@app.route('/')
def index():
    return render_template('application.html')
 
@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return render_template('ola.html', nome=nome)
 
@app.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return "Recebeu post! Fazer login!"
    else:
        return "Recebeu get! Exibir FORM de login."
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)