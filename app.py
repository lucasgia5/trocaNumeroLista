from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entrada = request.form.get('lista')
        lista = entrada.split()
        
        if len(lista) != 5:
            return render_template('index.html', error="A lista deve ter 5 números e espaço entre eles.")
        
        try:
            lista = [int(num) for num in lista]
        except ValueError:
            return render_template('index.html', error="Todos os elementos devem ser números inteiros.")
        
        primeiro_num = int(request.form.get('primeiro_num'))
        segundo_num = int(request.form.get('segundo_num'))
        
        if primeiro_num not in lista or segundo_num not in lista:
            return render_template('index.html', error="Um ou ambos os números não estão na lista.")
        
        indice_primeiro = lista.index(primeiro_num)
        indice_segundo = lista.index(segundo_num)
        lista[indice_primeiro], lista[indice_segundo] = lista[indice_segundo], lista[indice_primeiro]
        
        return render_template('index.html', lista=lista, sucesso="Lista atualizada com sucesso!")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
