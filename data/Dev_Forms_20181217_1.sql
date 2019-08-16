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
-- Table structure for table `Dev_Forms`
--

DROP TABLE IF EXISTS `Dev_Forms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Dev_Forms` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Table` varchar(45) NOT NULL,
  `Field` varchar(45) NOT NULL,
  `Type` varchar(45) DEFAULT NULL,
  `Null` varchar(45) DEFAULT NULL,
  `Key` varchar(45) DEFAULT NULL,
  `Default` varchar(45) DEFAULT NULL,
  `Extra` varchar(45) DEFAULT NULL,
  `Foreign_Key` varchar(45) DEFAULT NULL,
  `Referenced_Table` varchar(45) DEFAULT NULL,
  `Foreign_Field` varchar(45) DEFAULT NULL,
  `Foreign_Value` varchar(45) DEFAULT NULL,
  `Length` int(11) DEFAULT NULL,
  `Validation` tinyint(4) DEFAULT NULL,
  `Validation_Type` varchar(45) DEFAULT NULL,
  `Validation_String` varchar(128) DEFAULT NULL,
  `Caption_String` varchar(45) DEFAULT NULL,
  `Field_Order` int(11) DEFAULT NULL,
  `Field_Format` varchar(45) DEFAULT NULL,
  `Form_Editable` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dev_Forms`
--

LOCK TABLES `Dev_Forms` WRITE;
/*!40000 ALTER TABLE `Dev_Forms` DISABLE KEYS */;
INSERT INTO `Dev_Forms` VALUES (1,'Charge_Items','CIT_Date','date','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,10,1,'PK','Required()','Date',2,NULL,1),(2,'Charge_Items','CIT_Is_Active','tinyint(4)','YES','','0','',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Is Active',6,NULL,1),(3,'Charge_Items','CIT_Quantity','decimal(20,6)','NO','','0.000000','',NULL,NULL,NULL,NULL,20,1,'NULL','Required()','Quantity',4,NULL,1),(4,'Charge_Items','CIT_Status','int(11)','NO','MUL','0','','CIT_Status','CIT_Statuses','CIT_Status','Value',45,1,'FK','Required()','Status',5,NULL,1),(5,'Charge_Items','CIT_Time','time','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,8,1,'PK','Required()','Time',3,NULL,1),(6,'Charge_Items','CU_Id','int(11)','NO','PRI','0','','CU_Id','Charge_Units','CU_Id','CU_Description',11,1,'PK','Required()','Charge Unit Id',1,NULL,1),(7,'Charge_Units','CC_Id','int(11)','NO','MUL',NULL,'','CC_Id','Cost_Centers','CC_Id','CC_Description',11,1,'FK','Required()','Cost Center Id',10,NULL,1),(8,'Charge_Units','CI_Id','int(11)','NO','MUL',NULL,'','CI_Id','Configuration_Items','CI_Id','CI_Name',11,1,'FK','Required()','Configuration Item Id',2,NULL,1),(9,'Charge_Units','CIT_Generation','int(11)','NO','MUL',NULL,'','CIT_Generation','CIT_Generations','CIT_Generation','Value',45,1,'FK','Required()','Item Generation Type',11,NULL,1),(10,'Charge_Units','CU_Description','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Description',3,NULL,1),(11,'Charge_Units','CU_Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Id',1,NULL,1),(12,'Charge_Units','CU_Is_Always_Billeable','tinyint(4)','YES','','0','',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Is Always Billeable',6,NULL,1),(13,'Charge_Units','CU_Is_Billeable','tinyint(4)','YES','','0','',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Is Billeable',5,NULL,1),(14,'Charge_Units','CU_Operation','varchar(10)','NO','MUL',NULL,'','CU_Operation','CU_Operations','CU_Operation','Value',45,1,'FK','Required()','Conversion Operation',8,NULL,1),(15,'Charge_Units','CU_Quantity','decimal(20,6)','YES','',NULL,'',NULL,NULL,NULL,NULL,20,1,'NULL','Required()','Quantity',7,'{:,.2f}',1),(16,'Charge_Units','CU_Reference_1','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Reference 1',13,NULL,1),(17,'Charge_Units','CU_Reference_2','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Reference 2',14,NULL,1),(18,'Charge_Units','CU_Reference_3','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Reference 3',15,NULL,1),(19,'Charge_Units','CU_UUID','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','UUID',4,NULL,1),(20,'Charge_Units','Rat_Id','int(11)','YES','',NULL,'',NULL,NULL,NULL,NULL,11,NULL,'NULL','NULL','Rate Id',12,NULL,0),(21,'Charge_Units','Typ_Code','varchar(10)','NO','MUL',NULL,'','Typ_Code','CU_Types','Typ_Code','Typ_Description',10,1,'FK','Required()','Type',9,NULL,1),(22,'CIT_Generations','CIT_Generation','int(11)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,11,1,'PK','Required()','CIT_Generation',1,NULL,1),(23,'CIT_Generations','Value','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Value',2,NULL,1),(24,'CIT_Statuses','CIT_Status','int(11)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,11,1,'PK','Required()','CIT Status',1,NULL,1),(25,'CIT_Statuses','Value','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Vallue',2,NULL,1),(26,'Configuration_Items','CC_Id','int(11)','NO','MUL',NULL,'','CC_Id','Cost_Centers','CC_Id','CC_Description',11,1,'FK','Required()','Cost Center Id',5,NULL,1),(27,'Configuration_Items','CI_Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Id',1,NULL,1),(28,'Configuration_Items','CI_Name','varchar(45)','NO','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Name',2,NULL,1),(29,'Configuration_Items','CI_UUID','varchar(45)','NO','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','UUID',3,NULL,1),(30,'Configuration_Items','CIT_Generation','int(11)','NO','MUL','0','','CIT_Generation','CIT_Generations','CIT_Generation','Value',45,1,'FK','Required()','Default Item Generation Type',6,NULL,1),(31,'Configuration_Items','Cus_Id','int(11)','NO','MUL','1','','Cus_Id','Customers','Cus_Id','Cus_Name',11,1,'FK','Required()','Customer Id',7,NULL,1),(32,'Configuration_Items','Pla_Id','int(11)','NO','MUL',NULL,'','Pla_Id','Platforms','Pla_Id','Pla_Name',11,1,'FK','Required()','Platform Id',4,NULL,1),(33,'Cost_Centers','CC_Code','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Code',2,NULL,1),(34,'Cost_Centers','CC_Description','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Description',3,NULL,1),(35,'Cost_Centers','CC_Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Cost Center Id',1,NULL,1),(36,'Cost_Centers','Cur_Code','varchar(3)','NO','MUL',NULL,'','Cur_Code','Currencies','Cur_Code','Cur_Name',3,1,'FK','Required()','Currency Code',4,NULL,1),(37,'Countries','Cou_A3','varchar(3)','YES','',NULL,'',NULL,NULL,NULL,NULL,3,NULL,'NULL','NULL','Alphanum Code',3,NULL,1),(38,'Countries','Cou_Code','varchar(2)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,2,1,'PK','Required()','Code',1,NULL,1),(39,'Countries','Cou_N','int(11)','YES','',NULL,'',NULL,NULL,NULL,NULL,11,NULL,'NULL','NULL','ISO Numeric Code',4,NULL,1),(40,'Countries','Cou_Name','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Name',2,NULL,1),(41,'Countries_Currencies','Cou_Code','varchar(2)','NO','PRI',NULL,'','Cou_Code','Countries','Cou_Code','Cou_Name',2,1,'PK','Required()','Country Code',1,NULL,1),(42,'Countries_Currencies','Cou_Cur_Comment','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Comment',3,NULL,1),(43,'Countries_Currencies','Cur_Code','varchar(3)','NO','PRI',NULL,'','Cur_Code','Currencies','Cur_Code','Cur_Name',3,1,'PK','Required()','Currency Code',2,NULL,1),(44,'CU_Operations','CU_Operation','varchar(10)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,10,1,'PK','Required()','Operation',1,NULL,1),(45,'CU_Operations','Factor','int(11)','YES','',NULL,'',NULL,NULL,NULL,NULL,11,NULL,'NULL','NULL','Factor',4,NULL,1),(46,'CU_Operations','Is_Multiply','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Is Multiply',3,NULL,1),(47,'CU_Operations','Value','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Value',2,NULL,1),(48,'CU_Types','Typ_Code','varchar(10)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,10,1,'PK','Required()','Type',1,NULL,1),(49,'CU_Types','Typ_Description','varchar(45)','NO','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Description',2,NULL,1),(50,'Currencies','Cur_Code','varchar(3)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,3,1,'PK','Required()','Code',1,NULL,1),(51,'Currencies','Cur_Comment','varchar(128)','YES','',NULL,'',NULL,NULL,NULL,NULL,128,NULL,'NULL','NULL','Comment',4,NULL,1),(52,'Currencies','Cur_Id','int(11)','YES','',NULL,'',NULL,NULL,NULL,NULL,11,NULL,'NULL','NULL','Id',3,NULL,1),(53,'Currencies','Cur_Name','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Name',2,NULL,1),(54,'Customers','CC_Id','int(11)','NO','MUL',NULL,'','CC_Id','Cost_Centers','CC_Id','CC_Description',11,1,'FK','Required()','Cost Center Id',3,NULL,1),(55,'Customers','Cus_Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Id',1,NULL,1),(56,'Customers','Cus_Name','varchar(45)','NO','UNI',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Name',2,NULL,1),(57,'Dev_Forms','Caption_String','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Caption String',17,NULL,1),(58,'Dev_Forms','Default','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Default',7,NULL,1),(59,'Dev_Forms','Extra','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Extra',8,NULL,1),(60,'Dev_Forms','Field','varchar(45)','NO','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Field',3,NULL,1),(61,'Dev_Forms','Foreign_Field','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Foreign Field',11,NULL,1),(62,'Dev_Forms','Foreign_Key','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Foreign Key',9,NULL,1),(63,'Dev_Forms','Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Id',1,NULL,1),(64,'Dev_Forms','Key','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Key',6,NULL,1),(65,'Dev_Forms','Length','int(11)','YES','',NULL,'',NULL,NULL,NULL,NULL,11,NULL,'NULL','NULL','Length',13,NULL,1),(66,'Dev_Forms','Null','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Null',5,NULL,1),(67,'Dev_Forms','Referenced_Table','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Referenced Table',10,NULL,1),(68,'Dev_Forms','Table','varchar(45)','NO','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Table',2,NULL,1),(69,'Dev_Forms','Type','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Type',4,NULL,1),(70,'Dev_Forms','Validation','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Validation',14,NULL,1),(71,'Dev_Forms','Validation_String','varchar(128)','YES','',NULL,'',NULL,NULL,NULL,NULL,128,NULL,'NULL','NULL','Validation String',16,NULL,1),(72,'Dev_Forms','Validation_Type','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Validation Type',15,NULL,1),(73,'Dev_Tables','Caption','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Caption',3,NULL,1),(74,'Dev_Tables','Child_Table','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Child Table',6,NULL,1),(75,'Dev_Tables','Class_Name','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Class Name',5,NULL,1),(76,'Dev_Tables','Entity','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Entity',4,NULL,1),(77,'Dev_Tables','Generate_Children','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Generate Children',13,NULL,1),(78,'Dev_Tables','Generate_form_All','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Generate form All',11,NULL,1),(79,'Dev_Tables','Generate_Form_Filter','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Generate Form Filter',12,NULL,1),(80,'Dev_Tables','Generate_Form_One','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Generate Form One',10,NULL,1),(81,'Dev_Tables','Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Id',1,NULL,1),(82,'Dev_Tables','Name','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Name',2,NULL,1),(83,'Dev_Tables','Parent_Table','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Parent Table',7,NULL,1),(84,'Dev_Tables','Permission_Administer','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Permission Administer',22,NULL,1),(85,'Dev_Tables','Permission_Delete','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Permission Delete',16,NULL,1),(86,'Dev_Tables','Permission_Export','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Permission Export',19,NULL,1),(87,'Dev_Tables','Permission_Modify','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Permission Modify',17,NULL,1),(88,'Dev_Tables','Permission_Modify_Private','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Permission Modify Private',21,NULL,1),(89,'Dev_Tables','Permission_Report','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Permission Report',18,NULL,1),(90,'Dev_Tables','Permission_View','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Permission View',15,NULL,1),(91,'Dev_Tables','Permission_View_Private','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Permission View Private',20,NULL,1),(92,'Dev_Tables','Use_Children_Pagination','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Use Children Pagination',9,NULL,1),(93,'Dev_Tables','Use_Pagination','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Use Pagination',8,NULL,1),(94,'Exchange_Rates','Cur_Code','varchar(3)','NO','MUL',NULL,'','Cur_Code','Currencies','Cur_Code','Cur_Name',3,1,'FK','Required()','Currency Code',2,NULL,1),(95,'Exchange_Rates','ER_Date','date','NO','',NULL,'',NULL,NULL,NULL,NULL,10,NULL,'NULL','NULL','Date',4,NULL,1),(96,'Exchange_Rates','ER_Factor','decimal(20,6)','NO','',NULL,'',NULL,NULL,NULL,NULL,20,1,'NULL','Required()','Factor',3,NULL,1),(97,'Exchange_Rates','ER_Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Id',1,NULL,1),(98,'Measure_Units','MU_Code','varchar(3)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,3,1,'PK','Required()','Code',1,NULL,1),(99,'Measure_Units','MU_Description','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Description',2,NULL,1),(100,'Platforms','Pla_Host','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Host',3,NULL,1),(101,'Platforms','Pla_Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Id',1,NULL,1),(102,'Platforms','Pla_Name','varchar(45)','NO','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Name',2,NULL,1),(103,'Platforms','Pla_Password','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Password',6,NULL,1),(104,'Platforms','Pla_Port','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Port',4,NULL,1),(105,'Platforms','Pla_User','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','User',5,NULL,1),(106,'Rat_Periods','Rat_Period','int(11)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Rate Period',1,NULL,1),(107,'Rat_Periods','Value','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,45,NULL,'NULL','NULL','Value',2,NULL,1),(108,'Rates','CC_Id','int(11)','NO','MUL',NULL,'','CC_Id','Cost_Centers','CC_Id','CC_Description',11,1,'FK','Required()','Cost Center Id',5,NULL,1),(109,'Rates','CU_Id','int(11)','NO','MUL',NULL,'','CU_Id','Charge_Units','CU_Id','CU_Description',11,1,'FK','Required()','Charge Unit Id',6,NULL,1),(110,'Rates','Cur_Code','varchar(3)','NO','MUL',NULL,'','Cur_Code','Currencies','Cur_Code','Cur_Name',3,1,'FK','Required()','Currency Code',8,NULL,1),(111,'Rates','Cus_Id','int(11)','NO','MUL',NULL,'','Cus_Id','Customers','Cus_Id','Cus_Name',11,1,'FK','Required()','Customer Id',3,NULL,1),(112,'Rates','MU_Code','varchar(3)','NO','MUL',NULL,'','MU_Code','Measure_Units','MU_Code','MU_Description',3,1,'FK','Required()','Measure Unit',9,NULL,1),(113,'Rates','Pla_Id','int(11)','NO','MUL',NULL,'','Pla_Id','Platforms','Pla_Id','Pla_Name',11,1,'FK','Required()','Platform Id',4,NULL,1),(114,'Rates','Rat_Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','Id',1,NULL,1),(115,'Rates','Rat_Period','int(11)','NO','MUL',NULL,'','Rat_Period','Rat_Periods','Rat_Period','Value',11,1,'RF','Required()','Period',10,NULL,1),(116,'Rates','Rat_Price','decimal(20,6)','YES','',NULL,'',NULL,NULL,NULL,NULL,20,1,'','Required()','Rate Price',7,NULL,1),(117,'Rates','Typ_Code','varchar(10)','NO','MUL',NULL,'','Typ_Code','CU_Types','Typ_Code','Typ_Description',10,1,'FK','Required()','Charge Unit Type',2,NULL,1),(118,'Trace','ID','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,11,1,'PK','Required()','ID',1,NULL,1),(119,'Trace','LINE','varchar(128)','YES','',NULL,'',NULL,NULL,NULL,NULL,128,NULL,'NULL','NULL','LINE',2,NULL,1),(120,'Dev_Forms','Field_Order','int(11)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Field Order',18,NULL,1),(121,'Dev_Forms','Field_Format','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Field Format',19,NULL,1),(122,'Dev_Forms','Form_Editable','tinyint(4)','YES','','1','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Form Editable',20,NULL,1),(123,'Rates','Rat_Type','int(11)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Rate Type',11,NULL,0),(124,'Dev_Forms','Foreign_Value','varchar(45)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Foreign_Value',12,NULL,1),(125,'Dev_Tables','Generate_Foreign_Fields','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,4,NULL,'NULL','NULL','Generate Foreign Fields',14,NULL,1),(126,'Charge_Items','CIT_DateTime','datetime','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'CIT_DateTime',7,NULL,0),(127,'Configuration_Items','CI_Commissioning_DateTime','datetime','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'CI_Commissioning_DateTime',8,NULL,1),(128,'Configuration_Items','CI_Decommissioning_DateTime','datetime','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'CI_Decommissioning_DateTime',9,NULL,1),(129,'Cost_Centers','CC_Parent_Id','int(11)','NO','','1','',NULL,NULL,NULL,NULL,11,1,'NULL','Required()','CC_Parent_Id',5,NULL,1),(130,'Users','Id','int(11)','NO','PRI',NULL,'auto_increment',NULL,NULL,NULL,NULL,NULL,1,'PK','Required()','Id',1,NULL,1),(131,'Users','username','varchar(64)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'username',2,NULL,1),(132,'Users','role_id','int(11)','NO','MUL',NULL,'','id','Roles','id','name',11,1,'FK','Required()','role_id',3,NULL,1),(133,'Users','email','varchar(64)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'email',4,NULL,1),(134,'Users','password_hash','varchar(128)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'password_hash',5,NULL,1),(135,'Users','confirmed','tinyint(4)','YES','','0','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'confirmed',6,NULL,1),(136,'Users','CC_Id','int(11)','NO','MUL','1','','CC_Id','Cost_Centers','CC_Id','CC_Description',11,1,'FK','Required()','CC_Id',7,NULL,1),(137,'Roles','id','int(11)','NO','PRI',NULL,'',NULL,NULL,NULL,NULL,NULL,1,'PK','Required()','id',1,NULL,1),(138,'Roles','name','varchar(64)','YES','UNI',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'name',2,NULL,1),(139,'Roles','default','tinyint(4)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'default',3,NULL,1),(140,'Roles','permissions','int(11)','YES','',NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'permissions',4,NULL,1);
/*!40000 ALTER TABLE `Dev_Forms` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-17 16:35:26
