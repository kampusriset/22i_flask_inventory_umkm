import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self):
        self.connection = MySQLdb.connect(
            host='localhost',
            user='root',
            password='',
            database='inventory_ukm'
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

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
