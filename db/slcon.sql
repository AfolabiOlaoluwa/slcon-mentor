-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 09, 2015 at 05:33 AM
-- Server version: 5.5.41-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `slcon`
--

-- --------------------------------------------------------

--
-- Table structure for table `interest`
--

CREATE TABLE IF NOT EXISTS `interest` (
  `iid` int(11) NOT NULL AUTO_INCREMENT,
  `interest` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`iid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `link`
--

CREATE TABLE IF NOT EXISTS `link` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `ltid` int(11) DEFAULT NULL,
  `mid` int(11) DEFAULT NULL,
  PRIMARY KEY (`lid`),
  KEY `ltid` (`ltid`),
  KEY `mid` (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `link_type`
--

CREATE TABLE IF NOT EXISTS `link_type` (
  `ltid` int(11) NOT NULL AUTO_INCREMENT,
  `link_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ltid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE IF NOT EXISTS `member` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `nationality` varchar(30) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `member_interest`
--

CREATE TABLE IF NOT EXISTS `member_interest` (
  `miid` int(11) NOT NULL AUTO_INCREMENT,
  `iid` int(11) DEFAULT NULL,
  `mid` int(11) DEFAULT NULL,
  PRIMARY KEY (`miid`),
  KEY `iid` (`iid`),
  KEY `mid` (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `member_skill`
--

CREATE TABLE IF NOT EXISTS `member_skill` (
  `msid` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) DEFAULT NULL,
  `sid` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`msid`),
  KEY `mid` (`mid`),
  KEY `sid` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `mentor`
--

CREATE TABLE IF NOT EXISTS `mentor` (
  `mtid` int(11) NOT NULL AUTO_INCREMENT,
  `mid1` int(11) DEFAULT NULL,
  `mid2` int(11) DEFAULT NULL,
  PRIMARY KEY (`mtid`),
  KEY `mid1` (`mid1`),
  KEY `mid2` (`mid2`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE IF NOT EXISTS `project` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) DEFAULT NULL,
  `pcid` int(11) DEFAULT NULL,
  `project_name` varchar(50) DEFAULT NULL,
  `descr` text,
  PRIMARY KEY (`pid`),
  KEY `mid` (`mid`),
  KEY `pcid` (`pcid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `project_cat`
--

CREATE TABLE IF NOT EXISTS `project_cat` (
  `pcid` int(11) NOT NULL AUTO_INCREMENT,
  `project_cat` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`pcid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `project_skill`
--

CREATE TABLE IF NOT EXISTS `project_skill` (
  `psid` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `sid` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`psid`),
  KEY `pid` (`pid`),
  KEY `sid` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `skill`
--

CREATE TABLE IF NOT EXISTS `skill` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `skill` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `link`
--
ALTER TABLE `link`
  ADD CONSTRAINT `link_ibfk_1` FOREIGN KEY (`ltid`) REFERENCES `link_type` (`ltid`),
  ADD CONSTRAINT `link_ibfk_2` FOREIGN KEY (`mid`) REFERENCES `member` (`mid`);

--
-- Constraints for table `member_interest`
--
ALTER TABLE `member_interest`
  ADD CONSTRAINT `member_interest_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `interest` (`iid`),
  ADD CONSTRAINT `member_interest_ibfk_2` FOREIGN KEY (`mid`) REFERENCES `member` (`mid`);

--
-- Constraints for table `member_skill`
--
ALTER TABLE `member_skill`
  ADD CONSTRAINT `member_skill_ibfk_1` FOREIGN KEY (`mid`) REFERENCES `member` (`mid`),
  ADD CONSTRAINT `member_skill_ibfk_2` FOREIGN KEY (`sid`) REFERENCES `skill` (`sid`);

--
-- Constraints for table `mentor`
--
ALTER TABLE `mentor`
  ADD CONSTRAINT `mentor_ibfk_1` FOREIGN KEY (`mid1`) REFERENCES `member` (`mid`),
  ADD CONSTRAINT `mentor_ibfk_2` FOREIGN KEY (`mid2`) REFERENCES `member` (`mid`);

--
-- Constraints for table `project`
--
ALTER TABLE `project`
  ADD CONSTRAINT `project_ibfk_1` FOREIGN KEY (`mid`) REFERENCES `member` (`mid`),
  ADD CONSTRAINT `project_ibfk_2` FOREIGN KEY (`pcid`) REFERENCES `project_cat` (`pcid`);

--
-- Constraints for table `project_skill`
--
ALTER TABLE `project_skill`
  ADD CONSTRAINT `project_skill_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `project` (`pid`),
  ADD CONSTRAINT `project_skill_ibfk_2` FOREIGN KEY (`sid`) REFERENCES `skill` (`sid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
