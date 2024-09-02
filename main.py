#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')

        # Задание №2.Получаем текст
        textTop = request.form.get('textTop')
        textBottom = request.form.get('textBottom')


        # Задание №3. Получаем расположение текста
        textTop_y = request.form.get('textTop_y')
        textBottom_y = request.form.get('textBottom_y')

        # Задание №3. Получаем цвет текста
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               # отображаем выбранное изображение
                               selected_image=selected_image, 

                               # Задание №2. Отображаем текст
                                textTop=textTop,
                                textBottom=textBottom,

                               # Задание №3. Отображаем цвет 
                                selected_color=selected_color,
                               #Задание №3. Отоброжаем расположение текста
                                textTop_y=textTop_y,
                                textBottom_y=textBottom_y
                               )
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
