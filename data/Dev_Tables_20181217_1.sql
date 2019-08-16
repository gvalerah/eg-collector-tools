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
-- Table structure for table `Dev_Tables`
--

DROP TABLE IF EXISTS `Dev_Tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Dev_Tables` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `Caption` varchar(45) DEFAULT NULL,
  `Entity` varchar(45) DEFAULT NULL,
  `Class_Name` varchar(45) DEFAULT NULL,
  `Child_Table` varchar(45) DEFAULT NULL,
  `Parent_Table` varchar(45) DEFAULT NULL,
  `Use_Pagination` tinyint(4) DEFAULT NULL,
  `Use_Children_Pagination` tinyint(4) DEFAULT NULL,
  `Generate_Form_One` tinyint(4) DEFAULT NULL,
  `Generate_Form_All` tinyint(4) DEFAULT NULL,
  `Generate_Form_Filter` tinyint(4) DEFAULT NULL,
  `Generate_Children` tinyint(4) DEFAULT NULL,
  `Generate_Foreign_Fields` tinyint(4) DEFAULT NULL,
  `Permission_View` tinyint(4) DEFAULT NULL,
  `Permission_Delete` tinyint(4) DEFAULT NULL,
  `Permission_Modify` tinyint(4) DEFAULT NULL,
  `Permission_Report` tinyint(4) DEFAULT NULL,
  `Permission_Export` tinyint(4) DEFAULT NULL,
  `Permission_View_Private` tinyint(4) DEFAULT NULL,
  `Permission_Modify_Private` tinyint(4) DEFAULT NULL,
  `Permission_Administer` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dev_Tables`
--

LOCK TABLES `Dev_Tables` WRITE;
/*!40000 ALTER TABLE `Dev_Tables` DISABLE KEYS */;
INSERT INTO `Dev_Tables` VALUES (1,'Charge_Items','Charge Items','Charge Item','charge_item','NULL','Charge_Units',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(2,'Charge_Units','Charge Units','Charge Unit','charge_unit','Charge_Items','Configuration_Items',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(3,'CIT_Generations','Configuration Items Generation Types','Configuration Item Generation Type','cit_generation','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(4,'CIT_Statuses','Configuration Items Status Types','Configuration Item Status Type','cit_status','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(5,'Configuration_Items','Configuration Items','Configuration Item','configuration_item','Charge_Units','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(6,'Cost_Centers','Cost Centers','Cost Center','cost_center','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(7,'Countries','Countries','Country','country','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(8,'Countries_Currencies','Countries vs Currencies','Country vs Currency','country_currency','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(9,'CU_Operations','Charge Units Conversion Operations','Charge Unit Conversion Operation','cu_operation','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(10,'CU_Types','Configuration Unit Types','Configuration Unit Type','cu_type','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(11,'Currencies','Currencies','Currency','currency','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(12,'Customers','Customers','Customer','customer','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(13,'Dev_Forms','Forms','Form','dev_form','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(14,'Dev_Tables','Tables','Table','dev_table','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(15,'Exchange_Rates','Exchange Rates','Exchange Rate','exchange_rate','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(16,'Measure_Units','Measure Units','Measure Unit','measure_unit','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(17,'Platforms','Platforms','Platform','platform','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(18,'Rat_Periods','Rate Periods','Rate Period','rat_period','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(19,'Rates','Rates','Rate','rate','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(20,'Trace','Trace','Trace line','trace','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(21,'Users','Users','User','User','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),(22,'Roles','Roles','Roles','Role','NULL','NULL',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1);
/*!40000 ALTER TABLE `Dev_Tables` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-17 16:35:07
