import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self):
        self.connection = MySQLdb.connect(
            host='localhost',
            user='root',
            port=3308,
            password='',
            database='inventory_ukm'
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()
    
    def fetch_as_dict(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        
        result = [dict(zip(column_names, row)) for row in rows]
        return result

class Barang:
    def __init__(self, kode, nama, jumlah, kondisi, gambar, boleh_dipinjam, status="Tersedia"):
        self.kode = kode
        self.nama = nama
        self.jumlah = jumlah
        self.kondisi = kondisi
        self.gambar = gambar
        self.boleh_dipinjam = boleh_dipinjam
        self.status = status  
    @staticmethod
    def get_all_barang():
        db = Database()
        db.cursor.execute("SELECT * FROM barang")
        barangs = db.cursor.fetchall()
        db.close()
        return barangs

    @staticmethod
    def get_barang(kode):
        db = Database()
        db.cursor.execute("SELECT * FROM barang WHERE kode = %s", (kode,))
        barang = db.cursor.fetchone()
        db.close()
        return barang

    @staticmethod
    def create_barang(barang):
        db = Database()
        db.cursor.execute("INSERT INTO barang (kode, nama, jumlah, kondisi, gambar, boleh_dipinjam, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                          (barang.kode, barang.nama, barang.jumlah, barang.kondisi, barang.gambar, barang.boleh_dipinjam, barang.status))
        db.connection.commit()
        db.close()

    @staticmethod
    def update_barang(kode, barang):
        db = Database()
        db.cursor.execute("UPDATE barang SET nama = %s, jumlah = %s, kondisi = %s, gambar = %s, boleh_dipinjam = %s, status = %s WHERE kode = %s",
                          (barang.nama, barang.jumlah, barang.kondisi, barang.gambar, barang.boleh_dipinjam, barang.status, kode))
        db.connection.commit()
        db.close()

    @staticmethod
    def delete_barang(kode):
        db = Database()
        db.cursor.execute("DELETE FROM barang WHERE kode = %s", (kode,))
        db.connection.commit()
        db.close()

    @staticmethod
    def get_barang_by_status(status):
        db = Database()
        query = "SELECT * FROM barang WHERE status = %s"
        db.cursor.execute(query, (status,))
        data = db.cursor.fetchall()
        db.close()
        return data
    
    @staticmethod
    def pinjam_barang(kode, jumlah, peminjam):
        db = Database()
        
        db.cursor.execute("SELECT jumlah FROM barang WHERE kode = %s", (kode,))
        stok_sekarang = db.cursor.fetchone()[0]
        
        if stok_sekarang >= jumlah:

            db.cursor.execute("UPDATE barang SET jumlah = jumlah - %s WHERE kode = %s", (jumlah, kode))

            db.cursor.execute(
                "INSERT INTO peminjam (nama_peminjam, nama_barang_dipinjam, jumlah_barang_dipinjam, nomor_telepon, identitas, tanggal_pinjam, tanggal_kembali) VALUES (%s, %s, %s, '-', '-', NOW(), DATE_ADD(NOW(), INTERVAL 7 DAY))",
                (peminjam, kode, jumlah)
            )
            
            db.connection.commit()
        else:
            flash('Stok tidak mencukupi!', 'error')

        db.close()
        
    @staticmethod
    def get_barang_dipinjam():
        db = Database()
        db.cursor.execute("SELECT * FROM pinjam WHERE status = 'Dipinjam'")
        barangs = db.cursor.fetchall()
        db.close()
        return barangs
    
    @staticmethod
    def get_barang_tersedia():
        db = Database()
        query = "SELECT * FROM barang WHERE status = 'Tersedia' AND jumlah > 0"
        data = db.fetch_as_dict(query)
        db.close()
        return data
    
<<<<<<< HEAD
    @staticmethod
    def pinjam_barang(kode, jumlah, peminjam):
        db = Database()
        # Kurangi jumlah barang
        db.cursor.execute("UPDATE barang SET jumlah = jumlah - %s WHERE kode = %s AND jumlah >= %s", (jumlah, kode, jumlah))
        if db.cursor.rowcount > 0:
            # Simpan data peminjaman jika barang tersedia
            db.cursor.execute(
                "INSERT INTO pinjam (kode_barang, jumlah, peminjam, status) VALUES (%s, %s, %s, 'Dipinjam')",
                (kode, jumlah, peminjam)
            )
            db.connection.commit()
        db.close()
        
    @staticmethod
    def get_barang_dipinjam():
        db = Database()
        db.cursor.execute("SELECT * FROM pinjam WHERE status = 'Dipinjam'")
        barangs = db.cursor.fetchall()
        db.close()
        return barangs
=======
    def get_total_jenis_barang():
        db = Database()
        query = "SELECT COUNT(DISTINCT nama) AS jumlah_jenis_barang FROM barang;";
        data = db.fetch_as_dict(query)
        db.close()
        return data
    
    def get_total_barang_tersedia():
        db = Database()
        query = "SELECT COUNT(DISTINCT jumlah) AS total_barang_tersedia FROM barang WHERE status = 'Tersedia';"
        data = db.fetch_as_dict(query)
        db.close()
        return data
    
    def get_barang_dipinjam():
        db= Database()
        query = "SELECT COUNT(DISTINCT nama) AS barang_dipinjam FROM barang WHERE status = 'Dipinjam'"
        data = db.fetch_as_dict(query)
        db.close
        return data
>>>>>>> 530bf3fa56678e540e336c608f0ce0eea2c87e3d


class User:
    """User model for managing user-related operations."""
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    @staticmethod
    def create_user(username, password):
        """Create a new user."""
        db = Database()
        password_hash = generate_password_hash(password)
        db.cursor.execute(
            "INSERT INTO pengguna (username, password_hash) VALUES (%s, %s)",
            (username, password_hash)
        )
        db.connection.commit()
        db.close()

    @staticmethod
    def get_user_by_username(username):
        """Retrieve a user by their username."""
        db = Database()
        db.cursor.execute("SELECT * FROM pengguna WHERE username = %s", (username,))
        user = db.cursor.fetchone()
        db.close()
        return user

    @staticmethod
    def verify_password(username, password):
        """Verify a user's password."""
        db = Database()
        db.cursor.execute("SELECT password_hash FROM pengguna WHERE username = %s", (username,))
        result = db.cursor.fetchone()
        db.close()
        return check_password_hash(result[0], password) if result else False

    @staticmethod
    def update_password(username, new_password):
        """Update a user's password."""
        db = Database()
        password_hash = generate_password_hash(new_password)
        db.cursor.execute(
            "UPDATE pengguna SET password_hash = %s WHERE username = %s",
            (password_hash, username)
        )
        db.connection.commit()
        db.close()

class Peminjam:
    def __init__(self, nm_peminjam, nm_brg, jml_brg, nmr_telp, identitas, tgl_pinjam, tgl_kembali):
        self.nm_peminjam = nm_peminjam
        self.nm_brg = nm_brg
        self.jml_brg = jml_brg
        self.nmr_telp = nmr_telp
        self.identitas = identitas
        self.tgl_pinjam = tgl_pinjam
        self.tgl_kembali = tgl_kembali
    
    @staticmethod
    def get_all_peminjam():
        db = Database()
        list_peminjam = db.fetch_as_dict("SELECT * FROM peminjam")
        db.close()
        return list_peminjam
    
    @staticmethod
    def get_peminjam(id_peminjam):
        db = Database()
        db.cursor.execute("SELECT * FROM peminjam WHERE id_peminjam = %s", (id_peminjam,))
        row = db.cursor.fetchone()
        db.close()

        if row:
            return {
                'id_peminjam': row[0],
                'nama_peminjam': row[1],
                'nama_barang_dipinjam': row[2],
                'jumlah_barang_dipinjam': row[3],
                'nomor_telepon': row[4],
                'identitas': row[5],
                'tanggal_pinjam': row[6],
                'tanggal_kembali': row[7]
            }
        return None

    @staticmethod
    def create_peminjam(peminjam):
        db = Database()
        db.cursor.execute("INSERT INTO peminjam (nama_peminjam, nama_barang_dipinjam, jumlah_barang_dipinjam, nomor_telepon, identitas, tanggal_pinjam, tanggal_kembali) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                          (peminjam.nm_peminjam, peminjam.nm_brg, peminjam.jml_brg, peminjam.nmr_telp, peminjam.identitas, peminjam.tgl_pinjam, peminjam.tgl_kembali))
        db.connection.commit()
        db.close()

    @staticmethod
    def update_peminjam(id_peminjam, peminjam):
        db = Database()
        db.cursor.execute("UPDATE peminjam SET nama_peminjam = %s, nama_barang_dipinjam = %s, jumlah_barang_dipinjam = %s, nomor_telepon = %s, identitas = %s, tanggal_pinjam = %s, tanggal_kembali = %s WHERE id_peminjam = %s",
                          (peminjam.nm_peminjam, peminjam.nm_brg, peminjam.jml_brg, peminjam.nmr_telp, peminjam.identitas, peminjam.tgl_pinjam, peminjam.tgl_kembali, id_peminjam))
        db.connection.commit()
        db.close()

    @staticmethod
    def selesai_pinjam(id_peminjam):
        db = Database()
        db.cursor.execute("DELETE FROM peminjam WHERE id_peminjam = %s", (id_peminjam,))
        db.connection.commit()
        db.close()
        
        