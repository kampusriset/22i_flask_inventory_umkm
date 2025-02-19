-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for inventory_ukm
CREATE DATABASE IF NOT EXISTS `inventory_ukm` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `inventory_ukm`;

-- Dumping structure for table inventory_ukm.barang
CREATE TABLE IF NOT EXISTS `barang` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kode` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `nama` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `jumlah` int NOT NULL,
  `kondisi` enum('Bagus','Rusak','Sedang') COLLATE utf8mb4_general_ci NOT NULL,
  `gambar` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `boleh_dipinjam` tinyint(1) NOT NULL,
  `tanggal_ditambahkan` date DEFAULT (curdate()),
  `status` enum('Tersedia','Dipinjam','Dalam Perbaikan') COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'Tersedia',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kode` (`kode`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table inventory_ukm.barang: ~10 rows (approximately)
REPLACE INTO `barang` (`id`, `kode`, `nama`, `jumlah`, `kondisi`, `gambar`, `boleh_dipinjam`, `tanggal_ditambahkan`, `status`) VALUES
	(1, 'EL001', 'Laptop', 5, 'Bagus', 'laptop.jpg', 1, '2025-02-15', 'Dipinjam'),
	(2, 'EL002', 'Proyektor', 2, 'Bagus', 'proyektor.jpg', 1, '2025-02-15', 'Dipinjam'),
	(3, 'PR001', 'Meja Lipat', 10, 'Bagus', 'meja_lipat.jpg', 0, '2025-02-15', 'Dalam Perbaikan'),
	(4, 'PR002', 'Kursi Lipat', 20, 'Bagus', 'kursi_lipat.jpg', 0, '2025-02-15', 'Tersedia'),
	(5, 'EL003', 'Speaker Portable', 3, 'Bagus', 'speaker.jpg', 1, '2025-02-15', 'Tersedia'),
	(6, 'EL004', 'Mikrofon', 4, 'Bagus', 'mikrofon.jpg', 1, '2025-02-15', 'Tersedia'),
	(7, 'AC001', 'Kabel HDMI', 8, 'Bagus', 'kabel_hdmi.jpg', 1, '2025-02-15', 'Tersedia'),
	(8, 'PR003', 'Whiteboard', 2, 'Bagus', 'whiteboard.jpg', 0, '2025-02-15', 'Dipinjam'),
	(9, 'AC002', 'Spidol Board', 50, 'Bagus', 'spidol.jpg', 0, '2025-02-15', 'Tersedia'),
	(10, 'PR004', 'Tripod Kamera', 3, 'Bagus', 'tripod.jpg', 1, '2025-02-15', 'Tersedia');

-- Dumping structure for table inventory_ukm.peminjam
CREATE TABLE IF NOT EXISTS `peminjam` (
  `id_peminjam` int NOT NULL AUTO_INCREMENT,
  `nama_peminjam` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nama_barang_dipinjam` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `jumlah_barang_dipinjam` int NOT NULL,
  `nomor_telepon` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `identitas` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tanggal_pinjam` date NOT NULL,
  `tanggal_kembali` date NOT NULL,
  PRIMARY KEY (`id_peminjam`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table inventory_ukm.peminjam: ~2 rows (approximately)
REPLACE INTO `peminjam` (`id_peminjam`, `nama_peminjam`, `nama_barang_dipinjam`, `jumlah_barang_dipinjam`, `nomor_telepon`, `identitas`, `tanggal_pinjam`, `tanggal_kembali`) VALUES
	(1, 'Reno Afrido', 'Laptop', 1, '081228275280', 'KTA', '2025-02-19', '2025-02-25'),
	(2, 'Donia Kenang', 'Mikrofon', 1, '081228275280', 'KTA', '2025-02-19', '2025-02-28'),
	(4, 'Aslan', 'EL003', 2, '123123', '480467223_1348028529731979_7457330173927748541_n.jpg', '2025-02-19', '2025-02-26'),
	(5, 'Afrido', 'PR004', 1, '123456', 'download.png', '2025-02-19', '2025-02-26'),
	(6, 'Afrido', 'PR004', 1, '123456', 'download.png', '2025-02-19', '2025-02-26'),
	(7, 'Afrido', 'PR004', 1, '123456', 'download.png', '2025-02-19', '2025-02-26');

-- Dumping structure for table inventory_ukm.pengguna
CREATE TABLE IF NOT EXISTS `pengguna` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table inventory_ukm.pengguna: ~2 rows (approximately)
REPLACE INTO `pengguna` (`id`, `username`, `password_hash`, `created_at`) VALUES
	(1, 'admin', 'scrypt:32768:8:1$HBvh98D0QAKcFZY4$60fd5555559465166ba941e866af04dbbb504174c80d0badb9ca392b98ab27348835a6516a083fa72e1586b558d4bc2e23d34f7ee67bb39ec6bb63654d780e1d', '2025-02-14 17:54:06'),
	(3, 'renoafrido', 'scrypt:32768:8:1$n0ed5IWWAR4y260t$77359a5422fa25fd97ea10ff91aed233bff2e59e63ad020ea13465dfdabf73c509ad2caaea7abc51d689ecbde1e0680dfb7ab9347fb9b43198a1e9090e3dbc79', '2025-02-19 07:10:25');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
