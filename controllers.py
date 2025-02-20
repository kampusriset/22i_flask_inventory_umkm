from flask import Blueprint, flash, render_template, request, redirect, session, url_for
from models import Barang, Database, User, Peminjam
from flask import request, jsonify

barang_controller = Blueprint('barang_controller', __name__)

@barang_controller.route('/')
def landing_page():
    return render_template('landing-page.html')

@barang_controller.route('/dashboard')
def dashboard():
    """Dashboard hanya menampilkan barang yang dipinjam."""
    if 'username' not in session:
        return redirect(url_for('barang_controller.login'))
    
    total_jenis = Barang.get_total_jenis_barang()[0]['jumlah_jenis_barang']
    total_barang_tersedia = Barang.get_total_barang_tersedia()[0]['total_barang_tersedia']
    total_barang_dipinjam = Barang.get_barang_dipinjam()[0]['barang_dipinjam']
    barang_dipinjam = Barang.get_barang_by_status("Dipinjam")
    return render_template('dashboard.html', username=session['username'], total_jenis=total_jenis, barang_tersedia=total_barang_tersedia, barang_dipinjam=total_barang_dipinjam, barangs = barang_dipinjam)


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

@barang_controller.route('/pinjam_barang/<string:kode>', methods=['POST'])
def pinjam_barang(kode):
    if 'username' not in session:
        return redirect(url_for('barang_controller.login'))
    
    jumlah_pinjam = int(request.form['jumlah_pinjam'])
    peminjam = session['username'] 

    Barang.pinjam_barang(kode, jumlah_pinjam, peminjam)
    return redirect(url_for('barang_controller.index'))

@barang_controller.route('/peminjam', methods=['GET', 'POST'])
def kelola_peminjam():
    if request.method == 'POST':
        nm_peminjam = request.form['nama_peminjam']
        nm_brg = request.form['nama_barang_dipinjam']
        jml_brg = request.form['jumlah_barang_dipinjam']
        nmr_telp = request.form['nomor_telepon']
        identitas = request.files['identitas'].filename
        tgl_pinjam = request.form['tanggal_pinjam']
        tgl_kembali = request.form['tanggal_kembali']
        new_peminjam = Peminjam(nm_peminjam, nm_brg, jml_brg, nmr_telp, identitas, tgl_pinjam, tgl_kembali)
        Peminjam.create_peminjam(new_peminjam)

    
    barang_tersedia = Barang.get_barang_tersedia() 
    data_peminjam = Peminjam.get_all_peminjam()
    return render_template('peminjam.html',barang_tersedia = barang_tersedia, list_peminjam = data_peminjam)
    
@barang_controller.route('/selesai_pinjam/<string:id_peminjam>', methods=['POST'])
def selesai_pinjam(id_peminjam):
    Peminjam.selesai_pinjam(id_peminjam)
<<<<<<< HEAD
    return redirect(url_for('barang_controller.peminjam'))

@barang_controller.route('/pinjam', methods=['POST'])
def pinjam_barang():
    kode = request.form['kode']
    jumlah = int(request.form['jumlah'])
    peminjam = "User123"  # Gantilah dengan sistem autentikasi user

    Barang.pinjam_barang(kode, jumlah, peminjam)

    # Ambil jumlah terbaru
    db = Database()
    db.cursor.execute("SELECT jumlah FROM barang WHERE kode = %s", (kode,))
    new_jumlah = db.cursor.fetchone()[0]
    db.close()

    return jsonify({"success": True, "new_jumlah": new_jumlah})
=======
    return redirect(url_for('barang_controller.kelola_peminjam'))

@barang_controller.route('/update_peminjam/<string:id_peminjam>', methods=['GET', 'POST'])
def update_peminjam(id_peminjam):
    peminjam = Peminjam.get_peminjam(id_peminjam)
    barang_tersedia = Barang.get_barang_tersedia() 

    if request.method == 'POST':
        nm_peminjam = request.form['nama_peminjam']
        nm_brg = request.form['nama_barang_dipinjam']
        jml_brg = request.form['jumlah_barang_dipinjam']
        nmr_telp = request.form['nomor_telepon']
        tgl_pinjam = request.form['tanggal_pinjam']
        tgl_kembali = request.form['tanggal_kembali']

        file_identitas = request.files['identitas']
        identitas = file_identitas.filename if file_identitas.filename else peminjam['identitas'] 

        updated_peminjam = Peminjam(nm_peminjam, nm_brg, jml_brg, nmr_telp, identitas, tgl_pinjam, tgl_kembali)
        Peminjam.update_peminjam(id_peminjam, updated_peminjam)
        return redirect(url_for('barang_controller.kelola_peminjam'))

    return render_template('update_peminjam.html', peminjam=peminjam, barang_tersedia=barang_tersedia)
>>>>>>> 530bf3fa56678e540e336c608f0ce0eea2c87e3d
