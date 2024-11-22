# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Formularz z rezultatami
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # odczytywanie wybranego obrazka
        selected_image = request.form.get('image-selector')

        # Zadanie #2. Odczytywanie tekstu
        text_top = request.form["textTop"]
        text_bottom = request.form["textBottom"]

        # Zadanie #3. Odczytywanie pozycji tekstu
        selected_color = request.form["color-selector"]

        # Zadanie #3. Odczytywanie koloru tekstu
        top_y = request.form["textTop_y"]
        bottom_y = request.form["textBottom_y"]

        return render_template('index.html', 
                               # Wyświetlanie wybranego obrazka
                               selected_image=selected_image, 

                               # Zadanie #2. Wyświetlanie tekstu
                               text_top=text_top,
                               text_bottom=text_bottom,

                               # Zadanie #3. Wyświetlanie koloru
                               selected_color=selected_color,
                               
                               # Zadanie #3. Wyświetlanie pozycji tekstu
                               top_y=top_y,
                               bottom_y=bottom_y
                               )
    else:
        # Wyświetlanie pierwszego obrazka, jako grafika domyślna
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
