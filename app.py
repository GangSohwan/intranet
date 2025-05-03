import os
import json
from collections import defaultdict
from flask import Flask, render_template, redirect, url_for, session

# 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask 앱 생성 시 템플릿/정적 경로 지정
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)
app.secret_key = 'super_secret_key'  # 실제 운영 시 환경변수 사용 권장

# 블루프린트 임포트
from routes.auth import auth_bp
from routes.attendance import attendance_bp
from routes.rp import rp_bp
from routes.report import report_bp
from routes.law import law_bp
from routes.notices import notice_bp
from routes.license import license_bp
from routes.audit import audit_bp
from routes.admin import admin_bp
from routes.side_notices import side_bp
from routes.admin_side_notice import admin_side_notice_bp

# 블루프린트 등록
app.register_blueprint(auth_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(rp_bp)
app.register_blueprint(report_bp)
app.register_blueprint(law_bp)
app.register_blueprint(notice_bp)
app.register_blueprint(license_bp)
app.register_blueprint(audit_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(side_bp)
app.register_blueprint(admin_side_notice_bp)

# JSON 로딩 함수
def load_json(filename):
    path = os.path.join(BASE_DIR, 'database', filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def find_nickname(user_id, users):
    for user in users:
        if str(user['id']) == str(user_id):
            return user['nickname']
    return '알 수 없음'

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    users = load_json('users.json')
    attendance = load_json('attendance.json')
    rp_logs = load_json('rp_logs.json')
    reports = load_json('reports.json')

    attendance_count = defaultdict(int)
    for log in attendance:
        if 'user_id' in log:
            attendance_count[str(log['user_id'])] += 1

    attendance_rank = sorted(
        [{'nickname': find_nickname(uid, users), 'count': count}
         for uid, count in attendance_count.items()],
        key=lambda x: x['count'], reverse=True
    )

    rp_score = defaultdict(int)
    for rp in rp_logs:
        if 'user_id' in rp and 'score' in rp:
            rp_score[str(rp['user_id'])] += rp['score']

    rp_rank = sorted(
        [{'nickname': find_nickname(uid, users), 'score': score}
         for uid, score in rp_score.items()],
        key=lambda x: x['score'], reverse=True
    )

    report_count = defaultdict(int)
    for rpt in reports:
        if 'user_id' in rpt:
            report_count[str(rpt['user_id'])] += 1

    report_rank = sorted(
        [{'nickname': find_nickname(uid, users), 'count': count}
         for uid, count in report_count.items()],
        key=lambda x: x['count'], reverse=True
    )

    return render_template(
        'dashboard.html',
        attendance_rank=attendance_rank,
        rp_rank=rp_rank,
        report_rank=report_rank
    )

if __name__ == '__main__':
    app.run(debug=True)
