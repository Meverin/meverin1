from flask import Flask, render_template, request

app = Flask(__name__)

# Strona główna
@app.route('/')
def index():
    return render_template('index.html')

# Strona Lista PG
@app.route('/list_pg')
def list_pg():
    # Przykładowe miasta
    cities = ["Ostrów Wielkopolski", "Ostrzeszów", "Pleszew", "Jarocin", "Raszków", "Odolanów"]
    return render_template('list_pg.html', cities=cities)

# Strona Wyszukaj Pozycję
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        street = request.form.get('street')
        house_number = request.form.get('house_number')
        if not street or not house_number:
            return render_template('search.html', error="Proszę wypełnić wszystkie pola.")
        return f"Szukam pozycji: Ulica: {street}, Numer domu: {house_number}"
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
