from flask import Blueprint, flash, render_template, request, redirect, session, url_for
from models import Barang, Database, User

barang_controller = Blueprint('barang_controller', __name__)

@barang_controller.route('/')
def landing_page():
    return render_template('landing-page.html')

@barang_controller.route('/dashboard')
def dashboard():
    """Dashboard hanya menampilkan barang yang dipinjam."""
    if 'username' not in session:
        return redirect(url_for('barang_controller.login'))
    
    barangs_dipinjam = Barang.get_barang_by_status('Dipinjam')
    return render_template('dashboard.html', barangs=barangs_dipinjam)


@barang_controller.route('/barang')
def index():
    barangs = Barang.get_all_barang()
    return render_template('index.html', barangs=barangs)

@barang_controller.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        jumlah = request.form['jumlah']
        kondisi = request.form['kondisi']
        gambar = request.files['gambar'].filename
        boleh_dipinjam = True if request.form.get('boleh_dipinjam') == 'on' else False
        new_barang = Barang(kode, nama, jumlah, kondisi, gambar, boleh_dipinjam)
        Barang.create_barang(new_barang)
        return redirect(url_for('barang_controller.index'))
    return render_template('create.html')

@barang_controller.route('/update/<string:kode>', methods=['GET', 'POST'])
def update(kode):
    barang = Barang.get_barang(kode)
    if request.method == 'POST':
        nama = request.form['nama']
        jumlah = request.form['jumlah']
        kondisi = request.form['kondisi']
        status = request.form['status']
        gambar = request.files['gambar'].filename if request.files['gambar'].filename else barang[5]
        boleh_dipinjam = True if request.form.get('boleh_dipinjam') == 'on' else False
        updated_barang = Barang(kode, nama, jumlah, kondisi, gambar, boleh_dipinjam, status)
        Barang.update_barang(kode, updated_barang)
        return redirect(url_for('barang_controller.index'))
    return render_template('update.html', barang=barang)


@barang_controller.route('/delete/<string:kode>', methods=['POST'])
def delete(kode):
    Barang.delete_barang(kode)
    return redirect(url_for('barang_controller.index'))

@barang_controller.route('/update_status/<kode>', methods=['POST'])
def update_status(kode):
    """Mengupdate status barang."""
    status = request.form['status']
    db = Database()
    db.cursor.execute("UPDATE barang SET status = %s WHERE kode = %s", (status, kode))
    db.connection.commit()
    db.close()
    return redirect(url_for('barang_controller.index'))


@barang_controller.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.verify_password(username, password):
            session['username'] = username
            return redirect(url_for('barang_controller.dashboard'))
        else:
            flash('Periksa lagi username dan password', 'error')
    
    return render_template('login.html')

@barang_controller.route('/logout')
def logout():
    """User logout route."""
    session.pop('username', None)
    return redirect(url_for('barang_controller.landing_page'))

@barang_controller.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        User.create_user(username, password)
        return redirect(url_for('barang_controller.login'))
    
    return render_template('register.html')

@barang_controller.route('/change-password', methods=['GET', 'POST'])
def change_password():
    """Route for changing password."""
    if 'username' not in session:
        return redirect(url_for('barang_controller.login'))

    if request.method == 'POST':
        username = session['username']
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        
        if User.verify_password(username, old_password):
            User.update_password(username, new_password)
            flash('Password changed successfully', 'success')
            return redirect(url_for('barang_controller.dashboard'))
        else:
            flash('Old password is incorrect', 'error')
    
    return render_template('change_password.html')
