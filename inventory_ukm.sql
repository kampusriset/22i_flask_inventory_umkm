-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 14, 2025 at 07:54 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventory_ukm`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `id` int(11) NOT NULL,
  `kode` varchar(50) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `kondisi` enum('Bagus','Rusak','Sedang') NOT NULL,
  `gambar` varchar(255) DEFAULT NULL,
  `boleh_dipinjam` tinyint(1) NOT NULL,
  `tanggal_ditambahkan` date DEFAULT curdate(),
  `status` enum('Tersedia','Dipinjam','Dalam Perbaikan') NOT NULL DEFAULT 'Tersedia'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`id`, `kode`, `nama`, `jumlah`, `kondisi`, `gambar`, `boleh_dipinjam`, `tanggal_ditambahkan`, `status`) VALUES
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

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id`, `username`, `password_hash`, `created_at`) VALUES
(0, 'admin', 'scrypt:32768:8:1$HBvh98D0QAKcFZY4$60fd5555559465166ba941e866af04dbbb504174c80d0badb9ca392b98ab27348835a6516a083fa72e1586b558d4bc2e23d34f7ee67bb39ec6bb63654d780e1d', '2025-02-14 17:54:06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode` (`kode`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `barang`
--
ALTER TABLE `barang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
