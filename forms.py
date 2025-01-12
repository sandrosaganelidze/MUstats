from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo


class AddArtistForm(FlaskForm):
    name = StringField("Artist Name", validators=[DataRequired()])
    id = StringField("ID", validators=[DataRequired()])
    streams = StringField("Stream", validators=[DataRequired()])
    submit = SubmitField('Add Album')



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    repeat_password = PasswordField("Repeat Password",validators=[DataRequired(), EqualTo('password', message="not the same password")])
    submit = SubmitField("Register")


class AlbumRegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    repeat_password = PasswordField("Repeat Password",validators=[DataRequired(), EqualTo('password', message="not the same password")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("login")


class AlbumloginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("login")
