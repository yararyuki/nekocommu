-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2024-03-01 09:03:48
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
  `post_id` int(9) NOT NULL,
  `id` varchar(12) NOT NULL,
  `image` varchar(999) NOT NULL,
  `comment` varchar(200) NOT NULL,
  `detail` varchar(100) NOT NULL,
  `tag_name` varchar(120) NOT NULL,
  `post_point` int(9) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `post`
--

INSERT INTO `post` (`post_id`, `id`, `image`, `comment`, `detail`, `tag_name`, `post_point`) VALUES
(1, 'rokoko', 'cat2.jpg', 'testです', 'いぇーい', 'ベンジャミン三世 かんま', 0),
(2, 'rokoko', 'cat3.jpg', 'あんとにお', 'yes', 'ベンジャミン三世', 0),
(3, 'rokoko', 'cat4.jpg', 'ろーる', 'あたっく', 'かんま', 63000),
(5, 'nekoko', 'nekoko20240301_153646_hitokomoru_05.jpg', '', 'ｈｈｈｈｈｈ', 'ちょこ', 0),
(6, 'rokoko', 'rokoko20240301_170126_model2.png', '', 'aaa', 'ベンジャミン三世', 0);

-- --------------------------------------------------------

--
-- テーブルの構造 `user`
--

CREATE TABLE `user` (
  `id` varchar(12) NOT NULL,
  `name` varchar(12) NOT NULL DEFAULT 'unknown',
  `mail` varchar(36) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `profile_image` varchar(999) NOT NULL DEFAULT 'unknownUser.jpg',
  `profile_detail` varchar(60) NOT NULL DEFAULT '新規ユーザーです',
  `tag_name` varchar(120) NOT NULL,
  `point` int(9) NOT NULL DEFAULT 0,
  `pointAll` int(9) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `user`
--

INSERT INTO `user` (`id`, `name`, `mail`, `pass`, `profile_image`, `profile_detail`, `tag_name`, `point`, `pointAll`) VALUES
('nekoko', 'ねこ', 'neko@gmail.com', '111', '20240301_160217_hitokomoru_05.jpg', 'あああああ', 'ちょこ', 180000, 3592500),
('rokoko', 'ろこ', 'roko@gmail.com', '111', '20240301_170227_IMG_6339.jpg', '新規ユーザーです', 'ま かんま ベンジャミン三世 野村 トーマス', 61755, 164514);

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`post_id`);

--
-- テーブルのインデックス `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mail` (`mail`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `post`
--
ALTER TABLE `post`
  MODIFY `post_id` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
