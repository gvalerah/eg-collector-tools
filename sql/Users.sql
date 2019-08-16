-- MySQL dump 10.13  Distrib 8.0.13, for Linux (x86_64)
--
-- Host: localhost    Database: collector
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  `email` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `confirmed` tinyint(4) DEFAULT '0',
  `CC_Id` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `fk_Users_Roles1_idx1` (`role_id`),
  KEY `fk_Users_Cost_Centers1_idx1` (`CC_Id`),
  CONSTRAINT `fk_Users_Cost_Centers1` FOREIGN KEY (`CC_Id`) REFERENCES `Cost_Centers` (`cc_id`),
  CONSTRAINT `fk_Users_Roles1` FOREIGN KEY (`role_id`) REFERENCES `Roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'gvalera',4,'gvalera@emtecgroup.net','pbkdf2:sha1:1000$00zgMbi7$fbfce9d2dae139caa8f3292f38034af9d920573a',1,10000000),(2,'admin',4,'admin_collector@email.com','pbkdf2:sha1:1000$vahNJ55E$c83864399cdee6b09e49b5466dafd3faa0be8d42',1,10100000),(3,'reporter',2,'reporter_collector@email.com','pbkdf2:sha1:1000$V2Z9cCpK$606122c48e02546fe958dcd6d10cb7fb958243da',1,10101010),(4,'charger',3,'charger_collector@email.com','pbkdf2:sha1:1000$84fgaNC7$34b48fe45a56e64568a7319278fe99711aad2ecd',1,10101000),(5,'customer',1,'customer@email.com','pbkdf2:sha1:1000$SmupDW8t$60698bb6775cf9c870ced2547a1f0caf261f9b2f',1,1),(6,'auditor',5,'auditor@email.com','pbkdf2:sha1:1000$CXI2LsFR$2c0440ec7bb25f9d3285c80398c2a5bf171a7bdc',1,1),(7,'linux',1,'linux@email.com','pbkdf2:sha1:1000$L2oMWyIa$de9daf8e7a5266aec15d046739f3fbe06308b329',1,1),(8,'windows',1,'windows@email.com','pbkdf2:sha1:1000$HxIvGI6f$f2f99d6e691e47337cc6c2f37047c8bce6d01c00',1,1);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-26 18:48:40
