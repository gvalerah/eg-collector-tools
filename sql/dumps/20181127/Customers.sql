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
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Customers` (
  `Cus_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Cus_Name` varchar(45) NOT NULL,
  `CC_Id` int(11) NOT NULL COMMENT 'Default CC in case CI does not have a defined CI-CC',
  PRIMARY KEY (`Cus_Id`),
  UNIQUE KEY `Cus_Name_UNIQUE` (`Cus_Name`),
  KEY `fk_Customers_Cost_Centers1_idx` (`CC_Id`),
  CONSTRAINT `fk_Customers_Cost_Centers1` FOREIGN KEY (`CC_Id`) REFERENCES `Cost_Centers` (`cc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (1,'DEFAULT',1),(2,'SERTECHNO',1),(3,'SERTECHNO CHILE',1),(4,'SERTECHNO COLOMBIA',1),(5,'SERTECHNO PERU',1),(6,'EMTEC GROUP',1),(7,'EMTEC CHILE',1),(8,'EMTEC PERU',1),(9,'EMTEC COLOMBIA',1),(10,'Demo: Business Unit 10 - Corp',1),(11,'Demo: Business Unit 11 - CL',1),(12,'Demo: Business Unit 12 - PE',1),(13,'Demo: Business Unit 13 - CO',1),(14,'Demo: Enjoy yourself.com',1),(15,'Demo: ADESSA - Falabella ',2);
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-27 12:10:44
