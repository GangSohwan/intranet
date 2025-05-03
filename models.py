from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 사용자 모델
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    nickname = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), nullable=False)  # 관리자 / 감사팀 / 경찰청
    approved = db.Column(db.Boolean, default=False)
    blocked = db.Column(db.Boolean, default=False)
    block_reason = db.Column(db.String(255))
    ip_address = db.Column(db.String(64))

# 출퇴근 기록 모델
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    clock_in = db.Column(db.String(64))
    clock_out = db.Column(db.String(64))

# RP 기록 모델
class RPLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    rp_type = db.Column(db.String(64))
    result = db.Column(db.String(64))  # 성공 or 실패
    score = db.Column(db.Integer)
    timestamp = db.Column(db.String(64))

# 사건처리 보고서
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)
    timestamp = db.Column(db.String(64))
    score = db.Column(db.Integer)

# 면허 신청
class LicenseRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    license_type = db.Column(db.String(64))  # 경찰 헬기 / 시민 항공
    note = db.Column(db.Text)
    interviewer = db.Column(db.String(64))
    status = db.Column(db.String(64))  # 승인 / 반려
    timestamp = db.Column(db.String(64))
