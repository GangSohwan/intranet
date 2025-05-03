from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length

# 로그인 폼
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('로그인')

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    nickname = StringField('닉네임', validators=[DataRequired(), Length(max=20)])
    unique_id = IntegerField('고유번호', validators=[DataRequired()])
    submit = SubmitField('회원가입')

# RP 기록 폼
class RPForm(FlaskForm):
    rp_type = SelectField('RP 유형', choices=[], validators=[DataRequired()])
    result = SelectField('결과', choices=[('성공', '성공'), ('실패', '실패')])
    submit = SubmitField('기록')

# 사건처리 보고서 폼
class ReportForm(FlaskForm):
    title = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    submit = SubmitField('보고')

# 면허 신청 폼
class LicenseForm(FlaskForm):
    license_type = SelectField('면허 종류', choices=[('경찰 헬기', '경찰 헬기'), ('시민 항공', '시민 항공')])
    note = TextAreaField('메모', validators=[DataRequired()])
    interviewer = StringField('면접관', validators=[DataRequired()])
    submit = SubmitField('신청')

# 법률 계산기 폼
class LawCalcForm(FlaskForm):
    crime = SelectField('범죄 선택', choices=[], validators=[DataRequired()])
    newbie_protection = BooleanField('신입 보호법 적용')
    submit = SubmitField('계산')
