-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2024-02-19 09:46:57
-- サーバのバージョン： 10.4.25-MariaDB
-- PHP のバージョン: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `nekocommu`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `post`
--

CREATE TABLE `post` (
  `id` varchar(12) NOT NULL,
  `image` varchar(30) NOT NULL,
  `comment` varchar(200) NOT NULL,
  `detail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- テーブルのデータのダンプ `post`
--

INSERT INTO `post` (`id`, `image`, `comment`, `detail`) VALUES
('nekoko', 'cat2.jpg', 'これはテストコメントです', 'これはテスト説明文です');

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
