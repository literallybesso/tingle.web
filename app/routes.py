from flask import Blueprint, render_template, send_from_directory, current_app

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/features')
def features():
    return render_template('features.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/download')
def download():
    return send_from_directory(
        directory=current_app.root_path + '/static',
        path='test_image.zip',  # Replace with the actual file name
        as_attachment=True
    )
