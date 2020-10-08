-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2020 at 08:58 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `criminal_detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `contact_id` int(11) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`contact_id`, `first_name`, `last_name`, `email`, `subject`) VALUES
(1, 'Baggelis', 'Michos', 'emichos@ceid.upatras.gr', 'ds'),
(2, 'Baggelis', 'Michos', 'emichos@ceid.upatras.gr', 'j');

-- --------------------------------------------------------

--
-- Table structure for table `criminals`
--

CREATE TABLE `criminals` (
  `criminal_id` int(11) NOT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `eye_color` varchar(255) DEFAULT NULL,
  `biography` varchar(255) DEFAULT NULL,
  `portrait` varchar(255) DEFAULT NULL,
  `last_location` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `criminals`
--

INSERT INTO `criminals` (`criminal_id`, `full_name`, `age`, `height`, `weight`, `eye_color`, `biography`, `portrait`, `last_location`) VALUES
(1, 'Jonathan Walters', 55, 1.78, 65, 'Black', 'We have literally no idea who this dude is', 'https://patch.com/img/cdn/users/546525/2013/01/raw/2f182fdc7ad6dbd044e7c2fb8cafca18.jpg', 'RU6 Lab'),
(2, 'Stamatis Goumas', 24, 1.81, 96, 'Brown', 'This one is the shame of HCI Lab', 'https://i.ibb.co/3MjR6Wc/qLM5mEG.png', 'RU6 Lab'),
(3, 'Baggelis Michos', 24, 1.76, 100, 'Brown', 'This dude is 5G \"massonos\" and works somewhere where no human being should ever work.', 'https://i.ibb.co/0cWDRb7/gYyN6Sd.png', 'RU6 Lab');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `full_name`, `role`, `avatar`) VALUES
(1, 'nikos25', 'nikos25', 'None', 'Nikos Athanasiou', 'ADMIN', 'https://i.ibb.co/jv0cjvP/4EaxKrr.jpg'),
(2, 'makisKar', 'makismakis', 'None', 'Makis Karapialis', 'ADMIN', 'https://i.ibb.co/hBqnhFq/8ZOn5uw.jpg'),
(3, 'giannisPapathanasiou', 'giannisPapathanasiou', 'None', 'Giannis Papathanasiou', 'USER', 'https://i.ibb.co/TbT8Q3r/meLd3mN.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`contact_id`);

--
-- Indexes for table `criminals`
--
ALTER TABLE `criminals`
  ADD PRIMARY KEY (`criminal_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `criminals`
--
ALTER TABLE `criminals`
  MODIFY `criminal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
