from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed


class ReviewForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired('Поле не должно быть пустым')])
    text = StringField('Текст отзыва', validators=[DataRequired('Поле не должно быть пустым')])
    score = SelectField('Ваша оценка', choices=[(i, i) for i in range(1, 11)])
    submit = SubmitField('Добавить')


class MovieForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(message='Поле не должно быть пустым')])
    description = TextAreaField('Описание', validators=[DataRequired(message='Поле не должно быть пустым')])
    image = FileField('Изображение', validators=[FileRequired(message='Поле не должно быть пустым'),
                                                 FileAllowed(['jpg', 'jpeg', 'png'], message='Неверный формат файла')])
    submit = SubmitField('Добавить фильм')




