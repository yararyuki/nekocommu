-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2024-02-20 10:00:32
-- サーバのバージョン： 10.4.28-MariaDB
-- PHP のバージョン: 8.2.4

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `post`
--

INSERT INTO `post` (`id`, `image`, `comment`, `detail`) VALUES
('nekoko', 'cat2.jpg', 'testです', 'いぇーい');

-- --------------------------------------------------------

--
-- テーブルの構造 `user`
--

CREATE TABLE `user` (
  `id` varchar(12) NOT NULL,
  `name` varchar(12) NOT NULL DEFAULT 'unknown',
  `mail` varchar(36) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `profile_image` varchar(30) NOT NULL DEFAULT 'unknownUser.jpg',
  `profile_detail` varchar(60) NOT NULL DEFAULT '新規ユーザーです',
  `tag_name` varchar(120) NOT NULL,
  `point` int(9) NOT NULL DEFAULT 0,
  `pointAll` int(9) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `user`
--

INSERT INTO `user` (`id`, `name`, `mail`, `pass`, `profile_image`, `profile_detail`, `tag_name`, `point`, `pointAll`) VALUES
('nekoko', 'ねこ', 'neko@gmail.com', '111', 'unknownUser.jpg', '新規ユーザーです', 'ちょこ', 200000, 3592500),
('rokoko', 'ろこ', 'roko@gmail.com', '111', 'unknownUser.jpg', '新規ユーザーです', 'ま,かんま,ベンジャミン三世', 35255, 114514);

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mail` (`mail`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
