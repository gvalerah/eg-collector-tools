-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema collector
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `collector` ;

-- -----------------------------------------------------
-- Schema collector
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `collector` ;
SHOW WARNINGS;
USE `collector` ;

-- -----------------------------------------------------
-- Table `collector`.`Platforms`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Platforms` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Platforms` (
  `Pla_Id` INT NOT NULL AUTO_INCREMENT,
  `Pla_Name` VARCHAR(45) NOT NULL,
  `Pla_Host` VARCHAR(45) NULL,
  `Pla_Port` VARCHAR(45) NULL,
  `Pla_User` VARCHAR(45) NULL,
  `Pla_Password` VARCHAR(45) NULL,
  PRIMARY KEY (`Pla_Id`))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX `Pla_id_UNIQUE` ON `collector`.`Platforms` (`Pla_Id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Currencies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Currencies` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Currencies` (
  `Cur_Code` VARCHAR(3) NOT NULL,
  `Cur_Name` VARCHAR(45) NULL,
  `Cur_Id` INT NULL,
  `Cur_Comment` VARCHAR(128) NULL,
  PRIMARY KEY (`Cur_Code`))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX `Cur_Code_UNIQUE` ON `collector`.`Currencies` (`Cur_Code` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Cost_Centers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Cost_Centers` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Cost_Centers` (
  `CC_Id` INT NOT NULL AUTO_INCREMENT COMMENT 'Unique Colletor\'\'s System Id (Auto generated)\\n',
  `CC_Code` VARCHAR(45) NULL COMMENT 'Known billing system code',
  `CC_Description` VARCHAR(45) NULL COMMENT 'Description of CC Location',
  `Cur_Code` VARCHAR(3) NOT NULL,
  `CC_Parent_Code` VARCHAR(45) NOT NULL DEFAULT 1,
  PRIMARY KEY (`CC_Id`),
  CONSTRAINT `fk_Cost_Centers_Currencies1`
    FOREIGN KEY (`Cur_Code`)
    REFERENCES `collector`.`Currencies` (`Cur_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Cost_Centers_Currencies1_idx1` ON `collector`.`Cost_Centers` (`Cur_Code` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Customers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Customers` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Customers` (
  `Cus_Id` INT NOT NULL AUTO_INCREMENT,
  `Cus_Name` VARCHAR(45) NOT NULL,
  `CC_Id` INT NOT NULL,
  PRIMARY KEY (`Cus_Id`),
  CONSTRAINT `fk_Customers_Cost_Centers1`
    FOREIGN KEY (`CC_Id`)
    REFERENCES `collector`.`Cost_Centers` (`CC_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX `Cus_Name_UNIQUE` ON `collector`.`Customers` (`Cus_Name` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Customers_Cost_Centers1_idx1` ON `collector`.`Customers` (`CC_Id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Configuration_Items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Configuration_Items` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Configuration_Items` (
  `CI_Id` INT NOT NULL AUTO_INCREMENT,
  `CI_Name` VARCHAR(45) NOT NULL,
  `CI_UUID` VARCHAR(45) NOT NULL,
  `Pla_Id` INT NOT NULL,
  `CC_Id` INT NOT NULL,
  `Cus_Id` INT NOT NULL DEFAULT 1,
  `CI_Commissioning_DateTime` DATETIME NULL,
  `CI_Decommissioning_DateTime` DATETIME NULL,
  PRIMARY KEY (`CI_Id`),
  CONSTRAINT `fk_Configuration_Items_Platforms1`
    FOREIGN KEY (`Pla_Id`)
    REFERENCES `collector`.`Platforms` (`Pla_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Configuration_Items_Customers1`
    FOREIGN KEY (`Cus_Id`)
    REFERENCES `collector`.`Customers` (`Cus_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Configuration_Items_Cost_Centers1`
    FOREIGN KEY (`CC_Id`)
    REFERENCES `collector`.`Cost_Centers` (`CC_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Configuration_Items_Platforms1_idx` ON `collector`.`Configuration_Items` (`Pla_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Configuration_Items_Customers1_idx` ON `collector`.`Configuration_Items` (`Cus_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Configuration_Items_Cost_Centers1_idx1` ON `collector`.`Configuration_Items` (`CC_Id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`CU_Types`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`CU_Types` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`CU_Types` (
  `Typ_Code` VARCHAR(10) NOT NULL,
  `Typ_Description` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Typ_Code`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`CU_Operations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`CU_Operations` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`CU_Operations` (
  `CU_Operation` VARCHAR(10) NOT NULL,
  `Value` VARCHAR(45) NULL,
  `Is_Multiply` TINYINT NULL,
  `Factor` INT NULL,
  PRIMARY KEY (`CU_Operation`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`CIT_Generations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`CIT_Generations` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`CIT_Generations` (
  `CIT_Generation` INT NOT NULL,
  `Value` VARCHAR(45) NULL,
  PRIMARY KEY (`CIT_Generation`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Charge_Units`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Charge_Units` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Charge_Units` (
  `CU_Id` INT NOT NULL AUTO_INCREMENT,
  `CI_Id` INT NOT NULL,
  `CU_Description` VARCHAR(45) NULL,
  `CU_UUID` VARCHAR(45) NULL,
  `CU_Is_Billeable` TINYINT NULL DEFAULT 0,
  `CU_Is_Always_Billeable` TINYINT NULL DEFAULT 0,
  `CU_Quantity` DECIMAL(20,6) NULL COMMENT 'Charge Unit Default Quantity, thos is used depending on GI Generation type of Charge_Items\nCI_CIT  = \n1, ignored if this will be retrieved from platform, if not possible this is used as default\n2, Manual this value is used/updated any time\n3, Periodic, This value is used to generate data periodically\n',
  `CU_Operation` VARCHAR(10) NOT NULL,
  `Typ_Code` VARCHAR(10) NOT NULL,
  `CIT_Generation` INT NOT NULL,
  `Rat_Id` INT NULL,
  `CU_Reference_1` VARCHAR(45) NULL,
  `CU_Reference_2` VARCHAR(45) NULL,
  `CU_Reference_3` VARCHAR(45) NULL,
  PRIMARY KEY (`CU_Id`),
  CONSTRAINT `fk_Charge_Units_Configuration_Items1`
    FOREIGN KEY (`CI_Id`)
    REFERENCES `collector`.`Configuration_Items` (`CI_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Charge_Units_CU_Types1`
    FOREIGN KEY (`Typ_Code`)
    REFERENCES `collector`.`CU_Types` (`Typ_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Charge_Units_CU_Operations1`
    FOREIGN KEY (`CU_Operation`)
    REFERENCES `collector`.`CU_Operations` (`CU_Operation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Charge_Units_CIT_Generations1`
    FOREIGN KEY (`CIT_Generation`)
    REFERENCES `collector`.`CIT_Generations` (`CIT_Generation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_Configuration_Items1_idx` ON `collector`.`Charge_Units` (`CI_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_CU_Types1_idx` ON `collector`.`Charge_Units` (`Typ_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_CU_Operations1_idx` ON `collector`.`Charge_Units` (`CU_Operation` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_CIT_Generations1_idx` ON `collector`.`Charge_Units` (`CIT_Generation` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Measure_Units`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Measure_Units` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Measure_Units` (
  `MU_Code` VARCHAR(3) NOT NULL,
  `MU_Description` VARCHAR(45) NULL,
  PRIMARY KEY (`MU_Code`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Rat_Periods`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Rat_Periods` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Rat_Periods` (
  `Rat_Period` INT NOT NULL,
  `Value` VARCHAR(45) NULL,
  PRIMARY KEY (`Rat_Period`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Rates`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Rates` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Rates` (
  `Rat_Id` INT NOT NULL AUTO_INCREMENT,
  `Typ_Code` VARCHAR(10) NOT NULL,
  `Cus_Id` INT NOT NULL,
  `Pla_Id` INT NOT NULL,
  `CC_Id` INT NOT NULL,
  `CI_Id` INT NOT NULL,
  `Rat_Price` DECIMAL(20,6) NULL,
  `Cur_Code` VARCHAR(3) NOT NULL,
  `MU_Code` VARCHAR(3) NOT NULL,
  `Rat_Period` INT NOT NULL,
  `Rat_Type` INT NULL,
  PRIMARY KEY (`Rat_Id`),
  CONSTRAINT `fk_Rate_Platform1`
    FOREIGN KEY (`Pla_Id`)
    REFERENCES `collector`.`Platforms` (`Pla_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rate_Customer2`
    FOREIGN KEY (`Cus_Id`)
    REFERENCES `collector`.`Customers` (`Cus_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rates_Measure_Units1`
    FOREIGN KEY (`MU_Code`)
    REFERENCES `collector`.`Measure_Units` (`MU_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rates_CU_Types1`
    FOREIGN KEY (`Typ_Code`)
    REFERENCES `collector`.`CU_Types` (`Typ_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rates_Rat_Periods1`
    FOREIGN KEY (`Rat_Period`)
    REFERENCES `collector`.`Rat_Periods` (`Rat_Period`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rates_Cost_Centers1`
    FOREIGN KEY (`CC_Id`)
    REFERENCES `collector`.`Cost_Centers` (`CC_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rates_Currencies1`
    FOREIGN KEY (`Cur_Code`)
    REFERENCES `collector`.`Currencies` (`Cur_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rates_Configuration_Items1`
    FOREIGN KEY (`CI_Id`)
    REFERENCES `collector`.`Configuration_Items` (`CI_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Rate_Platform1_idx` ON `collector`.`Rates` (`Pla_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rate_Customer2_idx` ON `collector`.`Rates` (`Cus_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_Measure_Units1_idx` ON `collector`.`Rates` (`MU_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_CU_Types1_idx` ON `collector`.`Rates` (`Typ_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_Rat_Periods1_idx` ON `collector`.`Rates` (`Rat_Period` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_Cost_Centers1_idx` ON `collector`.`Rates` (`CC_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_Currencies1_idx1` ON `collector`.`Rates` (`Cur_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_Configuration_Items1_idx` ON `collector`.`Rates` (`CI_Id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Dev_Forms`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Dev_Forms` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Dev_Forms` (
  `Id` INT(11) NOT NULL AUTO_INCREMENT,
  `Table` VARCHAR(45) NOT NULL,
  `Field` VARCHAR(45) NOT NULL,
  `Type` VARCHAR(45) NULL DEFAULT NULL,
  `Null` VARCHAR(45) NULL DEFAULT NULL,
  `Key` VARCHAR(45) NULL DEFAULT NULL,
  `Default` VARCHAR(45) NULL DEFAULT NULL,
  `Extra` VARCHAR(45) NULL DEFAULT NULL,
  `Foreign_Key` VARCHAR(45) NULL DEFAULT NULL,
  `Referenced_Table` VARCHAR(45) NULL DEFAULT NULL,
  `Foreign_Field` VARCHAR(45) NULL DEFAULT NULL,
  `Foreign_Value` VARCHAR(45) NULL,
  `Length` INT(11) NULL DEFAULT NULL,
  `Validation` TINYINT(4) NULL DEFAULT NULL,
  `Validation_Type` VARCHAR(45) NULL DEFAULT NULL,
  `Validation_String` VARCHAR(128) NULL DEFAULT NULL,
  `Caption_String` VARCHAR(45) NULL DEFAULT NULL,
  `Field_Order` INT NULL,
  `Field_Format` VARCHAR(45) NULL,
  `Form_Editable` TINYINT NULL DEFAULT 1,
  `ORM_Schema` TINYINT NULL DEFAULT 1,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB
AUTO_INCREMENT = 79
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`CIT_Statuses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`CIT_Statuses` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`CIT_Statuses` (
  `CIT_Status` INT NOT NULL,
  `Value` VARCHAR(45) NULL,
  PRIMARY KEY (`CIT_Status`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Charge_Items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Charge_Items` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Charge_Items` (
  `CU_Id` INT NOT NULL DEFAULT 0,
  `CIT_Date` DATE NULL,
  `CIT_Time` TIME NULL,
  `CIT_Quantity` DECIMAL(20,6) NOT NULL DEFAULT 0,
  `CIT_Status` INT NOT NULL DEFAULT 0,
  `CIT_Is_Active` TINYINT NULL DEFAULT 0,
  `CIT_DateTime` DATETIME NOT NULL,
  PRIMARY KEY (`CU_Id`, `CIT_DateTime`),
  CONSTRAINT `fk_Charge_Item_Charge_Unit1`
    FOREIGN KEY (`CU_Id`)
    REFERENCES `collector`.`Charge_Units` (`CU_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Charge_Items_CIT_Statuses1`
    FOREIGN KEY (`CIT_Status`)
    REFERENCES `collector`.`CIT_Statuses` (`CIT_Status`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'Table that captures Platform details. Need to be filled by Demons, also may include Claim records in order to consider them for Cycle Billing/or better chand status:\n1 Pending Approval\n2 Claim\n3 Rejected\n4 Approved';

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Item_Charge_Unit1_idx` ON `collector`.`Charge_Items` (`CU_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Items_CIT_Statuses1_idx` ON `collector`.`Charge_Items` (`CIT_Status` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Exchange_Rates`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Exchange_Rates` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Exchange_Rates` (
  `ER_Id` INT NOT NULL AUTO_INCREMENT,
  `Cur_Code` VARCHAR(3) NOT NULL,
  `ER_Factor` DECIMAL(20,10) NOT NULL,
  `ER_Date` DATE NOT NULL,
  PRIMARY KEY (`ER_Id`),
  CONSTRAINT `fk_Exchange_Rates_Currencies1`
    FOREIGN KEY (`Cur_Code`)
    REFERENCES `collector`.`Currencies` (`Cur_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX `ER_Id_UNIQUE` ON `collector`.`Exchange_Rates` (`ER_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Exchange_Rates_Currencies1_idx1` ON `collector`.`Exchange_Rates` (`Cur_Code` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Countries`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Countries` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Countries` (
  `Cou_Code` VARCHAR(2) NOT NULL COMMENT 'ISO ALPHA-2 Code\n',
  `Cou_Name` VARCHAR(45) NULL,
  `Cou_A3` VARCHAR(3) NULL,
  `Cou_N` INT NULL COMMENT 'ISO Numeric Code UN M49 Numerical Code',
  PRIMARY KEY (`Cou_Code`))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX `Cou_Code_UNIQUE` ON `collector`.`Countries` (`Cou_Code` ASC) INVISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Dev_Tables`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Dev_Tables` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Dev_Tables` (
  `Id` INT(11) NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL DEFAULT NULL,
  `Caption` VARCHAR(45) NULL DEFAULT NULL,
  `Entity` VARCHAR(45) NULL DEFAULT NULL,
  `Class_Name` VARCHAR(45) NULL DEFAULT NULL,
  `Child_Table` VARCHAR(45) NULL DEFAULT NULL,
  `Parent_Table` VARCHAR(45) NULL,
  `Use_Pagination` TINYINT NULL DEFAULT NULL,
  `Use_Children_Pagination` TINYINT NULL DEFAULT NULL,
  `Generate_Form_One` TINYINT NULL DEFAULT NULL,
  `Generate_Form_All` TINYINT NULL DEFAULT NULL,
  `Generate_Form_Filter` TINYINT NULL DEFAULT NULL,
  `Generate_Children` TINYINT NULL DEFAULT NULL,
  `Generate_Foreign_Fields` TINYINT NULL,
  `Permission_View` TINYINT NULL,
  `Permission_Delete` TINYINT NULL,
  `Permission_Modify` TINYINT NULL,
  `Permission_Report` TINYINT NULL,
  `Permission_Export` TINYINT NULL,
  `Permission_View_Private` TINYINT NULL,
  `Permission_Modify_Private` TINYINT NULL,
  `Permission_Administer` TINYINT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Trace`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Trace` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Trace` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `LINE` VARCHAR(128) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Countries_Currencies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Countries_Currencies` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Countries_Currencies` (
  `Cou_Code` VARCHAR(2) NOT NULL,
  `Cur_Code` VARCHAR(3) NOT NULL,
  `Cou_Cur_Comment` VARCHAR(45) NULL,
  PRIMARY KEY (`Cou_Code`, `Cur_Code`),
  CONSTRAINT `fk_Countries_Currencies_Countries1`
    FOREIGN KEY (`Cou_Code`)
    REFERENCES `collector`.`Countries` (`Cou_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Countries_Currencies_Currencies1`
    FOREIGN KEY (`Cur_Code`)
    REFERENCES `collector`.`Currencies` (`Cur_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Countries_Currencies_Countries1_idx` ON `collector`.`Countries_Currencies` (`Cou_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Countries_Currencies_Currencies1_idx` ON `collector`.`Countries_Currencies` (`Cur_Code` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Roles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Roles` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Roles` (
  `id` INT NOT NULL,
  `name` VARCHAR(64) NULL,
  `default` TINYINT NULL,
  `permissions` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE UNIQUE INDEX `name_UNIQUE` ON `collector`.`Roles` (`name` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Users` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(64) NULL,
  `role_id` INT NOT NULL,
  `email` VARCHAR(64) NULL,
  `password_hash` VARCHAR(128) NULL,
  `confirmed` TINYINT NULL DEFAULT 0,
  `CC_Id` INT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Users_Roles1`
    FOREIGN KEY (`role_id`)
    REFERENCES `collector`.`Roles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_Cost_Centers1`
    FOREIGN KEY (`CC_Id`)
    REFERENCES `collector`.`Cost_Centers` (`CC_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Users_Roles1_idx1` ON `collector`.`Users` (`role_id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Users_Cost_Centers1_idx1` ON `collector`.`Users` (`CC_Id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Charge_Resumes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Charge_Resumes` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Charge_Resumes` (
  `Cus_Id` INT NOT NULL,
  `CR_Date_From` DATE NOT NULL,
  `CR_Date_To` DATE NOT NULL,
  `CIT_Status` INT NOT NULL,
  `Cur_Code` VARCHAR(3) NOT NULL,
  `CIT_Count` INT NULL,
  `CIT_Quantity` DECIMAL(20,6) NULL,
  `CIT_Generation` INT NULL DEFAULT 1,
  `CU_Id` INT NOT NULL,
  `CI_CC_Id` INT NULL,
  `CU_Operation` VARCHAR(10) NULL,
  `Typ_Code` VARCHAR(10) NULL,
  `CC_Cur_Code` VARCHAR(3) NULL,
  `CI_Id` INT NULL,
  `Rat_Id` INT NULL,
  `Rat_Price` DECIMAL(20,6) NULL,
  `Rat_MU_Code` VARCHAR(3) NULL,
  `Rat_Cur_Code` VARCHAR(3) NULL,
  `Rat_Period` INT NULL,
  `Rat_Hourly` DECIMAL(20,6) NULL,
  `Rat_Daily` DECIMAL(20,6) NULL,
  `Rat_Monthly` DECIMAL(20,6) NULL,
  `CR_Quantity` DECIMAL(20,6) NULL,
  `CR_Quantity_at_Rate` DECIMAL(20,6) NULL,
  `CC_XR` DECIMAL(20,10) NULL,
  `CR_Cur_XR` DECIMAL(20,10) NULL,
  `CR_ST_at_Rate_Cur` DECIMAL(20,6) NULL,
  `CR_ST_at_CC_Cur` DECIMAL(20,6) NULL,
  `CR_ST_at_Cur` DECIMAL(20,6) NULL,
  `Cus_Name` VARCHAR(45) NULL,
  `CI_Name` VARCHAR(45) NULL,
  `CU_Description` VARCHAR(45) NULL,
  `CC_Description` VARCHAR(45) NULL,
  `Rat_Period_Description` VARCHAR(10) NULL,
  `Pla_Id` INT NULL,
  PRIMARY KEY (`Cus_Id`, `CR_Date_From`, `CR_Date_To`, `CIT_Status`, `Cur_Code`, `CU_Id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`User_Resumes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`User_Resumes` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`User_Resumes` (
  `Cus_Id` INT NULL,
  `CR_Date_From` DATE NOT NULL,
  `CR_Date_To` DATE NOT NULL,
  `CIT_Status` INT NOT NULL,
  `Cur_Code` VARCHAR(3) NOT NULL,
  `CIT_Count` INT NULL,
  `CIT_Quantity` DECIMAL(20,6) NULL,
  `CIT_Generation` INT NULL DEFAULT 1,
  `CU_Id` INT NOT NULL,
  `CI_CC_Id` INT NULL,
  `CU_Operation` VARCHAR(10) NULL,
  `Typ_Code` VARCHAR(10) NULL,
  `CC_Cur_Code` VARCHAR(3) NULL,
  `CI_Id` INT NOT NULL,
  `Rat_Id` INT NULL,
  `Rat_Price` DECIMAL(20,6) NULL,
  `Rat_MU_Code` VARCHAR(3) NULL,
  `Rat_Cur_Code` VARCHAR(3) NULL,
  `Rat_Period` INT NULL,
  `Rat_Hourly` DECIMAL(20,6) NULL,
  `Rat_Daily` DECIMAL(20,6) NULL,
  `Rat_Monthly` DECIMAL(20,6) NULL,
  `CR_Quantity` DECIMAL(20,6) NULL,
  `CR_Quantity_at_Rate` DECIMAL(20,6) NULL,
  `CC_XR` DECIMAL(20,10) NULL,
  `CR_Cur_XR` DECIMAL(20,10) NULL,
  `CR_ST_at_Rate_Cur` DECIMAL(20,6) NULL,
  `CR_ST_at_CC_Cur` DECIMAL(20,6) NULL,
  `CR_ST_at_Cur` DECIMAL(20,6) NULL,
  `Cus_Name` VARCHAR(45) NULL,
  `CI_Name` VARCHAR(45) NULL,
  `CU_Description` VARCHAR(45) NULL,
  `CC_Description` VARCHAR(45) NULL,
  `Rat_Period_Description` VARCHAR(10) NULL,
  `CC_Code` VARCHAR(45) NULL,
  PRIMARY KEY (`CR_Date_From`, `CR_Date_To`, `CIT_Status`, `Cur_Code`, `CU_Id`, `CI_Id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`ST_Use_Per_CU`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`ST_Use_Per_CU` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`ST_Use_Per_CU` (
  `CU_Id` INT NOT NULL,
  `From` DATETIME NOT NULL,
  `To` DATETIME NOT NULL,
  `Total_Slices` INT NULL DEFAULT 0,
  `Found_Slices` INT NULL DEFAULT 0,
  `Not_Found_Slices` INT NULL DEFAULT 0,
  `Period_Initial_Q` DECIMAL(20,6) NULL DEFAULT 0,
  `Period_Increase` DECIMAL(20,6) NULL DEFAULT 0,
  `Period_Increase_Count` INT NULL DEFAULT 0,
  `Period_Reduction` DECIMAL(20,6) NULL DEFAULT 0,
  `Period_Reduction_Count` INT NULL DEFAULT 0,
  `Period_Final_Q` DECIMAL(20,6) NULL DEFAULT 0,
  `CI_Id` INT NULL DEFAULT 1,
  `CC_Id` INT NULL DEFAULT 1,
  `Cus_Id` INT NULL DEFAULT 1,
  `Rat_Id` INT(11) NULL DEFAULT 1,
  `Typ_Code` VARCHAR(10) NULL DEFAULT 'NUL',
  `Pla_Id` INT NULL DEFAULT 1,
  `Mean` DECIMAL(20,6) NULL DEFAULT 0,
  `Variance` DECIMAL(20,6) NULL DEFAULT 0,
  `StdDev` DECIMAL(20,6) NULL DEFAULT 0,
  `Min` DECIMAL(20,6) NULL DEFAULT 0,
  `Max` DECIMAL(20,6) NULL DEFAULT 0,
  PRIMARY KEY (`CU_Id`, `From`, `To`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`ST_Use_Per_Type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`ST_Use_Per_Type` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`ST_Use_Per_Type` (
  `Typ_Code` VARCHAR(10) NOT NULL,
  `Cus_Id` INT NOT NULL DEFAULT 1,
  `Pla_Id` INT NOT NULL DEFAULT 1,
  `CC_Id` INT NOT NULL DEFAULT 1,
  `CI_Id` INT NOT NULL DEFAULT 1,
  `Year` INT NOT NULL,
  `Month` INT NOT NULL,
  `Count` INT NULL DEFAULT 0,
  `Mean` DECIMAL(20,6) NULL DEFAULT 0,
  `Variance` DECIMAL(20,6) NULL DEFAULT 0,
  `StdDev` DECIMAL(20,6) NULL DEFAULT 0,
  `Min` DECIMAL(20,6) NULL DEFAULT 0,
  `Max` DECIMAL(20,6) NULL DEFAULT 0,
  PRIMARY KEY (`Typ_Code`, `Year`, `Month`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CI_Id`))
ENGINE = InnoDB;

SHOW WARNINGS;
USE `collector` ;

-- -----------------------------------------------------
-- function Get_CU_Type_Description_From_Code
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_CU_Type_Description_From_Code`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_CU_Type_Description_From_Code` (CODE VARCHAR(10)) RETURNS VARCHAR(45) DETERMINISTIC
BEGIN
	DECLARE DESCRIPTION VARCHAR(45);
    SELECT Typ_Description FROM CU_Types WHERE Typ_Code=CODE LIMIT 1 INTO DESCRIPTION;
	RETURN DESCRIPTION;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Customer_Id_From_Name
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Customer_Id_From_Name`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Customer_Id_From_Name` (NAME VARCHAR(45)) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE ID INT;
    SELECT Cus_Id FROM Customers WHERE Cus_Name=NAME LIMIT 1 INTO ID;
	RETURN ID;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Customer_Name_From_Id
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Customer_Name_From_Id`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Customer_Name_From_Id` (ID INT) RETURNS VARCHAR(45) DETERMINISTIC
BEGIN
	DECLARE NAME VARCHAR(45);
    SELECT Cus_Name FROM Customers WHERE Cus_Id=Id LIMIT 1 INTO NAME;
	RETURN NAME;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Country_Code_From_Name
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Country_Code_From_Name`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Country_Code_From_Name` (NAME VARCHAR(45)) RETURNS VARCHAR(10) DETERMINISTIC
BEGIN
	DECLARE CODE VARCHAR(10);
    SELECT Cou_Code FROM Countries WHERE Cou_Name=NAME LIMIT 1 INTO CODE;
	RETURN CODE;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Country_Name_From_Code
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Country_Name_From_Code`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Country_Name_From_Code` (CODE VARCHAR(10)) RETURNS VARCHAR(45) DETERMINISTIC
BEGIN
	DECLARE NAME VARCHAR(45);
    SELECT Cou_Name FROM Countries WHERE Cou_Code=CODE LIMIT 1 INTO NAME;
	RETURN NAME;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Rate_Id
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Rate_Id`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Rate_Id` (TYPE_CODE VARCHAR(10),PLATFORM INT,CUSTOMER INT,CC INT, ID INT) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE RATE INT;
    SET RATE = NULL;
		SELECT Rat_Id FROM Rates
			WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = PLATFORM AND Cus_Id = CUSTOMER AND CC_Id = CC AND CI_Id = ID
            LIMIT 1 INTO RATE;
		IF (RATE IS NULL) THEN
			SELECT Rat_Id FROM Rates
				WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = PLATFORM AND Cus_Id = CUSTOMER AND CC_Id = CC AND CI_Id = 1
				LIMIT 1 INTO RATE;
			IF (RATE IS NULL) THEN
				SELECT Rat_Id FROM Rates
					WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = PLATFORM AND Cus_Id = CUSTOMER AND CC_Id = 1 AND CI_Id = 1
					LIMIT 1 INTO RATE;
				IF (RATE IS NULL) THEN
					SELECT Rat_Id FROM Rates
						WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = PLATFORM AND Cus_Id = 1 AND CC_Id = 1 AND CI_Id = 1
						LIMIT 1 INTO RATE;
					IF (RATE IS NULL) THEN
						SELECT Rat_Id FROM Rates
							WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = 1 AND Cus_Id = 1 AND CC_Id = 1 AND CI_Id = 1
							LIMIT 1 INTO RATE;
					ELSE
						SET RATE=NULL;
					END IF;
				END IF;
            END IF;
        END IF;
	RETURN RATE;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Rate_Price_Per_Hour
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Rate_Price_Per_Hour`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Rate_Price_Per_Hour` (RATE INT) RETURNS DECIMAL(20,6) DETERMINISTIC
BEGIN
	DECLARE PERIOD 			DECIMAL(20,6);
	DECLARE PRICE 			DECIMAL(20,6);
	DECLARE PRICE_PER_HOUR 	DECIMAL(20,6);
    SET PRICE_PER_HOUR = 0.0;
	SELECT Rat_Price,Rat_Period
		FROM	Rates
		WHERE	Rat_Id = RATE
		LIMIT 1 
        INTO PRICE,PERIOD;
	IF PRICE IS NOT NULL THEN
		IF 		PERIOD = 1 THEN
				SET PRICE_PER_HOUR = PRICE;
		ELSEIF 	PERIOD = 2 THEN
				SET PRICE_PER_HOUR = PRICE / 24 ;
		ELSEIF 	PERIOD = 3 THEN
				SET PRICE_PER_HOUR = (PRICE / 24) / 30;
		ELSE 
			SET PRICE_PER_HOUR = 0.0;
		END IF;
    END IF;
	RETURN PRICE_PER_HOUR;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Rate_Measure_Unit
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Rate_Measure_Unit`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Rate_Measure_Unit` (RATE INT) RETURNS VARCHAR(3) DETERMINISTIC
BEGIN
	DECLARE MEASURE_UNIT VARCHAR(3);
    SET MEASURE_UNIT = NULL;
	SELECT MU_Code
		FROM	Rates
		WHERE	Rat_Id = RATE
		LIMIT 1 
        INTO MEASURE_UNIT;
	RETURN MEASURE_UNIT;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Rate_Currency
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Rate_Currency`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Rate_Currency` (RATE INT) RETURNS VARCHAR(3) DETERMINISTIC
BEGIN
	DECLARE CURRENCY VARCHAR(3);
    SET CURRENCY = NULL;
	SELECT Cur_Code
		FROM	Rates
		WHERE	Rat_Id = RATE
		LIMIT 1 
        INTO CURRENCY;
	RETURN CURRENCY;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Price_For_Customer
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Price_For_Customer`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Price_For_Customer` (CUSTOMER INT,TYPE_CODE VARCHAR(10)) RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE RATE		INT;
    DECLARE PLATFORM	INT;
    DECLARE CC			INT;
    DECLARE ID			INT;
    DECLARE PRICE		FLOAT;
    
    SET PLATFORM	= 1;
    SET CC			= 1;
    SET ID			= 1;
    
    SET RATE		= Get_Rate_Id(TYPE_CODE,CUSTOMER,PLATFORM,CC,ID);
	SET PRICE		= Get_Rate_Price_Per_Hour(RATE);
    
    IF (PRICE = 0) THEN
		SET PRICE 	= Get_Price_For_Type(TYPE_CODE);
    END IF;    
    
    
	RETURN PRICE;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Price_For_Platform
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Price_For_Platform`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Price_For_Platform` (CUSTOMER INT,PLATFORM INT,TYPE_CODE VARCHAR(10)) RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE RATE		INT;
    DECLARE CC			INT;
    DECLARE ID			INT;
    DECLARE PRICE		FLOAT;
    
    SET CC			= 1;
    SET ID			= 1;
    
    SET RATE		= Get_Rate_Id(TYPE_CODE,CUSTOMER,PLATFORM,CC,ID);
	SET PRICE		= Get_Rate_Price_Per_Hour(RATE);
    
    IF (PRICE = 0) THEN
		SET PRICE 	= Get_Price_For_Customer(CUSTOMER,TYPE_CODE);
    END IF;    
    
	RETURN PRICE;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Price_For_Cost_Center
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Price_For_Cost_Center`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Price_For_Cost_Center` (CUSTOMER INT,PLATFORM INT,CC INT,TYPE_CODE VARCHAR(10)) RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE RATE		INT;
    DECLARE ID			INT;
    DECLARE PRICE		FLOAT;
    
    SET ID			= 1;
    
    SET RATE		= Get_Rate_Id(TYPE_CODE,CUSTOMER,PLATFORM,CC,ID);
	SET PRICE		= Get_Rate_Price_Per_Hour(RATE);
    
    IF (PRICE = 0) THEN
		SET PRICE = Get_Price_For_Platform(CUSTOMER,PLATFORM,TYPE_CODE);
    END IF;
	
    RETURN PRICE;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Price_For_Charge_Unit
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Price_For_Charge_Unit`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Price_For_Charge_Unit` (CUSTOMER INT,PLATFORM INT,CC INT,ID INT,TYPE_CODE VARCHAR(10)) RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE RATE		INT;
    DECLARE PRICE		FLOAT;
        
    SET RATE		= Get_Rate_Id(TYPE_CODE,CUSTOMER,PLATFORM,CC,ID);
	SET PRICE		= Get_Rate_Price_Per_Hour(RATE);
    
    IF (PRICE = 0) THEN
		SET PRICE = Get_Price_For_Cost_Center(CUSTOMER,PLATFORM,CC,TYPE_CODE);
    END IF;
    
	RETURN PRICE;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Price_For_Type
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Price_For_Type`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Price_For_Type` (TYPE_CODE VARCHAR(10)) RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE RATE		INT;
    
    DECLARE CUSTOMER	INT;
    DECLARE PLATFORM	INT;
    DECLARE CC			INT;
    DECLARE ID			INT;
    DECLARE PRICE		FLOAT;
    
    SET CUSTOMER	= 1;
    SET PLATFORM	= 1;
    SET CC			= 1;
    SET ID			= 1;
    
    SET RATE		= Get_Rate_Id(TYPE_CODE,CUSTOMER,PLATFORM,CC,ID);
	SET PRICE		= Get_Rate_Price_Per_Hour(RATE);
        
	RETURN PRICE;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Get_Billing_Resume
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Get_Billing_Resume`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Get_Billing_Resume` (CUSTOMER INT,DATE_FROM DATE,DATE_TO DATE,XSTATUS INT,XCUR VARCHAR(3))
BEGIN
	SELECT 
		COUNT(CIT_Date) 								AS ITEMS,
		Charge_Items.CIT_Status 						AS STAT,
        Charge_Units.Typ_Code							AS CU_TYPE,
		Customers.Cus_Id 								AS CUS,
		Customers.Cus_Name 								AS CUSTOMER,
        Platforms.Pla_Id								AS PLAT,
		Charge_Units.CC_Id 								AS CC_ID,
		Cost_Centers.CC_Code 							AS CC_CODE,
		Cost_Centers.CC_Description						AS CC,
		Configuration_Items.CI_Id 						AS CI_ID,
        Configuration_Items.CI_Name 					AS CI,
		Charge_Units.CU_Id 								AS CU_ID,
		Charge_Units.CU_Description 					AS CU,
        Rates.Rat_Id									AS RATE,
        Rates.Rat_Price									AS RATE_PRICE,
        Rates.Cur_Code 									AS RATE_CUR,
		Rates.MU_Code									AS MU,
        IF(Rates.Rat_Period=1,"HOUR",
			IF(Rates.Rat_Period=2,"DAY",
				IF(Rates.Rat_Period=3,"MONTH","ERR")))	AS RATE_PERIOD,
        Get_Rate_Price_Per_Hour(Rates.Rat_Id)			AS RATE_PRICE_HOURLY,                
        Charge_Units.CU_Operation 						AS OP,
		SUM(Convert_Unit(
			Charge_Items.CIT_Quantity,
            Charge_Units.CU_Operation)) 				AS Q,
		SUM(
			Get_Rate_Price_Per_Hour(Rates.Rat_Id)
			*Convert_Unit(
				Charge_Items.CIT_Quantity,
                Charge_Units.CU_Operation)
            ) 											AS ST_AT_RATE,

        Charge_Units.CU_Is_Billeable 					AS BILL,

        Get_Exchange_Rate(
			Rates.Cur_Code,
            Cost_Centers.Cur_Code,
            DATE_TO) 									AS CCXR,

        IF (Charge_Units.CU_Is_Billeable,
			SUM(
				Get_Rate_Price_Per_Hour(Rates.Rat_Id)
				*Convert_Unit(
					Charge_Items.CIT_Quantity,
                    Charge_Units.CU_Operation)
				*Get_Exchange_Rate(
					Rates.Cur_Code,
                    Cost_Centers.Cur_Code,
                    DATE_TO)
				),
			0) 											AS TOTAL_CC_CUR,

		Cost_Centers.Cur_Code							AS CC_CUR,

        Get_Exchange_Rate(
			Rates.Cur_Code,
            XCUR,
            DATE_TO) 									AS BILLXR,

        IF (Charge_Units.CU_Is_Billeable,
			SUM(
				Get_Rate_Price_Per_Hour(Rates.Rat_Id)
				*Convert_Unit(
					Charge_Items.CIT_Quantity,
                    Charge_Units.CU_Operation)
				*Get_Exchange_Rate(
					Rates.Cur_Code,
                    XCUR,
                    DATE_TO)
				),
			0) 											AS TOTAL_BILL_CUR,
		XCUR											AS XCUR

		FROM Charge_Items
			JOIN Charge_Units			USING (CU_Id) 
			JOIN Configuration_Items 	USING (CI_Id)
			JOIN Platforms 				USING (Pla_Id)
			JOIN Customers 				USING (Cus_Id)
            JOIN Cost_Centers			ON Charge_Units.CC_Id = Cost_Centers.CC_Id
            JOIN Rates					ON Rat_Id = Get_Rate_Id(	Charge_Units.Typ_Code,
																	Platforms.Pla_Id,
                                                                    Customers.Cus_Id,
																	Cost_Centers.CC_Id,
																	Charge_Units.CU_Id
																)
		WHERE
				Customers.Cus_Id=CUSTOMER
			AND CIT_Date >= DATE_FROM
			AND CIT_Date <= DATE_TO
			AND CIT_Status = XSTATUS
		GROUP BY 
			CUSTOMER,
			CU_Id,
			CU,
			CC,
            RATE,
            RATE_CUR
		ORDER BY
			CUSTOMER,
            CU_Id,
            CU,
            CC,
            RATE,
            RATE_CUR
    ;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Cycle_Start
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Cycle_Start`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Cycle_Start` (XYEAR INT, XMONTH INT) RETURNS DATE DETERMINISTIC
BEGIN
	DECLARE XSTART DATE;
    SET XSTART = STR_TO_DATE(CONCAT(XYEAR,"-",XMONTH,"-1"),"%Y-%m-%d");
    RETURN XSTART;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Cycle_End
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Cycle_End`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Cycle_End` (XYEAR INT, XMONTH INT) RETURNS DATE DETERMINISTIC
BEGIN
	DECLARE XSTART DATE;
	SET XSTART=Get_Cycle_Start(XYEAR,XMONTH);
    RETURN LAST_DAY(XSTART);
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Get_Billing_Resume_For_Cycle
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Get_Billing_Resume_For_Cycle`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Get_Billing_Resume_For_Cycle` (CUSTOMER INT,XYEAR INT,XMONTH INT,XSTATUS INT)
BEGIN
	CALL Get_Billing_Resume(CUSTOMER,Get_Cycle_Start(XYEAR,XMONTH),Get_Cycle_End(XYEAR,XMONTH),XSTATUS);
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_Exchange_Rate
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_Exchange_Rate`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_Exchange_Rate` (CURRENCY_FROM VARCHAR(3),CURRENCY_TO VARCHAR(3),XDATE DATE)
	RETURNS DECIMAL(20,10) DETERMINISTIC
BEGIN
	DECLARE XR 				DECIMAL(20,10);
	DECLARE XRFROM 			DECIMAL(20,10);
	DECLARE XRTO 			DECIMAL(20,10);
	DECLARE DATE_FROM_MAX	DATE;
	DECLARE DATE_TO_MAX		DATE;
    
	# Gets range of valid Exchange Rates for CURRENCYs Pair searched
    # From CURRENCY
    
#	SELECT MIN(ER_Date_From),MAX(ER_Date_From) FROM Exchange_Rates
	SELECT MAX(ER_Date) FROM Exchange_Rates
		WHERE 
			Cur_Code 	= 	CURRENCY_FROM AND
            ER_Date		<= 	XDATE
		INTO DATE_FROM_MAX;
	# To CURRENCY
#	SELECT MIN(ER_Date_From),MAX(ER_Date_From) FROM Exchange_Rates
	SELECT MAX(ER_Date) FROM Exchange_Rates
		WHERE 
			Cur_Code		= CURRENCY_TO AND
            ER_Date			<= XDATE
		INTO DATE_TO_MAX;
        
	IF (CURRENCY_FROM = "USD") THEN
		SET XRFROM = 1.0;
	ELSE
		SELECT ER_Factor FROM Exchange_Rates
			WHERE 
				Cur_Code		=	CURRENCY_FROM	AND
				ER_Date		 	=	DATE_FROM_MAX	
			INTO XRFROM;
    END IF;
    
    IF (CURRENCY_TO = "USD") THEN
		SET XRTO = 1.0;
	ELSE
		SELECT ER_Factor FROM Exchange_Rates
			WHERE 
				Cur_Code		=	CURRENCY_TO	AND
				ER_Date		 	=	DATE_TO_MAX	
			INTO XRTO;
			
    END IF;
	# Actual Exchange Rate is composed by product of 2 factors FROM->USD * USD -> TO
    IF ((XRFROM IS NULL) OR (XRFROM = 0)) THEN
		SET XRFROM=0;
		SET XRTO=1;
    END IF;
    IF ((XRTO IS NULL) OR (XRTO = 0)) THEN
		SET XRFROM=0;
		SET XRTO=1;
    END IF;
	SET XR = ROUND(XRFROM/XRTO,10);
 
	RETURN XR;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_CI_Id_From_UUID
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_CI_Id_From_UUID`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_CI_Id_From_UUID` (UUID VARCHAR(45)) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE ID INT;
    SELECT CI_Id FROM Configuration_Items WHERE CI_UUID=UUID LIMIT 1 INTO ID;
	RETURN ID;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_CI_UUID_From_Id
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_CI_UUID_From_Id`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_CI_UUID_From_Id` (ID INT) RETURNS VARCHAR(45) DETERMINISTIC
BEGIN
	DECLARE UUID VARCHAR(45);
    SELECT CI_UUID FROM Configuration_Items WHERE CI_Id=ID LIMIT 1 INTO UUID;
	RETURN UUID;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_CU_UUID_From_Id
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_CU_UUID_From_Id`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_CU_UUID_From_Id` (ID INT) RETURNS VARCHAR(45) DETERMINISTIC
BEGIN
	DECLARE UUID VARCHAR(45);
    SELECT CU_UUID FROM Charge_Units WHERE CU_Id=ID LIMIT 1 INTO UUID;
	RETURN UUID;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_CU_Id_From_UUID
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_CU_Id_From_UUID`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE DEFINER=`root`@`%` FUNCTION `Get_CU_Id_From_UUID`(UUID VARCHAR(45),XCI_ID INT,XTYPE VARCHAR(10)) RETURNS int(11)
    DETERMINISTIC
BEGIN
	DECLARE ID INT;
    SELECT CU_Id FROM Charge_Units
		WHERE	CU_UUID=UUID AND
				CI_ID = XCI_ID AND
                Typ_Code = XTYPE
        LIMIT 1 INTO ID;
	RETURN ID;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Convert_Unit
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Convert_Unit`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Convert_Unit` (Q FLOAT,OPERATION VARCHAR(10)) RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE R FLOAT;
    # Byte TO
    IF     (OPERATION="NONE") THEN
		RETURN Q;
    # Byte TO
    ELSEIF (OPERATION="BTOKB") THEN
		RETURN Q/1024;
	ELSEIF (OPERATION="BTOMB") THEN
		RETURN (Q/1024)/1024;    
	ELSEIF (OPERATION="BTOGB") THEN
		RETURN ((Q/1024)/1024)/1024; 
	# KB TO
	ELSEIF (OPERATION="KBTOB") THEN
		RETURN Q*1024;
	ELSEIF (OPERATION="KBTOMB") THEN
		RETURN Q/1024;
	ELSEIF (OPERATION="KBTOGB") THEN
		RETURN (Q/1024)/1024;
	# MB TO
	ELSEIF (OPERATION="MBTOB") THEN
		RETURN (Q*1024)*1024;    
	ELSEIF (OPERATION="MBTOKB") THEN
		RETURN Q*1024;    
	ELSEIF (OPERATION="MBTOGB") THEN
		RETURN Q/1024;    
	# GB TO
    ELSEIF (OPERATION="GBTOB") THEN
		RETURN ((Q*1024)*1024)*1024;    
    ELSEIF (OPERATION="GBTOKB") THEN
		RETURN (Q*1024)*1024;    
    ELSEIF (OPERATION="GBTOMB") THEN
		RETURN Q*1024;
	# HOUR TO
    ELSEIF (OPERATION="HTOD") THEN
		RETURN Q/24;    
    ELSEIF (OPERATION="HTOM") THEN
		RETURN (Q/24)/30;    
	# DAY TO
    ELSEIF (OPERATION="DTOH") THEN
		RETURN Q*24;    
    ELSEIF (OPERATION="DTOM") THEN
		RETURN Q/30;    
	# MONTH TO
    ELSEIF (OPERATION="MTOH") THEN
		RETURN Q*24*30;    
    ELSEIF (OPERATION="MTOD") THEN
		RETURN Q*24;    
    END IF;
	RETURN 0;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_CU_Id_From_Data
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_CU_Id_From_Data`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_CU_Id_From_Data` (X_CI_UUID VARCHAR(45),X_CU_UUID VARCHAR(45),CU_TYPE VARCHAR(10)) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE ID INT;
    
    
    IF (X_CU_UUID IS NULL) OR (X_CU_UUID = '' ) THEN
		SELECT CU_Id FROM Charge_Units
			JOIN Configuration_Items using (CI_Id)
		WHERE CI_UUID=X_CI_UUID AND
			Typ_Code=CU_TYPE
		LIMIT 1 INTO ID;
    ELSE 
		IF LENGTH(X_CU_UUID)> 0 THEN
			SELECT CU_Id FROM Charge_Units
				JOIN Configuration_Items using (CI_Id)
			WHERE	CI_UUID = X_CI_UUID AND
					CU_UUID = X_CU_UUID AND
					Typ_Code=CU_TYPE
			LIMIT 1 INTO ID;        
        END IF;
	END IF;
	RETURN ID;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Record_Item
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Record_Item`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Record_Item` (CU_TYPE VARCHAR(10),CI_UUID VARCHAR(45),CU_UUID VARCHAR(45),QUANTITY DECIMAL(20,6) ,X_DATE DATE,X_TIME TIME,X_ACTIVE BOOLEAN)
BEGIN
	DECLARE _CI_ID		INT;
	DECLARE _CU_ID		INT;
	DECLARE _Q	 		DECIMAL(20,6);
	DECLARE X_DATE_TIME	VARCHAR(45);
    
    SET X_DATE_TIME = CONCAT(X_DATE," ",X_TIME);
	SET QUANTITY    = ROUND(QUANTITY,6);
    
    # Needs to be sure that recursion is possible
    SET @@max_sp_recursion_depth = 8;
    
    # Verifies if CI_UUID Corresponds to a valid Configuration Item
    
    SET _CI_ID = Get_CI_Id_From_UUID(CI_UUID);
    
    IF _CI_ID IS NOT NULL THEN
		# Gets Configuration Unit Id from raw DataType of CU and UUID for CI and CU
		SET _CU_ID = Get_CU_Id_From_Data(CI_UUID,CU_UUID,CU_TYPE);

        # Checks if a valid CU Id was found
		IF _CU_ID IS NOT NULL THEN
			# Creates an Item billing record for the valud Charge Unit
            # ----------------------------------------------------------------------------
            SELECT CIT_Quantity FROM Charge_Items WHERE CU_Id=_CU_ID AND CIT_Date=X_DATE AND CIT_Time=X_TIME LIMIT 1 INTO _Q;

            IF _Q IS NULL THEN
				START TRANSACTION;
				INSERT IGNORE INTO Charge_Items VALUES(_CU_ID,X_DATE,X_TIME,ROUND(QUANTITY,6),1,X_ACTIVE,X_DATE_TIME); # STATUS = 1 Created, Pending Approval
				COMMIT;
			ELSE 
				IF QUANTITY > _Q THEN
					START TRANSACTION;
					UPDATE Charge_Items SET CIT_QUANTITY = ROUND(QUANTITY,6) WHERE CU_Id=_CU_ID AND CIT_Date=X_DATE AND CIT_Time=X_TIME; # STATUS = 1 Created, Pending Approval
                    COMMIT;
                END IF;
            END IF;
            # ----------------------------------------------------------------------------
		ELSE 
			# Tries to complete DB Integrity by creating a Dummy Charge Unit
			CALL Create_Charge_Unit(_CI_ID,NULL, CU_UUID,1,1,QUANTITY,NULL,CU_TYPE,NULL,NULL,NULL,NULL); # 1 = Is Billeable
            SET _CU_ID =  Get_CU_Id_From_Data(CI_UUID,CU_UUID,CU_TYPE);
            IF _CU_ID IS NOT NULL THEN
				CALL Record_Item (CU_TYPE,CI_UUID,CU_UUID,QUANTITY,X_DATE,X_TIME,X_ACTIVE); # Recursive Call
            END IF;
		END IF;
	ELSE
		# Tries to complete DB Integrity by creating a Dummy Configuration Item
		CALL Create_Configuration_Item(NULL,CI_UUID,1,1,1);
        # Validates if a valid Configuration Item was created 
		SET _CI_ID = Get_CI_Id_From_UUID(CI_UUID);
		IF _CI_ID IS NOT NULL THEN
       		#call Tracer("P8 Llamada recursiva por CI recreado");		# Checks if a valid CU Id was found
			CALL Record_Item (CU_TYPE,CI_UUID,CU_UUID,QUANTITY,X_DATE,X_TIME,X_ACTIVE); # Recursive Call
        END IF;
	END IF;
 
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Create_Configuration_Item
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Create_Configuration_Item`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Create_Configuration_Item` (CI_NAME VARCHAR(45),CI_UUID VARCHAR(45),PLATFORM INT,CC INT,CUSTOMER INT)
BEGIN
	DECLARE XID		 	INT;
	DECLARE XNAME	 	VARCHAR(45);
	DECLARE XPLATFORM 	INT;
	DECLARE XCC			INT;
	DECLARE XCIT_GEN	INT;
	DECLARE XDATETIME	DATETIME;
	
	SET XNAME	 	= IF(CI_NAME IS NULL,"CI NO NAME",CI_NAME);
	SET XPLATFORM 	= IF(PLATFORM IS NULL,1,PLATFORM);
	SET XCC 		= IF(CC IS NULL,1,CC);
    
    # Checks for existence of CI
    SET XID 		= Get_CI_Id_From_UUID(CI_UUID);

	# If CI does not exists then creates it
	IF XID IS NULL THEN
			START TRANSACTION;
			INSERT INTO Configuration_Items VALUES(0,XNAME,CI_UUID,XPLATFORM,XCC,CUSTOMER,NOW(),NULL);
            COMMIT;
	END IF;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Create_Charge_Unit
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Create_Charge_Unit`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Create_Charge_Unit` (CI_ID INT,DESCRIPTION VARCHAR(45),CU_UUID VARCHAR(45),ISBILLEABLE BOOLEAN,ISALLWAYS BOOLEAN,QUANTITY DECIMAL(20,6),OPERATION VARCHAR(10),CU_TYPE VARCHAR(10),CIT_GENERATION INT,REF1 VARCHAR(45),REF2 VARCHAR(45),REF3 VARCHAR(45))
BEGIN
	DECLARE CU_ID 				INT;
	DECLARE XDESCRIPTION	 	VARCHAR(45);
	DECLARE XISBILLEABLE	 	BOOLEAN;
	DECLARE XISALLWAYS	 		BOOLEAN;
	DECLARE XOPERATION			VARCHAR(10);
	#DECLARE XCC_ID				VARCHAR(10);
	DECLARE XCIT_GENERATION		INT;
	
	SET XDESCRIPTION 	= IF(DESCRIPTION 	IS NULL,"CU NO DESCRIPTION",DESCRIPTION);
	SET XISBILLEABLE 	= IF(ISBILLEABLE 	IS NULL,TRUE,ISBILLEABLE);
	SET XISALLWAYS   	= IF(ISALLWAYS   	IS NULL,TRUE,ISALLWAYS);
	SET XOPERATION   	= IF(OPERATION   	IS NULL,"NONE",OPERATION);
	#SET XCC_ID	   	 	= IF(CC_ID       	IS NULL,1,CC_ID);
	SET XCIT_GENERATION = IF(CIT_GENERATION	IS NULL,1,CIT_GENERATION);
    
    # Checks for CU existence
    SET CU_ID = Get_CU_Id_From_UUID(CU_UUID,CI_ID,CU_TYPE);

	# If CU does not exist then creates it
	IF CU_ID IS NULL THEN
			START TRANSACTION;
			#INSERT IGNORE INTO Charge_Units VALUES(0,CI_ID,XDESCRIPTION,CU_UUID,XISBILLEABLE,XISALLWAYS,QUANTITY,XOPERATION,CU_TYPE,XCC_ID,XCIT_GENERATION,0,REF1,REF2,REF3);
			INSERT IGNORE INTO Charge_Units VALUES(0,CI_ID,XDESCRIPTION,CU_UUID,XISBILLEABLE,XISALLWAYS,QUANTITY,XOPERATION,CU_TYPE,XCIT_GENERATION,0,REF1,REF2,REF3);
			COMMIT;
    END IF;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Get_Billing_Details
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Get_Billing_Details`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Get_Billing_Details` (CUSTOMER INT,DATE_FROM DATE,DATE_TO DATE,XSTATUS INT)
BEGIN
	SELECT 
		CIT_Status 						AS STAT,
		
        Cus_Id 							AS CUS,
		Cus_Name 						AS CUSTOMER,
		CI_Id 							AS CI_ID,
		CU_Id 							AS CU_ID,
        CI_Name 						AS CI,
		CU_Description 					AS CU,
		CC_Id 							AS CC,
        Cur_Code 						AS CUR,
		Get_Price_For_Charge_Unit(
			Cus_Id,
            Pla_id,
            CC_Id,
            CU_Id,
            Typ_Code)					AS PRICE,
        CU_Operation 					AS OP,
		Convert_Unit(
			CIT_Quantity,
            CU_Operation) 				AS Q,
        Get_Rate_Measure_Unit(
			Get_Rate_Id(
				Typ_Code,
                Cus_Id,
                Pla_id,
                CC_Id,
                CU_Id)) 				AS MU,
		Get_Price_For_Charge_Unit(
			Cus_Id,
            Pla_id,
            CC_Id,
            CU_Id,
            Typ_Code)
			*Convert_Unit(
				CIT_Quantity,
                CU_Operation)
             							AS SUBTOTAL,
        Get_Exchange_Rate(
			Cur_Code,
            "USD",
            DATE_TO) 
										AS ER,
        CU_Is_Billeable 				AS BILL,
        IF (CU_Is_Billeable,
			Get_Price_For_Charge_Unit(
					Cus_Id,
                    Pla_id,
                    CC_Id,
                    CU_Id,
                    Typ_Code)
				*Convert_Unit(
					CIT_Quantity,
                    CU_Operation)
				*Get_Exchange_Rate(
					Cur_Code,
                    "USD",
                    DATE_TO)
				,
			0) 							AS USD
		FROM Charge_Items
			JOIN Charge_Units			USING (CU_Id) 
			JOIN Configuration_Items 	USING (CI_Id)
			JOIN Platforms 				USING (Pla_Id)
			JOIN Customers 				USING (Cus_Id)
            JOIN Cost_Centers			USING (CC_Id)
		WHERE
				Cus_Id=CUSTOMER
			AND CIT_Date >= DATE_FROM
			AND CIT_Date <= DATE_TO
			AND CIT_Status = XSTATUS
		ORDER BY
			CUSTOMER,
            CU_Id,
            CU,
            CC
    ;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Tracer
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Tracer`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Tracer` (L VARCHAR(128))
BEGIN
	START TRANSACTION;
    INSERT INTO Trace Values (0,L);
    COMMIT;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_CU_CC
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_CU_CC`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_CU_CC` (CU INT) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE CC 	INT;
	DECLARE CI 	INT;
	DECLARE CUS INT;
    # Try to get CC from Cost Unit specification
    SELECT CC_Id,CI_Id FROM Charge_Units WHERE CU_Id=CU LIMIT 1 INTO CC,CI;
    IF CC IS NULL THEN
		# If CC not gotten from CU will look in corresponding CI
		IF CI IS NULL THEN 
			# Null CI is an ERROR (NULL CC is returned)
			SET CC = NULL;
		ELSE
			# Will look for Default Cost Center as per CI Definition
			SELECT CC_Id,Cus_Id FROM Configuration_Items WHERE CI_Id=CI LIMIT 1 INTO CC,CUS;
			IF CC IS NULL THEN 
				# If CC not gotten from CI will look in corresponding Customer
				IF CUS IS NULL THEN
					# Null Customer is an ERROR (NULL CC is returned)
					SET CC = NULL;
				ELSE
					SELECT CC_Id FROM Customers WHERE Cus_Id=CUS LIMIT 1 INTO CC;
                END IF;
			END IF;
		END IF;
	END IF;
	RETURN CC;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Update_CU_Rates
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Update_CU_Rates`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Update_CU_Rates` ()
BEGIN
	START TRANSACTION;
	UPDATE
		Charge_Units as CU
			JOIN Configuration_Items	AS CI     USING (CI_Id)
		#SET Rat_Id = Get_Rate_Id(Typ_Code,Pla_Id,Cus_Id,CU.CC_Id,CU_Id)
		SET CU.Rat_Id = Get_Rate_Id(CU.Typ_Code,CI.Pla_Id,Cus_Id,CI.CC_Id,CU.CI_Id)
		;
	COMMIT;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Get_Charge_Resume
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Get_Charge_Resume`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Get_Charge_Resume` (CUS INT,DFROM DATE,DTO DATE,STATUS INT,CUR VARCHAR(3))
BEGIN
	SELECT * FROM 	Charge_Resumes
		WHERE	Cus_Id 			=  CUS
			AND CR_Date_From   	=  DFROM
			AND CR_Date_To   	=  DTO
			AND CIT_Status 		=  STATUS
			AND Cur_Code 		=  CUR
		ORDER BY	Cus_Id,CI_CC_Id,CI_Id;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Update_Charge_Resume_CI
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Update_Charge_Resume_CI`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Update_Charge_Resume_CI` (XCUS_ID INT,XDATE_FROM DATE,XDATE_TO DATE,XCIT_STATUS INT,XCUR_CODE VARCHAR(3),XCI_ID INT)
BEGIN
	START TRANSACTION;
	DELETE
		FROM 	Charge_Resumes
		WHERE	Cus_Id 			=  XCUS_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE
            AND CI_Id			=  XCI_ID;
	COMMIT;
    START TRANSACTION;
	INSERT
		INTO	Charge_Resumes
			(	Cus_Id,
				CR_Date_From,
                CR_Date_To,
                CIT_Status,
                Cur_Code,
                CIT_Count,
                CIT_Quantity,
                CIT_Generation,
                CU_Id,
                CI_CC_Id,
                CU_Operation,
                Typ_Code,
                CC_Cur_Code,
                CI_Id,
                Rat_Id,
                Rat_Price,
                Rat_MU_Code,
                Rat_Cur_Code,
                Rat_Period,
                Rat_Hourly,
                Rat_Daily,
                Rat_Monthly,
                CR_Quantity,
                CR_Quantity_at_Rate,
                CC_XR,
                CR_Cur_XR,
                CR_ST_at_Rate_Cur,
                CR_ST_at_CC_Cur,
                CR_ST_at_Cur,
                Cus_Name,
                CC_Description,
                CI_Name,
                CU_Description,
                Rat_Period_Description
			)
	SELECT 
        XCUS_ID 			AS CUS_ID,
		XDATE_FROM			AS DATE_FROM,
        XDATE_TO			AS DATE_TO,
        XCIT_STATUS			AS CIT_STATUS,
        XCUR_CODE			AS CUR_CODE,
		COUNT(*) 			AS CIT_COUNT,
        sum(CIT_Quantity) 	AS CIT_QUANTITY,
        CU.CIT_Generation 	AS CIT_GENERATION,
        CIT.CU_Id 			AS CU_ID,
        CI.CC_Id 			AS CI_CC_ID,
        CU.CU_Operation		AS CU_OPERATION,
        CU.Typ_Code			AS TYP_CODE,
        CC.Cur_Code			AS CC_CUR_CODE,
		XCI_ID 				AS CI_ID,
        CU.Rat_Id 			AS RAT_ID,
		RAT.Rat_Price		AS RAT_PRICE,
        RAT.MU_Code			AS RAT_MU_CODE,
        RAT.Cur_Code		AS RAT_CUR_CODE,
        RAT.Rat_Period		AS RAT_PERIOD,
        0					AS RAT_HOURLY,
        0					AS RAT_DAILY,
        0					AS RAT_MONTHLY,
        0					AS CR_QUANTITY,
        0					AS CR_QUANTITY_AT_RATE,
        1					AS CC_XR,
        1					AS CR_CUR_XR,
        0					AS ST_AT_RATE_CUR,
        0					AS ST_AT_CC_CUR,
        0					AS ST_AT_CUR,
        CUS.Cus_Name		AS CUS_NAME,
        CC.CC_Description	AS CC_DESCRIPTION,
        CI.CI_Name			AS CI_NAME,
        CU.CU_Description	AS CU_DESCRIPTION,
        IF(Rat_Period=1,"HOUR",IF(Rat_Period=2,"DAY",IF(RAT_Period=3,"MONTH","ERROR")))
							AS RAT_PERIOD_DESCRIPTION
		FROM Charge_Items 				AS CIT
			JOIN Charge_Units 			AS CU 	USING (CU_Id)
			JOIN Configuration_Items 	AS CI 	USING (CI_Id)
            JOIN Cost_Centers			AS CC	ON 	  (CC.CC_Id=CI.CC_Id)
			JOIN Customers 				AS CUS 	USING (Cus_Id)
			JOIN Rates 					AS RAT 	USING (Rat_Id)
		WHERE 	CIT_Status  =  XCIT_STATUS
			AND CIT_Date   >= XDATE_FROM
			AND CIT_Date   <= XDATE_TO
			AND CUS.Cus_Id  =  XCUS_ID
            AND CU.CI_Id    =  XCI_ID
		GROUP BY CIT.CU_Id
        ORDER BY CUS_ID,CI.CC_Id,CI.CI_Id,CIT.CU_Id
        ;
	COMMIT;
    START TRANSACTION;
	UPDATE Charge_Resumes
		SET CR_ST_at_Rate_Cur   =  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)),
			CR_ST_at_CC_Cur     =  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)) * CC_XR,
			CR_ST_at_Cur      	=  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)) * CR_Cur_XR
		WHERE	Cus_Id 			= XCUS_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE
            AND CI_Id           = XCI_ID;
	UPDATE Charge_Resumes
		SET CR_Quantity=IF(CU_Operation="NONE",CIT_Quantity,Convert_Unit(CIT_Quantity,CU_Operation))
		WHERE	Cus_Id 			= XCUS_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE
            AND CI_Id           = XCI_ID;
	UPDATE Charge_Resumes
		SET CR_Quantity_at_Rate = IF(CIT_Generation=1,CR_Quantity/IF(Rat_Period=3,720,IF(Rat_Period=2,24,1)),CR_Quantity)
		WHERE	Cus_Id 			= XCUS_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE
            AND CI_Id           = XCI_ID;
	UPDATE Charge_Resumes
		SET CC_XR = Get_Exchange_Rate(Rat_Cur_Code,CC_Cur_Code,CR_Date_To)
		WHERE	Cus_Id 			=  XCUS_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE
            AND CI_Id           =  XCI_ID;
	UPDATE Charge_Resumes
		SET CR_Cur_XR = Get_Exchange_Rate(Rat_Cur_Code,Cur_Code,CR_Date_To)
		WHERE	Cus_Id 			=  XCUS_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE
            AND CI_Id           =  XCI_ID
			AND Cur_Code 		!= Rat_Cur_Code;            
	UPDATE Charge_Resumes
		#SET CR_ST_at_Rate_Cur   =  CR_Quantity * Rat_Hourly,
		#	CR_ST_at_CC_Cur     =  CR_Quantity * Rat_Hourly * CC_XR,
		#	CR_ST_at_Cur      	=  CR_Quantity * Rat_Hourly * CR_Cur_XR
		SET CR_ST_at_Rate_Cur   =  CR_Quantity_at_Rate * Rat_Price,
			CR_ST_at_CC_Cur     =  CR_Quantity_at_Rate * Rat_Price * CC_XR,
			CR_ST_at_Cur      	=  CR_Quantity_at_Rate * Rat_Price * CR_Cur_XR
		WHERE	Cus_Id 			=  XCUS_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE
            AND CI_Id           =  XCI_ID;
	COMMIT;
    SELECT COUNT(*) AS RECORDS FROM Charge_Resumes
    #SELECT * FROM Charge_Resumes
		WHERE	Cus_Id 			=  XCUS_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE
            AND CI_Id           =  XCI_ID;

END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure User_Can_CC
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`User_Can_CC`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `User_Can_CC` (IN USER_ID INT, IN CC INT, OUT CAN BOOLEAN)
BEGIN
	DECLARE USER_CC     INT;
	DECLARE PARENT_CC   INT;
	DECLARE PARENT_CODE VARCHAR(45);
    
    # Needs to be sure that recursion is possible
    SET @@max_sp_recursion_depth = 8;
	
    SET CAN = FALSE;
    
    SELECT CC_Id FROM Users WHERE id=USER_ID INTO USER_CC;
    # Check if required CC matched Users Top Cost Center
    IF USER_CC IS NOT NULL AND USER_CC = 1 THEN
		SET CAN = TRUE;
	ELSE
		IF USER_CC IS NOT NULL AND USER_CC > 1 THEN
			IF USER_CC = CC THEN
				SET CAN = TRUE;
			ELSE
				# If CC does not match User's default CC then check for Parent CC
				SELECT CC_Parent_Code FROM Cost_Centers WHERE CC_Id=CC INTO PARENT_CODE;
				SELECT CC_Id FROM Cost_Centers WHERE CC_Code=PARENT_CODE INTO PARENT_CC;
				IF PARENT_CC IS NOT NULL AND PARENT_CC > 1 THEN
					# If parent CC matches User's default CC then returns True , else recurse one level Up
					IF PARENT_CC = CC THEN
						SET CAN = TRUE;
					ELSE
						# An stored procedure can be called recursively
						# It will recurse up to match or Parent = 1 (NO more parents up)
						CALL User_Can_CC(USER_ID,PARENT_CC,CAN);
					END IF;
				END IF;
			END IF;
		END IF;
    END IF;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function usercancc
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`usercancc`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION usercancc(USER_ID INT,CC INT) RETURNS BOOLEAN DETERMINISTIC
BEGIN
    DECLARE CAN BOOLEAN;
    CALL User_Can_CC(USER_ID, CC, CAN);
    RETURN CAN;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Update_User_Resume_CI
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Update_User_Resume_CI`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Update_User_Resume_CI` (XDATE_FROM DATE,XDATE_TO DATE,XCIT_STATUS INT,XCUR_CODE VARCHAR(3),XCI_ID INT)
BEGIN
	START TRANSACTION;
	DELETE
		FROM 	User_Resumes
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE;
	COMMIT;
    START TRANSACTION;
	INSERT
		INTO	User_Resumes
			(	Cus_Id,
				CR_Date_From,
                CR_Date_To,
                CIT_Status,
                Cur_Code,
                CIT_Count,
                CIT_Quantity,
                CIT_Generation,
                CU_Id,
                CI_CC_Id,
                CU_Operation,
                Typ_Code,
                CC_Cur_Code,
                CI_Id,
                Rat_Id,
                Rat_Price,
                Rat_MU_Code,
                Rat_Cur_Code,
                Rat_Period,
                Rat_Hourly,
                Rat_Daily,
                Rat_Monthly,
                CR_Quantity,
                CR_Quantity_at_Rate,
                CC_XR,
                CR_Cur_XR,
                CR_ST_at_Rate_Cur,
                CR_ST_at_CC_Cur,
                CR_ST_at_Cur,
                Cus_Name,
                CC_Description,
                CI_Name,
                CU_Description,
                Rat_Period_Description,
                CC_Code
			)
	SELECT 
        CI.Cus_Id 			AS CUS_ID,
		XDATE_FROM			AS DATE_FROM,
        XDATE_TO			AS DATE_TO,
        XCIT_STATUS			AS CIT_STATUS,
        XCUR_CODE			AS CUR_CODE,
		COUNT(*) 			AS CIT_COUNT,
        sum(CIT_Quantity) 	AS CIT_QUANTITY,
        CU.CIT_Generation 	AS CIT_GENERATION,
        CIT.CU_Id 			AS CU_ID,
        CI.CC_Id 			AS CI_CC_ID,
        CU.CU_Operation		AS CU_OPERATION,
        CU.Typ_Code			AS TYP_CODE,
        CC.Cur_Code			AS CC_CUR_CODE,
		XCI_ID 				AS CI_ID,
        CU.Rat_Id 			AS RAT_ID,
		RAT.Rat_Price		AS RAT_PRICE,
        RAT.MU_Code			AS RAT_MU_CODE,
        RAT.Cur_Code		AS RAT_CUR_CODE,
        RAT.Rat_Period		AS RAT_PERIOD,
        0					AS RAT_HOURLY,
        0					AS RAT_DAILY,
        0					AS RAT_MONTHLY,
        0					AS CR_QUANTITY,
        0					AS CR_QUANTITY_AT_RATE,
        1					AS CC_XR,
        1					AS CR_CUR_XR,
        0					AS ST_AT_RATE_CUR,
        0					AS ST_AT_CC_CUR,
        0					AS ST_AT_CUR,
        CUS.Cus_Name		AS CUS_NAME,
        CC.CC_Description	AS CC_DESCRIPTION,
        CI.CI_Name			AS CI_NAME,
        CU.CU_Description	AS CU_DESCRIPTION,
        IF(Rat_Period=1,"HOUR",IF(Rat_Period=2,"DAY",IF(RAT_Period=3,"MONTH","ERROR")))
							AS RAT_PERIOD_DESCRIPTION,
		CC.CC_Code			AS CC_CODE
		FROM Charge_Items 				AS CIT
			JOIN Charge_Units 			AS CU 	USING (CU_Id)
			JOIN Configuration_Items 	AS CI 	USING (CI_Id)
            JOIN Cost_Centers			AS CC	ON 	  (CC.CC_Id=CI.CC_Id)
			JOIN Customers 				AS CUS 	USING (Cus_Id)
			JOIN Rates 					AS RAT 	USING (Rat_Id)
		WHERE 	CIT_Status  =  XCIT_STATUS
			AND CIT_Date   >= XDATE_FROM
			AND CIT_Date   <= XDATE_TO
            AND CU.CI_Id    =  XCI_ID
		GROUP BY CIT.CU_Id
        ORDER BY CUS_ID,CI.CC_Id,CI.CI_Id,CIT.CU_Id
        ;
	COMMIT;
    START TRANSACTION;
	UPDATE User_Resumes
		SET CR_ST_at_Rate_Cur   =  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)),
			CR_ST_at_CC_Cur     =  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)) * CC_XR,
			CR_ST_at_Cur      	=  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)) * CR_Cur_XR
		WHERE	CI_Id 			= XCI_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE;
	UPDATE User_Resumes
		SET CR_Quantity=IF(CU_Operation="NONE",CIT_Quantity,Convert_Unit(CIT_Quantity,CU_Operation))
		WHERE	CI_Id 			= XCI_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE;
	UPDATE User_Resumes
		SET CR_Quantity_at_Rate = IF(CIT_Generation=1,CR_Quantity/IF(Rat_Period=3,720,IF(Rat_Period=2,24,1)),CR_Quantity)
		WHERE	CI_Id 			= XCI_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE;
	UPDATE User_Resumes
		SET CC_XR = Get_Exchange_Rate(Rat_Cur_Code,CC_Cur_Code,CR_Date_To)
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE;
	UPDATE User_Resumes
		SET CR_Cur_XR = Get_Exchange_Rate(Rat_Cur_Code,Cur_Code,CR_Date_To)
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE
			AND Cur_Code 		!= Rat_Cur_Code;            
	UPDATE User_Resumes
		SET CR_ST_at_Rate_Cur   =  CR_Quantity_at_Rate * Rat_Price,
			CR_ST_at_CC_Cur     =  CR_Quantity_at_Rate * Rat_Price * CC_XR,
			CR_ST_at_Cur      	=  CR_Quantity_at_Rate * Rat_Price * CR_Cur_XR
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE;
	COMMIT;
    SELECT COUNT(*) AS RECORDS FROM User_Resumes
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE;

END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Get_User_Resume
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Get_User_Resume`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Get_User_Resume` (USER_ID INT,DFROM DATE,DTO DATE,STATUS INT,CUR VARCHAR(3),CC_TOP INT)
BEGIN
	SELECT * FROM 	User_Resumes
		WHERE	CI_CC_Id 		IN (SELECT CC_Id FROM Cost_Centers WHERE usercancc(USER_ID,CC_Id) AND ccisbelow(CC_Id,CC_TOP))
			AND CR_Date_From   	=  DFROM
			AND CR_Date_To   	=  DTO
			AND CIT_Status 		=  STATUS
			AND Cur_Code 		=  CUR
		ORDER BY	Cus_Id,CI_CC_Id,CI_Id;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_CC_Id_From_Code
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_CC_Id_From_Code`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_CC_Id_From_Code` (X_CC_CODE VARCHAR(45)) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE ID INT;
        
    IF (X_CC_CODE IS NULL) OR (X_CC_CODE = '' ) THEN
		SET ID = 0;
    ELSE 
		IF LENGTH(X_CC_CODE)> 0 THEN
			SELECT CC_Id FROM Cost_Centers
			WHERE	CC_Code = X_CC_Code
			LIMIT 1 INTO ID;        
        END IF;
	END IF;
	RETURN ID;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure CC_Is_Below
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`CC_Is_Below`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `CC_Is_Below` (IN CC INT, IN CC_TOP INT, OUT IS_BELOW BOOLEAN)
BEGIN
	DECLARE X_CC   		INT;
	DECLARE PARENT_CC   INT;
	DECLARE PARENT_CODE VARCHAR(45);
    
    # Needs to be sure that recursion is possible
    SET @@max_sp_recursion_depth = 8;
	
    SET IS_BELOW = FALSE;
    
    SELECT CC_Id,CC_Parent_Code FROM Cost_Centers WHERE CC_Id=CC INTO X_CC,PARENT_CODE;
    
    IF X_CC IS NOT NULL AND X_CC > 1 THEN
		SELECT CC_Id FROM Cost_Centers WHERE CC_Code=PARENT_CODE INTO PARENT_CC;
		IF X_CC = CC_TOP OR X_CC=PARENT_CC THEN
			SET IS_BELOW = TRUE;
		ELSE
			IF PARENT_CC > 1 THEN
				CALL CC_Is_Below(PARENT_CC,CC_TOP,IS_BELOW);
			END IF;
        END IF; 
    END IF;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function ccisbelow
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`ccisbelow`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION ccisbelow(CC INT,TOP INT) RETURNS BOOLEAN DETERMINISTIC
BEGIN
    DECLARE IS_BELOW BOOLEAN;
    CALL CC_Is_Below(CC, TOP, IS_BELOW);
    RETURN IS_BELOW;
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Update_Charge_Resume_CI2
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Update_Charge_Resume_CI2`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Update_Charge_Resume_CI2` (XDATE_FROM DATE,XDATE_TO DATE,XCIT_STATUS INT,XCUR_CODE VARCHAR(3),XCI_ID INT)
BEGIN
	START TRANSACTION;
	DELETE
		FROM 	Charge_Resumes
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE;
	COMMIT;
    START TRANSACTION;
	INSERT
		INTO	Charge_Resumes
			(	Cus_Id,
				CR_Date_From,
                CR_Date_To,
                CIT_Status,
                Cur_Code,
                CIT_Count,
                CIT_Quantity,
                CIT_Generation,
                CU_Id,
                CI_CC_Id,
                CU_Operation,
                Typ_Code,
                CC_Cur_Code,
                CI_Id,
                Rat_Id,
                Rat_Price,
                Rat_MU_Code,
                Rat_Cur_Code,
                Rat_Period,
                Rat_Hourly,
                Rat_Daily,
                Rat_Monthly,
                CR_Quantity,
                CR_Quantity_at_Rate,
                CC_XR,
                CR_Cur_XR,
                CR_ST_at_Rate_Cur,
                CR_ST_at_CC_Cur,
                CR_ST_at_Cur,
                Cus_Name,
                CC_Description,
                CI_Name,
                CU_Description,
                Rat_Period_Description,
                Pla_Id
			)
	SELECT 
        CI.CUS_ID 			AS CUS_ID,
		XDATE_FROM			AS DATE_FROM,
        XDATE_TO			AS DATE_TO,
        XCIT_STATUS			AS CIT_STATUS,
        XCUR_CODE			AS CUR_CODE,
		COUNT(*) 			AS CIT_COUNT,
        sum(CIT_Quantity) 	AS CIT_QUANTITY,
        CU.CIT_Generation 	AS CIT_GENERATION,
        CIT.CU_Id 			AS CU_ID,
        CI.CC_Id 			AS CI_CC_ID,
        CU.CU_Operation		AS CU_OPERATION,
        CU.Typ_Code			AS TYP_CODE,
        CC.Cur_Code			AS CC_CUR_CODE,
		XCI_ID 				AS CI_ID,
        CU.Rat_Id 			AS RAT_ID,
		RAT.Rat_Price		AS RAT_PRICE,
        RAT.MU_Code			AS RAT_MU_CODE,
        RAT.Cur_Code		AS RAT_CUR_CODE,
        RAT.Rat_Period		AS RAT_PERIOD,
        0					AS RAT_HOURLY,
        0					AS RAT_DAILY,
        0					AS RAT_MONTHLY,
        0					AS CR_QUANTITY,
        0					AS CR_QUANTITY_AT_RATE,
        1					AS CC_XR,
        1					AS CR_CUR_XR,
        0					AS ST_AT_RATE_CUR,
        0					AS ST_AT_CC_CUR,
        0					AS ST_AT_CUR,
        CUS.Cus_Name		AS CUS_NAME,
        CC.CC_Description	AS CC_DESCRIPTION,
        CI.CI_Name			AS CI_NAME,
        CU.CU_Description	AS CU_DESCRIPTION,
        IF(Rat_Period=1,"HOUR",IF(Rat_Period=2,"DAY",IF(RAT_Period=3,"MONTH","ERROR")))
							AS RAT_PERIOD_DESCRIPTION,
		CI.Pla_Id			AS PLA_ID
		FROM Charge_Items 				AS CIT
			JOIN Charge_Units 			AS CU 	USING (CU_Id)
			JOIN Configuration_Items 	AS CI 	USING (CI_Id)
            JOIN Cost_Centers			AS CC	ON 	  (CC.CC_Id=CI.CC_Id)
			JOIN Customers 				AS CUS 	USING (Cus_Id)
			JOIN Rates 					AS RAT 	USING (Rat_Id)
		WHERE 	CIT_Status  =  XCIT_STATUS
			AND CIT_Date   >= XDATE_FROM
			AND CIT_Date   <= XDATE_TO
            AND CU.CI_Id    =  XCI_ID
		GROUP BY CIT.CU_Id
        ORDER BY CUS_ID,CI.CC_Id,CI.CI_Id,CIT.CU_Id
        ;
	COMMIT;
    START TRANSACTION;
	UPDATE Charge_Resumes
		SET CR_ST_at_Rate_Cur   =  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)),
			CR_ST_at_CC_Cur     =  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)) * CC_XR,
			CR_ST_at_Cur      	=  CR_Quantity * IF(Rat_Period=1,Rat_Hourly,IF(Rat_Period=2,Rat_Daily,Rat_Monthly)) * CR_Cur_XR
		WHERE	CI_Id 			= XCI_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE;
	UPDATE Charge_Resumes
		SET CR_Quantity=IF(CU_Operation="NONE",CIT_Quantity,Convert_Unit(CIT_Quantity,CU_Operation))
		WHERE	CI_Id 			= XCI_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE;
	UPDATE Charge_Resumes
		SET CR_Quantity_at_Rate = IF(CIT_Generation=1,CR_Quantity/IF(Rat_Period=3,720,IF(Rat_Period=2,24,1)),CR_Quantity)
		WHERE	CI_Id 			= XCI_ID
			AND CR_Date_From   	= XDATE_FROM
			AND CR_Date_To   	= XDATE_TO
			AND CIT_Status 		= XCIT_STATUS
			AND Cur_Code 		= XCUR_CODE;
	UPDATE Charge_Resumes
		SET CC_XR = Get_Exchange_Rate(Rat_Cur_Code,CC_Cur_Code,CR_Date_To)
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE;
	UPDATE Charge_Resumes
		SET CR_Cur_XR = Get_Exchange_Rate(Rat_Cur_Code,Cur_Code,CR_Date_To)
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE
			AND Cur_Code 		!= Rat_Cur_Code;            
	UPDATE Charge_Resumes
		#SET CR_ST_at_Rate_Cur   =  CR_Quantity * Rat_Hourly,
		#	CR_ST_at_CC_Cur     =  CR_Quantity * Rat_Hourly * CC_XR,
		#	CR_ST_at_Cur      	=  CR_Quantity * Rat_Hourly * CR_Cur_XR
		SET CR_ST_at_Rate_Cur   =  CR_Quantity_at_Rate * Rat_Price,
			CR_ST_at_CC_Cur     =  CR_Quantity_at_Rate * Rat_Price * CC_XR,
			CR_ST_at_Cur      	=  CR_Quantity_at_Rate * Rat_Price * CR_Cur_XR
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE;
	COMMIT;
    SELECT COUNT(*) AS RECORDS FROM Charge_Resumes
    #SELECT * FROM Charge_Resumes
		WHERE	CI_Id 			=  XCI_ID
			AND CR_Date_From   	=  XDATE_FROM
			AND CR_Date_To   	=  XDATE_TO
			AND CIT_Status 		=  XCIT_STATUS
			AND Cur_Code 		=  XCUR_CODE;

END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Get_Charge_Resume2
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Get_Charge_Resume2`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Get_Charge_Resume2` (FILTER INT,CODE INT,DFROM DATE,DTO DATE,STATUS INT,CUR VARCHAR(3))
BEGIN
	IF (FILTER = 1)
		THEN
			SELECT * FROM 	Charge_Resumes
				WHERE	Cus_Id 			=  CODE
				AND CR_Date_From   	=  DFROM
				AND CR_Date_To   	=  DTO
				AND CIT_Status 		=  STATUS
				AND Cur_Code 		=  CUR
			ORDER BY	Cus_Id,CI_CC_Id,CI_Id;
	ELSEIF (FILTER = 2)
		THEN
			SELECT * FROM 	Charge_Resumes
				WHERE	CI_CC_Id IN (SELECT CC_Id FROM Cost_Centers WHERE ccisbelow(CC_ID,CODE))
				AND CR_Date_From   	=  DFROM
				AND CR_Date_To   	=  DTO
				AND CIT_Status 		=  STATUS
				AND Cur_Code 		=  CUR
			ORDER BY	Cus_Id,CI_CC_Id,CI_Id;        
	ELSEIF (FILTER = 3)
		THEN
			SELECT * FROM 	Charge_Resumes
				WHERE	Pla_Id 			=  CODE
				AND CR_Date_From   	=  DFROM
				AND CR_Date_To   	=  DTO
				AND CIT_Status 		=  STATUS
				AND Cur_Code 		=  CUR
			ORDER BY	Pla_Id,Cus_Id,CI_CC_Id,CI_Id;        
	ELSEIF (FILTER = 4)
		THEN
			SELECT * FROM 	Charge_Resumes
				WHERE CR_Date_From   	=  DFROM
				AND CR_Date_To   	=  DTO
				AND CIT_Status 		=  STATUS
				AND Cur_Code 		=  CUR
			ORDER BY	Pla_Id,Cus_Id,CI_CC_Id,CI_Id;        
    END IF;    
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- procedure Record_Item_1
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Record_Item_1`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Record_Item_1` (CU_TYPE VARCHAR(10),CI_UUID VARCHAR(45),CU_UUID VARCHAR(45),QUANTITY DECIMAL(20,6) ,X_DATE_TIME DATETIME,X_ACTIVE BOOLEAN)
BEGIN
	DECLARE _CI_ID		INT;
	DECLARE _CU_ID		INT;
	DECLARE _Q	 		DECIMAL(20,6);
	DECLARE X_SLICE		DATETIME;
    DECLARE X_DATE		DATE;
    DECLARE X_TIME		TIME;
    
    #SET X_DATE_TIME = CONCAT(X_DATE," ",X_TIME);
    SET X_SLICE = Get_DateTime_Slice(X_DATE_TIME);
    SET X_DATE=DATE(X_SLICE);
    SET X_TIME=TIME(X_SLICE);
    
	SET QUANTITY    = ROUND(QUANTITY,6);
    
    # Needs to be sure that recursion is possible
    SET @@max_sp_recursion_depth = 8;
    
    # Verifies if CI_UUID Corresponds to a valid Configuration Item
    
    SET _CI_ID = Get_CI_Id_From_UUID(CI_UUID);
    
    IF _CI_ID IS NOT NULL THEN
		# Gets Configuration Unit Id from raw DataType of CU and UUID for CI and CU
		SET _CU_ID = Get_CU_Id_From_Data(CI_UUID,CU_UUID,CU_TYPE);

        # Checks if a valid CU Id was found
		IF _CU_ID IS NOT NULL THEN
			# Creates an Item billing record for the valud Charge Unit
            # ----------------------------------------------------------------------------
            #SELECT CIT_Quantity FROM Charge_Items WHERE CU_Id=_CU_ID AND CIT_Date=X_DATE AND CIT_Time=X_TIME LIMIT 1 INTO _Q;
            SELECT CIT_Quantity FROM Charge_Items WHERE CU_Id=_CU_ID AND CIT_DateTime=X_SLICE LIMIT 1 INTO _Q;

            IF _Q IS NULL THEN
				START TRANSACTION;
				#INSERT IGNORE INTO Charge_Items VALUES(_CU_ID,X_DATE,X_TIME,ROUND(QUANTITY,6),1,X_ACTIVE,X_DATE_TIME); # STATUS = 1 Created, Pending Approval
				INSERT IGNORE INTO Charge_Items
					(CU_Id,CIT_Quantity,CIT_Status,CIT_Is_Active,CIT_DateTime,CIT_Date,CIT_Time)
					VALUES(_CU_ID,ROUND(QUANTITY,6),1,X_ACTIVE,X_SLICE,X_DATE,X_TIME); # STATUS = 1 Created, Pending Approval
				COMMIT;
			ELSE 
				IF QUANTITY > _Q THEN
					START TRANSACTION;
					#UPDATE Charge_Items SET CIT_QUANTITY = ROUND(QUANTITY,6) WHERE CU_Id=_CU_ID AND CIT_Date=X_DATE AND CIT_Time=X_TIME; # STATUS = 1 Created, Pending Approval
					UPDATE Charge_Items SET CIT_QUANTITY = ROUND(QUANTITY,6)
						WHERE CU_Id=_CU_ID AND CIT_DateTime=X_SLICE; # STATUS = 1 Created, Pending Approval
                    COMMIT;
                END IF;
            END IF;
            # ----------------------------------------------------------------------------
		ELSE 
			# Tries to complete DB Integrity by creating a Dummy Charge Unit
			CALL Create_Charge_Unit(_CI_ID,NULL, CU_UUID,1,1,QUANTITY,NULL,CU_TYPE,NULL,NULL,NULL,NULL); # 1 = Is Billeable
            SET _CU_ID =  Get_CU_Id_From_Data(CI_UUID,CU_UUID,CU_TYPE);
            IF _CU_ID IS NOT NULL THEN
				#CALL Record_Item (CU_TYPE,CI_UUID,CU_UUID,QUANTITY,X_DATE,X_TIME,X_ACTIVE); # Recursive Call
				CALL Record_Item_1 (CU_TYPE,CI_UUID,CU_UUID,QUANTITY,X_SLICE,X_ACTIVE); # Recursive Call
            END IF;
		END IF;
	ELSE
		# Tries to complete DB Integrity by creating a Dummy Configuration Item
		CALL Create_Configuration_Item(NULL,CI_UUID,1,1,1);
        # Validates if a valid Configuration Item was created 
		SET _CI_ID = Get_CI_Id_From_UUID(CI_UUID);
		IF _CI_ID IS NOT NULL THEN
       		#call Tracer("P8 Llamada recursiva por CI recreado");		# Checks if a valid CU Id was found
			#CALL Record_Item (CU_TYPE,CI_UUID,CU_UUID,QUANTITY,X_DATE,X_TIME,X_ACTIVE); # Recursive Call
			CALL Record_Item_1 (CU_TYPE,CI_UUID,CU_UUID,QUANTITY,X_SLICE,X_ACTIVE); # Recursive Call
        END IF;
	END IF;
 
END$$

DELIMITER ;
SHOW WARNINGS;

-- -----------------------------------------------------
-- function Get_DateTime_Slice
-- -----------------------------------------------------

USE `collector`;
DROP function IF EXISTS `collector`.`Get_DateTime_Slice`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE FUNCTION `Get_DateTime_Slice` (XDATETIME DATETIME) RETURNS DATETIME DETERMINISTIC
BEGIN
	RETURN STR_TO_DATE(CONCAT(DATE(XDATETIME),' ',HOUR(XDATETIME)),"%Y-%m-%d %H");
END$$

DELIMITER ;
SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `collector`.`Platforms`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (1, 'Platform', 'localhost', '80', 'user', 'password');
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (0, 'Laboratorio Sertechno', '192.168.30.128', '9440', 'gvalera', 'gvalera123');
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (0, 'DC Demo : ENJ', '172.26.200.210', '9440', 'test', 'Pass1010.,');
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (0, 'DC Demo : NTX_ING_DCC', '0.0.0.0', '9440', 'user', 'password');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Currencies`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('UF', 'UNIDAD DE FOMENTO', 0, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('AFN', 'Afghani', 971, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ALL', 'Lek', 8, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('DZD', 'Algerian Dinar', 12, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('USD', 'US Dollar', 840, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('AOA', 'Kwanza', 973, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('XCD', 'East Caribbean Dollar', 951, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ARS', 'Argentine Peso', 32, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('AMD', 'Armenian Dram', 51, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('AWG', 'Aruban Guilder', 533, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('AUD', 'Australian Dollar', 36, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('AZN', 'Azerbaijan Manat', 31, 'Beginning January 2006, 1 new Manat (AZN) = 5000 old Manats (AZM).');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BSD', 'Bahamian Dollar', 44, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BHD', 'Bahraini Dinar', 48, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BDT', 'Taka', 50, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BBD', 'Barbados Dollar', 52, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BYR', 'Belarusian Ruble', 974, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BZD', 'Belize Dollar', 84, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('XOF', 'CFA Franc BCEAO', 952, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BMD', 'Bermudian Dollar', 60, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BTN', 'Ngultrum', 64, 'Indian Rupee (INR 356)');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BOB', 'Boliviano', 68, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BAM', 'Convertible Mark', 977, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BWP', 'Pula', 72, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BRL', 'Brazilian Real', 986, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BND', 'Brunei Dollar', 96, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BGN', 'Bulgarian Lev', 975, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('BIF', 'Burundi Franc', 108, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KHR', 'Riel (The US dollar is the de facto currency)', 116, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('XAF', 'CFA Franc BEAC', 950, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CAD', 'Canadian Dollar', 124, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CVE', 'Cape Verde Escudo', 132, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KYD', 'Cayman Islands Dollar', 136, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CLP', 'Chilean Peso', 152, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CNY', 'Renminbi (Yuan)', 156, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('COP', 'Colombian Peso', 170, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KMF', 'Comoro Franc', 174, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CDF', 'Franc Congolais', 976, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('NZD', 'New Zealand Dollar', 554, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CRC', 'Costa Rican Colon', 188, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('HRK', 'Croatian Kuna', 191, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CUP', 'Cuban Peso', 192, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CZK', 'Czech Koruna', 203, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('DKK', 'Danish Krone', 208, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('DJF', 'Djibouti Franc', 262, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('DOP', 'Dominican Peso', 214, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('EGP', 'Egyptian Pound', 818, NULL);
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ERN', 'Nakfa', 232, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('EEK', 'Euro replaced Estonian Kroon in 2011.', 233, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ETB', 'Ethiopian Birr', 230, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('FKP', 'Falkland Islands Pound', 238, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('FJD', 'Fiji Dollar', 242, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('XPF', 'CFP Franc', 953, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GMD', 'Dalasi', 270, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GEL', 'Lari', 981, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GHC', 'Cedi', 288, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GIP', 'Gibraltar Pound', 292, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GTQ', 'Quetzal', 320, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GNF', 'Guinea Franc', 324, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GWP', 'Guinea-Bissau Peso', 624, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GYD', 'Guyana Dollar', 328, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('HTG', 'Haitian Gourde', 332, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('HNL', 'Lempira', 340, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('HKD', 'Hong Kong Dollar', 344, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('HUF', 'Forint', 348, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ISK', 'Iceland Krona', 352, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('INR', 'Indian Rupee', 356, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('IDR', 'Rupiah', 360, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('IRR', 'Iranian Rial', 364, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('IQD', 'Iraqi Dinar', 368, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ILS', 'New Israeli Sheqel', 376, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('JMD', 'Jamaican Dollar', 388, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('JPY', 'Yen', 392, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('JOD', 'Jordanian Dinar', 400, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KZT', 'Tenge', 398, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KES', 'Kenyan Shilling', 404, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KPW', 'North Korean Won', 408, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KRW', 'Won', 410, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KWD', 'Kuwaiti Dinar', 414, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('KGS', 'Som', 417, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('LAK', 'Kip', 418, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('LBP', 'Lebanese Pound', 422, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('LSL', 'Loti', 426, ' (plural Maloti). It is equivalent to the South African Rand.');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('LRD', 'Liberian Dollar', 430, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('LYD', 'Lybian Dinar', 434, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CHF', 'Swiss Franc', 756, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('LTL', 'Euro replaced Lithuanian Litas', 440, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MOP', 'Macanese Pataca', 446, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MKD', 'Macedonian Denar', 807, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MGF', 'Malagasy Franc', 450, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MWK', 'Kwacha', 454, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MYR', 'Malaysian Ringgit', 458, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MVR', 'Rufiyaa', 462, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MTL', 'Maltese Lira', 470, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MRO', 'Ouguiya', 478, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MUR', 'Mauritius Rupee', 480, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('EUR', 'Euro', 978, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MXN', 'Mexican Peso', 484, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MXV', 'Mexican Unidad de Inversion (UDI)', 979, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MDL', 'Moldovan Leu', 498, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MNT', 'Tugrik (Tugrug)', 496, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MAD', 'Moroccan Dirham', 504, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MZM', 'Metical', 508, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('MMK', 'Kyat', 104, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ZAR', 'Rand', 710, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('NAD', 'Namibia Dollar', 516, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('NPR', 'Nepalese Rupee', 524, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ANG', 'Netherlands Antillan Guilder', 532, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('NIO', 'Cordoba Oro', 558, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('NGN', 'Naira', 566, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('NOK', 'Norwegian Krone', 578, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('OMR', 'Rial Omani', 512, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('PKR', 'Pakistan Rupee', 586, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('PAB', 'Balboa', 590, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('PGK', 'Kina', 598, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('PYG', 'Guarani', 600, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('PEN', 'Nuevo Sol', 604, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('PHP', 'Philippine Peso', 608, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('PLN', 'Zloty', 985, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('QAR', 'Qatari Rial', 634, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ROL', 'Leu', 642, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('RUR', 'Russian Ruble', 810, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('RUB', 'Russian Ruble', 643, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('RWF', 'Rwanda Franc', 646, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SHP', 'Saint Helena Pound', 654, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('WST', 'Tala', 882, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('STD', 'Dobra', 678, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SAR', 'Saudi Riyal', 682, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('CSD', 'Serbian Dinar', 891, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SCR', 'Seychelles Rupee', 690, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SLL', 'Leone', 694, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SGD', 'Singapore Dollar', 702, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SBD', 'Solomon Islands Dollar', 90, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SOS', 'Somali Shilling', 706, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SSP', 'South Sudanese pound', 728, 'since 18. July 2011');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('LKR', 'Sri Lanka Rupee', 144, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SDD', 'Sudanese Dinar [obsolete]', 736, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SDG', 'Sudanese Pound', 938, 'since 10. Jan. 2007');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SRG', 'Suriname Guilder', 740, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SZL', 'Lilangeni', 748, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SEK', 'Swedish Krona', 752, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('SYP', 'Syrian Pound', 760, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('TWD', 'New Taiwan Dollar', 901, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('TJS', 'Somoni', 972, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('TZS', 'Tanzanian Shilling', 834, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('THB', 'Thai Baht', 764, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('TOP', 'Pa?anga', 776, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('TTD', 'Trinidad and Tobago Dollar', 780, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('TND', 'Tunisian Dinar', 788, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('TRY', 'Yeni Turk Liras (YTL)', 949, 'on 1 January 2005 New Turkish Lira replaced Turkish Lira (TRL)');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('TMM', 'Manat', 795, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('UGX', 'Uganda Shilling', 800, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('UAH', 'Hryvnia', 980, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('AED', 'UAE Dirham', 784, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('GBP', 'Pound Sterling', 826, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('USS', 'US Dollar r (Same day)', 998, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('USN', 'US Dollar r (Next day)', 997, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('UYU', 'Peso Uruguayo', 858, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('UZS', 'Uzbekistan Sum', 860, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('VUV', 'Vatu', 548, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('VEF', 'Venezuelan Bolivar ', 937, 'replaced at 1 bolivar fuerte for 1000 old bolivares)(VEB 862)(Bolivar fuerte venezolano) (since 1 January 2008,');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('VND', 'Vietnamese Dong', 704, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('YER', 'Yemeni Rial', 886, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ZMK', 'Kwacha', 894, '');
INSERT INTO `collector`.`Currencies` (`Cur_Code`, `Cur_Name`, `Cur_Id`, `Cur_Comment`) VALUES ('ZWD', 'Zimbabwe Dollar', 716, '');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Cost_Centers`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`, `CC_Parent_Code`) VALUES (1, 'DEFAULT-CC-CODE', 'DEFAULT_CC_DESCRIPTION', 'USD', '1');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Customers`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (1, 'DEFAULT', 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Configuration_Items`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `Cus_Id`, `CI_Commissioning_DateTime`, `CI_Decommissioning_DateTime`) VALUES (1, '', '', 1, 1, 1, NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`CU_Types`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('NUL', '');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('CLU', 'Cluster');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('NOD', 'Node');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('VM', 'Virtual Machine');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('CPU', 'CPU Unit');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('RAM', 'RAM Unit');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('DSK', 'Virtual Disk Drive');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('CDR', 'Virtual CDROM');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('VGA', 'VGA Console');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('COR', 'Cores per CPU');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('HOU', 'Housing');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('HOS', 'Hosting');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('NIC', 'Network Interface Card');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('W10', 'Windows 10 OS');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('LNX', 'Linux OS');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('MYS', 'MySQL Instance');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('ORA', 'Oracle Instance');
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('MSS', 'MS SQL Server Instance');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`CU_Operations`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('NONE', 'No Conversion', 1, 1);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('BTOKB', 'Byte to KB', 0, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('BTOMB', 'Byte to MB', 0, 1048576);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('BTOGB', 'Byte to GB', 0, 1073741824);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('KBTOB', 'Kilobyte to Byte', 1, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('KBTOMG', 'Kilobyte to MB', 0, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('KBTOGB', 'Kilobyte to GB', 0, 1048576);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MBTOB', 'Megabyte to Byte', 1, 1048576);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MBTOKB', 'Megabyte to KB', 1, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MBTOGB', 'Megabyte to GB', 0, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('GBTOB', 'Gigabyte to Bytes', 0, 1073741824);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('GBTOKB', 'Gigabyte to KB', NULL, 1048576);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('GBTOMB', 'Gigabyte to MB', NULL, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('HTOD', 'Hours to Days', 0, 24);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('HTOM', 'Hours to Months', 0, 720);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('DTOH', 'Days to Hours', 1, 24);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('DTOM', 'Days to Months', 0, 30);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MTOH', 'Months to Hours', 1, 720);
INSERT INTO `collector`.`CU_Operations` (`CU_Operation`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MTOD', 'Months to Days', 1, 30);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`CIT_Generations`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`CIT_Generations` (`CIT_Generation`, `Value`) VALUES (1, 'Daemon');
INSERT INTO `collector`.`CIT_Generations` (`CIT_Generation`, `Value`) VALUES (2, 'Manual');
INSERT INTO `collector`.`CIT_Generations` (`CIT_Generation`, `Value`) VALUES (3, 'Monthly');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Charge_Units`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operation`, `Typ_Code`, `CIT_Generation`, `Rat_Id`, `CU_Reference_1`, `CU_Reference_2`, `CU_Reference_3`) VALUES (1, 1, 'CU DESCRIPTION', 'CU UUID', 1, 1, 0, 'NONE', 'NUL', 1, 1, NULL, NULL, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Measure_Units`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Measure_Units` (`MU_Code`, `MU_Description`) VALUES ('UNT', 'Unit');
INSERT INTO `collector`.`Measure_Units` (`MU_Code`, `MU_Description`) VALUES ('GB', 'GigaByte');
INSERT INTO `collector`.`Measure_Units` (`MU_Code`, `MU_Description`) VALUES ('TB', 'TeraByte');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Rat_Periods`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Rat_Periods` (`Rat_Period`, `Value`) VALUES (1, 'Hourly Rate');
INSERT INTO `collector`.`Rat_Periods` (`Rat_Period`, `Value`) VALUES (2, 'Dayly Rate');
INSERT INTO `collector`.`Rat_Periods` (`Rat_Period`, `Value`) VALUES (3, 'Monthly Rate');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Rates`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CI_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`, `Rat_Type`) VALUES (1, 'NUL', 1, 1, 1, 1, 0.0, 'USD', 'UNT', 1, 0);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CI_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`, `Rat_Type`) VALUES (14, 'VM', 1, 1, 1, 1, 10.000000, 'USD', 'UNT', 3, 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CI_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`, `Rat_Type`) VALUES (15, 'RAM', 1, 1, 1, 1, 5.000000, 'USD', 'GB', 3, 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CI_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`, `Rat_Type`) VALUES (16, 'COR', 1, 1, 1, 1, 1.000000, 'USD', 'UNT', 3, 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CI_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`, `Rat_Type`) VALUES (17, 'CPU', 1, 1, 1, 1, 0.000000, 'USD', 'UNT', 3, 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CI_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`, `Rat_Type`) VALUES (18, 'DSK', 1, 1, 1, 1, 1.000000, 'USD', 'GB', 3, 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CI_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`, `Rat_Type`) VALUES (19, 'NIC', 1, 1, 1, 1, 0.500000, 'USD', 'UNT', 3, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Dev_Forms`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (79, 'Charge_Items', 'CU_Id', 'int(11)', 'NO', 'PRI', '0', '', 'CU_Id', 'Charge_Units', 'CU_Id', 'CU_Description', 11, 1, 'PK', 'Required()', 'Charge Unit Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (80, 'Charge_Items', 'CIT_Date', 'date', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 10, 1, 'PK', 'Required()', 'Date', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (81, 'Charge_Items', 'CIT_Time', 'time', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 8, 1, 'PK', 'Required()', 'Time', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (82, 'Charge_Items', 'CIT_Quantity', 'decimal(20,6)', 'NO', '', '0.000000', '', 'NULL', 'NULL', 'NULL', 'NULL', 20, 1, 'NULL', 'Required()', 'Quantity', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (83, 'Charge_Items', 'CIT_Status', 'int(11)', 'NO', 'MUL', '0', '', 'CIT_Status', 'CIT_Statuses', 'CIT_Status', 'Value', 45, 1, 'FK', 'Required()', 'Status', 5, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (84, 'Charge_Items', 'CIT_Is_Active', 'tinyint(4)', 'YES', '', '0', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Is Active', 6, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (85, 'Charge_Items', 'CIT_DateTime', 'datetime', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'CIT_DateTime', 7, 'NULL', 0, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (86, 'Charge_Units', 'CU_Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (87, 'Charge_Units', 'CI_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'CI_Id', 'Configuration_Items', 'CI_Id', 'CI_Name', 11, 1, 'FK', 'Required()', 'Configuration Item Id', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (88, 'Charge_Units', 'CU_Description', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Description', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (89, 'Charge_Units', 'CU_UUID', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'UUID', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (90, 'Charge_Units', 'CU_Is_Billeable', 'tinyint(4)', 'YES', '', '0', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Is Billeable', 5, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (91, 'Charge_Units', 'CU_Is_Always_Billeable', 'tinyint(4)', 'YES', '', '0', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Is Always Billeable', 6, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (92, 'Charge_Units', 'CU_Quantity', 'decimal(20,6)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 20, 1, 'NULL', 'Required()', 'Quantity', 7, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (93, 'Charge_Units', 'CU_Operation', 'varchar(10)', 'NO', 'MUL', 'NULL', '', 'CU_Operation', 'CU_Operations', 'CU_Operation', 'Value', 45, 1, 'FK', 'Required()', 'Conversion Operation', 8, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (94, 'Charge_Units', 'Typ_Code', 'varchar(10)', 'NO', 'MUL', 'NULL', '', 'Typ_Code', 'CU_Types', 'Typ_Code', 'Typ_Description', 10, 1, 'FK', 'Required()', 'Type', 9, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (95, 'Charge_Units', 'CC_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'CC_Id', 'Cost_Centers', 'CC_Id', 'CC_Description', 11, 1, 'FK', 'Required()', 'Cost Center Id', 10, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (96, 'Charge_Units', 'CIT_Generation', 'int(11)', 'NO', 'MUL', 'NULL', '', 'CIT_Generation', 'CIT_Generations', 'CIT_Generation', 'Value', 45, 1, 'FK', 'Required()', 'Item Generation Type', 11, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (97, 'Charge_Units', 'Rat_Id', 'int(11)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 11, NULL, 'NULL', 'NULL', 'Rate Id', 12, 'NULL', 0, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (98, 'Charge_Units', 'CU_Reference_1', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Reference 1', 13, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (99, 'Charge_Units', 'CU_Reference_2', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Reference 2', 14, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (100, 'Charge_Units', 'CU_Reference_3', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Reference 3', 15, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (101, 'CIT_Generations', 'CIT_Generation', 'int(11)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'CIT_Generation', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (102, 'CIT_Generations', 'Value', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Value', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (103, 'CIT_Statuses', 'CIT_Status', 'int(11)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'CIT Status', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (104, 'CIT_Statuses', 'Value', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Vallue', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (105, 'Configuration_Items', 'CI_Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (106, 'Configuration_Items', 'CI_Name', 'varchar(45)', 'NO', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Name', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (107, 'Configuration_Items', 'CI_UUID', 'varchar(45)', 'NO', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'UUID', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (108, 'Configuration_Items', 'Pla_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'Pla_Id', 'Platforms', 'Pla_Id', 'Pla_Name', 11, 1, 'FK', 'Required()', 'Platform Id', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (109, 'Configuration_Items', 'CC_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'CC_Id', 'Cost_Centers', 'CC_Id', 'CC_Description', 11, 1, 'FK', 'Required()', 'Cost Center Id', 5, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (110, 'Configuration_Items', 'Cus_Id', 'int(11)', 'NO', 'MUL', '1', '', 'Cus_Id', 'Customers', 'Cus_Id', 'Cus_Name', 11, 1, 'FK', 'Required()', 'Customer Id', 6, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (111, 'Configuration_Items', 'CI_Commissioning_DateTime', 'datetime', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'CI_Commissioning_DateTime', 7, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (112, 'Configuration_Items', 'CI_Decommissioning_DateTime', 'datetime', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'CI_Decommissioning_DateTime', 8, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (113, 'Cost_Centers', 'CC_Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Cost Center Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (114, 'Cost_Centers', 'CC_Code', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Code', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (115, 'Cost_Centers', 'CC_Description', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Description', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (116, 'Cost_Centers', 'Cur_Code', 'varchar(3)', 'NO', 'MUL', 'NULL', '', 'Cur_Code', 'Currencies', 'Cur_Code', 'Cur_Name', 3, 1, 'FK', 'Required()', 'Currency Code', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (118, 'Countries', 'Cou_Code', 'varchar(2)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 2, 1, 'PK', 'Required()', 'Code', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (119, 'Countries', 'Cou_Name', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Name', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (120, 'Countries', 'Cou_A3', 'varchar(3)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 3, NULL, 'NULL', 'NULL', 'Alphanum Code', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (121, 'Countries', 'Cou_N', 'int(11)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 11, NULL, 'NULL', 'NULL', 'ISO Numeric Code', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (122, 'Countries_Currencies', 'Cou_Code', 'varchar(2)', 'NO', 'PRI', 'NULL', '', 'Cou_Code', 'Countries', 'Cou_Code', 'Cou_Name', 2, 1, 'PK', 'Required()', 'Country Code', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (123, 'Countries_Currencies', 'Cur_Code', 'varchar(3)', 'NO', 'PRI', 'NULL', '', 'Cur_Code', 'Currencies', 'Cur_Code', 'Cur_Name', 3, 1, 'PK', 'Required()', 'Currency Code', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (124, 'Countries_Currencies', 'Cou_Cur_Comment', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Comment', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (125, 'CU_Operations', 'CU_Operation', 'varchar(10)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 10, 1, 'PK', 'Required()', 'Operation', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (126, 'CU_Operations', 'Value', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Value', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (127, 'CU_Operations', 'Is_Multiply', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Is Multiply', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (128, 'CU_Operations', 'Factor', 'int(11)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 11, NULL, 'NULL', 'NULL', 'Factor', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (129, 'CU_Types', 'Typ_Code', 'varchar(10)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 10, 1, 'PK', 'Required()', 'Type', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (130, 'CU_Types', 'Typ_Description', 'varchar(45)', 'NO', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Description', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (131, 'Currencies', 'Cur_Code', 'varchar(3)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 3, 1, 'PK', 'Required()', 'Code', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (132, 'Currencies', 'Cur_Name', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Name', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (133, 'Currencies', 'Cur_Id', 'int(11)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 11, NULL, 'NULL', 'NULL', 'Id', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (134, 'Currencies', 'Cur_Comment', 'varchar(128)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 128, NULL, 'NULL', 'NULL', 'Comment', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (135, 'Customers', 'Cus_Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (136, 'Customers', 'Cus_Name', 'varchar(45)', 'NO', 'UNI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Name', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (137, 'Customers', 'CC_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'CC_Id', 'Cost_Centers', 'CC_Id', 'CC_Description', 11, 1, 'FK', 'Required()', 'Cost Center Id', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (138, 'Dev_Forms', 'Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (139, 'Dev_Forms', 'Table', 'varchar(45)', 'NO', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Table', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (140, 'Dev_Forms', 'Field', 'varchar(45)', 'NO', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Field', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (141, 'Dev_Forms', 'Type', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Type', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (142, 'Dev_Forms', 'Null', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Null', 5, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (143, 'Dev_Forms', 'Key', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Key', 6, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (144, 'Dev_Forms', 'Default', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Default', 7, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (145, 'Dev_Forms', 'Extra', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Extra', 8, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (146, 'Dev_Forms', 'Foreign_Key', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Foreign Key', 9, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (147, 'Dev_Forms', 'Referenced_Table', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Referenced Table', 10, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (148, 'Dev_Forms', 'Foreign_Field', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Foreign Field', 11, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (149, 'Dev_Forms', 'Foreign_Value', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'Foreign_Value', 12, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (150, 'Dev_Forms', 'Length', 'int(11)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 11, NULL, 'NULL', 'NULL', 'Length', 13, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (151, 'Dev_Forms', 'Validation', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Validation', 14, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (152, 'Dev_Forms', 'Validation_Type', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Validation Type', 15, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (153, 'Dev_Forms', 'Validation_String', 'varchar(128)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 128, NULL, 'NULL', 'NULL', 'Validation String', 16, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (154, 'Dev_Forms', 'Caption_String', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Caption String', 17, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (155, 'Dev_Forms', 'Field_Order', 'int(11)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'Field Order', 18, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (156, 'Dev_Forms', 'Field_Format', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'Field Format', 19, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (157, 'Dev_Forms', 'Form_Editable', 'tinyint(4)', 'YES', '', '1', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'Form Editable', 20, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (158, 'Dev_Tables', 'Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (159, 'Dev_Tables', 'Name', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Name', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (160, 'Dev_Tables', 'Caption', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Caption', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (161, 'Dev_Tables', 'Entity', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Entity', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (162, 'Dev_Tables', 'Class_Name', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Class Name', 5, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (163, 'Dev_Tables', 'Child_Table', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Child Table', 6, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (164, 'Dev_Tables', 'Parent_Table', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Parent Table', 7, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (165, 'Dev_Tables', 'Use_Pagination', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Use Pagination', 8, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (166, 'Dev_Tables', 'Use_Children_Pagination', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Use Children Pagination', 9, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (167, 'Dev_Tables', 'Generate_Form_One', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Generate Form One', 10, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (168, 'Dev_Tables', 'Generate_form_All', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Generate form All', 11, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (169, 'Dev_Tables', 'Generate_Form_Filter', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Generate Form Filter', 12, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (170, 'Dev_Tables', 'Generate_Children', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Generate Children', 13, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (171, 'Dev_Tables', 'Generate_Foreign_Fields', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Generate Foreign Fields', 14, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (172, 'Dev_Tables', 'Permission_View', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Permission View', 15, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (173, 'Dev_Tables', 'Permission_Delete', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Permission Delete', 16, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (174, 'Dev_Tables', 'Permission_Modify', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Permission Modify', 17, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (175, 'Dev_Tables', 'Permission_Report', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Permission Report', 18, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (176, 'Dev_Tables', 'Permission_Export', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Permission Export', 19, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (177, 'Dev_Tables', 'Permission_View_Private', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Permission View Private', 20, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (178, 'Dev_Tables', 'Permission_Modify_Private', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Permission Modify Private', 21, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (179, 'Dev_Tables', 'Permission_Administer', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 4, NULL, 'NULL', 'NULL', 'Permission Administer', 22, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (180, 'Exchange_Rates', 'ER_Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (181, 'Exchange_Rates', 'Cur_Code', 'varchar(3)', 'NO', 'MUL', 'NULL', '', 'Cur_Code', 'Currencies', 'Cur_Code', 'Cur_Name', 3, 1, 'FK', 'Required()', 'Currency Code', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (182, 'Exchange_Rates', 'ER_Factor', 'decimal(20,6)', 'NO', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 20, 1, 'NULL', 'Required()', 'Factor', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (183, 'Exchange_Rates', 'ER_Date', 'date', 'NO', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 10, NULL, 'NULL', 'NULL', 'Date', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (184, 'Measure_Units', 'MU_Code', 'varchar(3)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 3, 1, 'PK', 'Required()', 'Code', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (185, 'Measure_Units', 'MU_Description', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Description', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (186, 'Platforms', 'Pla_Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (187, 'Platforms', 'Pla_Name', 'varchar(45)', 'NO', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Name', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (188, 'Platforms', 'Pla_Host', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Host', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (189, 'Platforms', 'Pla_Port', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Port', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (190, 'Platforms', 'Pla_User', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'User', 5, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (191, 'Platforms', 'Pla_Password', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Password', 6, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (192, 'Rat_Periods', 'Rat_Period', 'int(11)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Rate Period', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (193, 'Rat_Periods', 'Value', 'varchar(45)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 45, NULL, 'NULL', 'NULL', 'Value', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (194, 'Rates', 'Rat_Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (195, 'Rates', 'Typ_Code', 'varchar(10)', 'NO', 'MUL', 'NULL', '', 'Typ_Code', 'CU_Types', 'Typ_Code', 'Typ_Description', 10, 1, 'FK', 'Required()', 'Charge Unit Type', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (196, 'Rates', 'Cus_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'Cus_Id', 'Customers', 'Cus_Id', 'Cus_Name', 11, 1, 'FK', 'Required()', 'Customer Id', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (197, 'Rates', 'Pla_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'Pla_Id', 'Platforms', 'Pla_Id', 'Pla_Name', 11, 1, 'FK', 'Required()', 'Platform Id', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (198, 'Rates', 'CC_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'CC_Id', 'Cost_Centers', 'CC_Id', 'CC_Description', 11, 1, 'FK', 'Required()', 'Cost Center Id', 5, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (199, 'Rates', 'CI_Id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'CI_Id', 'Configuration_Items', 'CI_Id', 'CI_Name', 11, 1, 'FK', 'Required()', 'Configuration Item', 6, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (200, 'Rates', 'Rat_Price', 'decimal(20,6)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 20, 1, '', 'Required()', 'Rate Price', 7, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (201, 'Rates', 'Cur_Code', 'varchar(3)', 'NO', 'MUL', 'NULL', '', 'Cur_Code', 'Currencies', 'Cur_Code', 'Cur_Name', 3, 1, 'FK', 'Required()', 'Currency Code', 8, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (202, 'Rates', 'MU_Code', 'varchar(3)', 'NO', 'MUL', 'NULL', '', 'MU_Code', 'Measure_Units', 'MU_Code', 'MU_Description', 3, 1, 'FK', 'Required()', 'Measure Unit', 9, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (203, 'Rates', 'Rat_Period', 'int(11)', 'NO', 'MUL', 'NULL', '', 'Rat_Period', 'Rat_Periods', 'Rat_Period', 'Value', 11, 1, 'RF', 'Required()', 'Period', 10, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (204, 'Rates', 'Rat_Type', 'int(11)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'Rate Type', 11, 'NULL', 0, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (205, 'Roles', 'id', 'int(11)', 'NO', 'PRI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, 1, 'PK', 'Required()', 'id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (206, 'Roles', 'name', 'varchar(64)', 'YES', 'UNI', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'name', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (207, 'Roles', 'default', 'tinyint(4)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'default', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (208, 'Roles', 'permissions', 'int(11)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'permissions', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (209, 'Trace', 'ID', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', 11, 1, 'PK', 'Required()', 'ID', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (210, 'Trace', 'LINE', 'varchar(128)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', 128, NULL, 'NULL', 'NULL', 'LINE', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (211, 'Users', 'Id', 'int(11)', 'NO', 'PRI', 'NULL', 'auto_increment', 'NULL', 'NULL', 'NULL', 'NULL', NULL, 1, 'PK', 'Required()', 'Id', 1, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (212, 'Users', 'username', 'varchar(64)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'username', 2, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (213, 'Users', 'role_id', 'int(11)', 'NO', 'MUL', 'NULL', '', 'id', 'Roles', 'id', 'name', 11, 1, 'FK', 'Required()', 'role_id', 3, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (214, 'Users', 'email', 'varchar(64)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'email', 4, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (215, 'Users', 'password_hash', 'varchar(128)', 'YES', '', 'NULL', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'password_hash', 5, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (216, 'Users', 'confirmed', 'tinyint(4)', 'YES', '', '0', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'confirmed', 6, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (217, 'Users', 'CC_Id', 'int(11)', 'NO', 'MUL', '1', '', 'CC_Id', 'Cost_Centers', 'CC_Id', 'CC_Description', 11, 1, 'FK', 'Required()', 'CC_Id', 7, 'NULL', 1, NULL);
INSERT INTO `collector`.`Dev_Forms` (`Id`, `Table`, `Field`, `Type`, `Null`, `Key`, `Default`, `Extra`, `Foreign_Key`, `Referenced_Table`, `Foreign_Field`, `Foreign_Value`, `Length`, `Validation`, `Validation_Type`, `Validation_String`, `Caption_String`, `Field_Order`, `Field_Format`, `Form_Editable`, `ORM_Schema`) VALUES (218, 'Cost_Centers', 'CC_Parent_Code', 'varchar(45)', 'NO', '', '1', '', 'NULL', 'NULL', 'NULL', 'NULL', NULL, NULL, 'NULL', 'NULL', 'CC_Parent_Code', 5, 'NULL', 1, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`CIT_Statuses`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (1, 'Created, Pending Approval');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (2, 'Claimed');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (3, 'Rejected');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (4, 'Approved');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (5, 'Billed');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (6, 'Paid');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Exchange_Rates`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (1, 'USD', 1, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'USD', 1.3, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'USD', 0.001538, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'UF', 41.71, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'USD', 0.312500, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'USD', 0.001000, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'USD', 1.35, '2018-09-15');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'USD', 0.00151515, '2018-09-15');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Countries`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AF', 'Afghanistan', 'AFG', 4);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AX', 'Aland Islands', 'ALA', 248);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AL', 'Albania', 'ALB', 8);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('DZ', 'Algeria', 'DZA', 12);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AS', 'American Samoa', 'ASM', 16);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AD', 'Andorra', 'AND', 20);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AO', 'Angola', 'AGO', 24);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AI', 'Anguilla', 'AIA', 660);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AQ', 'Antarctica', 'ATA', 10);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AG', 'Antigua and Barbuda', 'ATG', 28);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AR', 'Argentina', 'ARG', 32);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AM', 'Armenia', 'ARM', 51);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AW', 'Aruba', 'ABW', 533);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AU', 'Australia', 'AUS', 36);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AT', 'Austria', 'AUT', 40);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AZ', 'Azerbaijan', 'AZE', 31);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BS', 'Bahamas', 'BHS', 44);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BH', 'Bahrain', 'BHR', 48);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BD', 'Bangladesh', 'BGD', 50);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BB', 'Barbados', 'BRB', 52);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BY', 'Belarus', 'BLR', 112);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BE', 'Belgium', 'BEL', 56);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BZ', 'Belize', 'BLZ', 84);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BJ', 'Benin', 'BEN', 204);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BM', 'Bermuda', 'BMU', 60);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BT', 'Bhutan', 'BTN', 64);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BO', 'Bolivia', 'BOL', 68);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BA', 'Bosnia and Herzegovina', 'BIH', 70);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BW', 'Botswana', 'BWA', 72);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BV', 'Bouvet Island', 'BVT', 74);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BR', 'Brazil', 'BRA', 76);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('VG', 'British Virgin Islands', 'VGB', 92);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IO', 'British Indian Ocean Territory', 'IOT', 86);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BN', 'Brunei Darussalam', 'BRN', 96);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BG', 'Bulgaria', 'BGR', 100);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BF', 'Burkina Faso', 'BFA', 854);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BI', 'Burundi', 'BDI', 108);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KH', 'Cambodia', 'KHM', 116);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CM', 'Cameroon', 'CMR', 120);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CA', 'Canada', 'CAN', 124);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CV', 'Cape Verde', 'CPV', 132);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KY', 'Cayman Islands', 'CYM', 136);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CF', 'Central African Republic', 'CAF', 140);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TD', 'Chad', 'TCD', 148);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CL', 'Chile', 'CHL', 152);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CN', 'China', 'CHN', 156);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('HK', 'Hong Kong', 'HKG', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MO', 'Macao', 'MAC', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CX', 'Christmas Island', 'CXR', 162);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CC', 'Cocos (Keeling) Islands', 'CCK', 166);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CO', 'Colombia', 'COL', 170);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KM', 'Comoros', 'COM', 174);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CG', 'Congo (Brazzaville)', 'COG', 178);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CD', 'Congo', 'COD', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CK', 'Cook Islands', 'COK', 184);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CR', 'Costa Rica', 'CRI', 188);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CI', 'Cote d\'Ivoire', 'CIV', 384);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('HR', 'Croatia', 'HRV', 191);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CU', 'Cuba', 'CUB', 192);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CY', 'Cyprus', 'CYP', 196);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CZ', 'Czech Republic', 'CZE', 203);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('DK', 'Denmark', 'DNK', 208);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('DJ', 'Djibouti', 'DJI', 262);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('DM', 'Dominica', 'DMA', 212);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('DO', 'Dominican Republic', 'DOM', 214);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('EC', 'Ecuador', 'ECU', 218);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('EG', 'Egypt', 'EGY', 818);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SV', 'El Salvador', 'SLV', 222);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GQ', 'Equatorial Guinea', 'GNQ', 226);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ER', 'Eritrea', 'ERI', 232);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('EE', 'Estonia', 'EST', 233);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ET', 'Ethiopia', 'ETH', 231);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('FK', 'Falkland Islands (Malvinas)', 'FLK', 238);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('FO', 'Faroe Islands', 'FRO', 234);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('FJ', 'Fiji', 'FJI', 242);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('FI', 'Finland', 'FIN', 246);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('FR', 'France', 'FRA', 250);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GF', 'French Guiana', 'GUF', 254);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PF', 'French Polynesia', 'PYF', 258);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TF', 'French Southern Territories', 'ATF', 260);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GA', 'Gabon', 'GAB', 266);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GM', 'Gambia', 'GMB', 270);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GE', 'Georgia', 'GEO', 268);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('DE', 'Germany', 'DEU', 276);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GH', 'Ghana', 'GHA', 288);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GI', 'Gibraltar', 'GIB', 292);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GR', 'Greece', 'GRC', 300);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GL', 'Greenland', 'GRL', 304);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GD', 'Grenada', 'GRD', 308);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GP', 'Guadeloupe', 'GLP', 312);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GU', 'Guam', 'GUM', 316);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GT', 'Guatemala', 'GTM', 320);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GG', 'Guernsey', 'GGY', 831);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GN', 'Guinea', 'GIN', 324);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GW', 'Guinea-Bissau', 'GNB', 624);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GY', 'Guyana', 'GUY', 328);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('HT', 'Haiti', 'HTI', 332);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('HM', 'Heard and Mcdonald Islands', 'HMD', 334);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('VA', 'Holy See (Vatican City State)', 'VAT', 336);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('HN', 'Honduras', 'HND', 340);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('HU', 'Hungary', 'HUN', 348);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IS', 'Iceland', 'ISL', 352);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IN', 'India', 'IND', 356);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ID', 'Indonesia', 'IDN', 360);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IR', 'Iran', 'IRN', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IQ', 'Iraq', 'IRQ', 368);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IE', 'Ireland', 'IRL', 372);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IM', 'Isle of Man', 'IMN', 833);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IL', 'Israel', 'ISR', 376);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('IT', 'Italy', 'ITA', 380);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('JM', 'Jamaica', 'JAM', 388);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('JP', 'Japan', 'JPN', 392);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('JE', 'Jersey', 'JEY', 832);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('JO', 'Jordan', 'JOR', 400);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KZ', 'Kazakhstan', 'KAZ', 398);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KE', 'Kenya', 'KEN', 404);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KI', 'Kiribati', 'KIR', 296);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KP', 'Korea (North)', 'PRK', 408);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KR', 'Korea (South)', 'KOR', 410);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KW', 'Kuwait', 'KWT', 414);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KG', 'Kyrgyzstan', 'KGZ', 417);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LA', 'Lao PDR', 'LAO', 418);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LV', 'Latvia', 'LVA', 428);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LB', 'Lebanon', 'LBN', 422);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LS', 'Lesotho', 'LSO', 426);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LR', 'Liberia', 'LBR', 430);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LY', 'Libya', 'LBY', 434);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LI', 'Liechtenstein', 'LIE', 438);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LT', 'Lithuania', 'LTU', 440);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LU', 'Luxembourg', 'LUX', 442);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MK', 'Macedonia', 'MKD', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MG', 'Madagascar', 'MDG', 450);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MW', 'Malawi', 'MWI', 454);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MY', 'Malaysia', 'MYS', 458);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MV', 'Maldives', 'MDV', 462);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ML', 'Mali', 'MLI', 466);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MT', 'Malta', 'MLT', 470);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MH', 'Marshall Islands', 'MHL', 584);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MQ', 'Martinique', 'MTQ', 474);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MR', 'Mauritania', 'MRT', 478);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MU', 'Mauritius', 'MUS', 480);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('YT', 'Mayotte', 'MYT', 175);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MX', 'Mexico', 'MEX', 484);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('FM', 'Micronesia', 'FSM', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MD', 'Moldova', 'MDA', 498);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MC', 'Monaco', 'MCO', 492);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MN', 'Mongolia', 'MNG', 496);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ME', 'Montenegro', 'MNE', 499);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MS', 'Montserrat', 'MSR', 500);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MA', 'Morocco', 'MAR', 504);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MZ', 'Mozambique', 'MOZ', 508);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MM', 'Myanmar', 'MMR', 104);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NA', 'Namibia', 'NAM', 516);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NR', 'Nauru', 'NRU', 520);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NP', 'Nepal', 'NPL', 524);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NL', 'Netherlands', 'NLD', 528);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AN', 'Netherlands Antilles', 'ANT', 530);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NC', 'New Caledonia', 'NCL', 540);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NZ', 'New Zealand', 'NZL', 554);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NI', 'Nicaragua', 'NIC', 558);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NE', 'Niger', 'NER', 562);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NG', 'Nigeria', 'NGA', 566);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NU', 'Niue', 'NIU', 570);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NF', 'Norfolk Island', 'NFK', 574);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MP', 'Northern Mariana Islands', 'MNP', 580);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('NO', 'Norway', 'NOR', 578);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('OM', 'Oman', 'OMN', 512);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PK', 'Pakistan', 'PAK', 586);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PW', 'Palau', 'PLW', 585);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PS', 'Palestinian Territory', 'PSE', 275);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PA', 'Panama', 'PAN', 591);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PG', 'Papua New Guinea', 'PNG', 598);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PY', 'Paraguay', 'PRY', 600);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PE', 'Peru', 'PER', 604);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PH', 'Philippines', 'PHL', 608);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PN', 'Pitcairn', 'PCN', 612);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PL', 'Poland', 'POL', 616);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PT', 'Portugal', 'PRT', 620);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PR', 'Puerto Rico', 'PRI', 630);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('QA', 'Qatar', 'QAT', 634);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('RE', 'Reunion', 'REU', 638);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('RO', 'Romania', 'ROU', 642);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('RU', 'Russian Federation', 'RUS', 643);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('RW', 'Rwanda', 'RWA', 646);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('BL', 'Saint-Barth lemy', 'BLM', 652);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SH', 'Saint Helena', 'SHN', 654);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('KN', 'Saint Kitts and Nevis', 'KNA', 659);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LC', 'Saint Lucia', 'LCA', 662);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('MF', 'Saint-Martin (French part)', 'MAF', 663);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('PM', 'Saint Pierre and Miquelon', 'SPM', 666);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('VC', 'Saint Vincent and Grenadines', 'VCT', 670);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('WS', 'Samoa', 'WSM', 882);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SM', 'San Marino', 'SMR', 674);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ST', 'Sao Tome and Principe', 'STP', 678);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SA', 'Saudi Arabia', 'SAU', 682);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SN', 'Senegal', 'SEN', 686);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('RS', 'Serbia', 'SRB', 688);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SC', 'Seychelles', 'SYC', 690);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SL', 'Sierra Leone', 'SLE', 694);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SG', 'Singapore', 'SGP', 702);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SK', 'Slovakia', 'SVK', 703);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SI', 'Slovenia', 'SVN', 705);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SB', 'Solomon Islands', 'SLB', 90);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SO', 'Somalia', 'SOM', 706);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ZA', 'South Africa', 'ZAF', 710);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GS', 'South Georgia and the South Sandwich Islands', 'SGS', 239);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SS', 'South Sudan', 'SSD', 728);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ES', 'Spain', 'ESP', 724);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('LK', 'Sri Lanka', 'LKA', 144);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SD', 'Sudan', 'SDN', 736);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SR', 'Suriname', 'SUR', 740);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SJ', 'Svalbard and Jan Mayen Islands', 'SJM', 744);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SZ', 'Swaziland', 'SWZ', 748);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SE', 'Sweden', 'SWE', 752);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('CH', 'Switzerland', 'CHE', 756);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('SY', 'Syrian Arab Republic (Syria)', 'SYR', 760);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TW', 'Taiwan', 'TWN', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TJ', 'Tajikistan', 'TJK', 762);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TZ', 'Tanzania', 'TZA', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TH', 'Thailand', 'THA', 764);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TL', 'Timor-Leste', 'TLS', 626);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TG', 'Togo', 'TGO', 768);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TK', 'Tokelau', 'TKL', 772);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TO', 'Tonga', 'TON', 776);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TT', 'Trinidad and Tobago', 'TTO', 780);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TN', 'Tunisia', 'TUN', 788);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TR', 'Turkey', 'TUR', 792);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TM', 'Turkmenistan', 'TKM', 795);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TC', 'Turks and Caicos Islands', 'TCA', 796);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('TV', 'Tuvalu', 'TUV', 798);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('UG', 'Uganda', 'UGA', 800);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('UA', 'Ukraine', 'UKR', 804);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('AE', 'United Arab Emirates', 'ARE', 784);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('GB', 'United Kingdom', 'GBR', 826);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('US', 'United States of America', 'USA', 840);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('UM', 'US Minor Outlying Islands', 'UMI', 581);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('UY', 'Uruguay', 'URY', 858);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('UZ', 'Uzbekistan', 'UZB', 860);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('VU', 'Vanuatu', 'VUT', 548);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('VE', 'Venezuela (Bolivarian Republic)', 'VEN', 862);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('VN', 'Viet Nam', 'VNM', 704);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('VI', 'Virgin Islands', ' US', 0);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('WF', 'Wallis and Futuna Islands', 'WLF', 876);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('EH', 'Western Sahara', 'ESH', 732);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('YE', 'Yemen', 'YEM', 887);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ZM', 'Zambia', 'ZMB', 894);
INSERT INTO `collector`.`Countries` (`Cou_Code`, `Cou_Name`, `Cou_A3`, `Cou_N`) VALUES ('ZW', 'Zimbabwe', 'ZWE', 716);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Dev_Tables`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (19, 'Charge_Items', 'Charge Items', 'Charge Item', 'charge_item', 'NULL', 'Charge_Units', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (20, 'Charge_Units', 'Charge Units', 'Charge Unit', 'charge_unit', 'Charge_Items', 'Configuration_Items', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (21, 'CIT_Generations', 'Configuration Items Generation Types', 'Configuration Item Generation Type', 'cit_generation', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (22, 'CIT_Statuses', 'Configuration Items Status Types', 'Configuration Item Status Type', 'cit_status', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (23, 'Configuration_Items', 'Configuration Items', 'Configuration Item', 'configuration_item', 'Charge_Units', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (24, 'Cost_Centers', 'Cost Centers', 'Cost Center', 'cost_center', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (25, 'Countries', 'Countries', 'Country', 'country', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (26, 'Countries_Currencies', 'Countries vs Currencies', 'Country vs Currency', 'country_currency', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (27, 'CU_Operations', 'Charge Units Conversion Operations', 'Charge Unit Conversion Operation', 'cu_operation', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (28, 'CU_Types', 'Configuration Unit Types', 'Configuration Unit Type', 'cu_type', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (29, 'Currencies', 'Currencies', 'Currency', 'currency', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (30, 'Customers', 'Customers', 'Customer', 'customer', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (31, 'Dev_Forms', 'Forms', 'Form', 'dev_form', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (32, 'Dev_Tables', 'Tables', 'Table', 'dev_table', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (33, 'Exchange_Rates', 'Exchange Rates', 'Exchange Rate', 'exchange_rate', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (34, 'Measure_Units', 'Measure Units', 'Measure Unit', 'measure_unit', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (35, 'Platforms', 'Platforms', 'Platform', 'platform', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (36, 'Rat_Periods', 'Rate Periods', 'Rate Period', 'rat_period', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (37, 'Rates', 'Rates', 'Rate', 'rate', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (38, 'Trace', 'Trace', 'Trace line', 'trace', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (39, 'Users', 'Users', 'User', 'User', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);
INSERT INTO `collector`.`Dev_Tables` (`Id`, `Name`, `Caption`, `Entity`, `Class_Name`, `Child_Table`, `Parent_Table`, `Use_Pagination`, `Use_Children_Pagination`, `Generate_Form_One`, `Generate_Form_All`, `Generate_Form_Filter`, `Generate_Children`, `Generate_Foreign_Fields`, `Permission_View`, `Permission_Delete`, `Permission_Modify`, `Permission_Report`, `Permission_Export`, `Permission_View_Private`, `Permission_Modify_Private`, `Permission_Administer`) VALUES (40, 'Roles', 'Roles', 'Role', 'Role', 'NULL', 'NULL', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Countries_Currencies`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Countries_Currencies` (`Cou_Code`, `Cur_Code`, `Cou_Cur_Comment`) VALUES ('US', 'USD', NULL);
INSERT INTO `collector`.`Countries_Currencies` (`Cou_Code`, `Cur_Code`, `Cou_Cur_Comment`) VALUES ('CL', 'CLP', NULL);
INSERT INTO `collector`.`Countries_Currencies` (`Cou_Code`, `Cur_Code`, `Cou_Cur_Comment`) VALUES ('CL', 'UF', NULL);
INSERT INTO `collector`.`Countries_Currencies` (`Cou_Code`, `Cur_Code`, `Cou_Cur_Comment`) VALUES ('PE', 'PEN', NULL);
INSERT INTO `collector`.`Countries_Currencies` (`Cou_Code`, `Cur_Code`, `Cou_Cur_Comment`) VALUES ('CO', 'COP', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Roles`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Roles` (`id`, `name`, `default`, `permissions`) VALUES (1, 'Customer', 0, 1);
INSERT INTO `collector`.`Roles` (`id`, `name`, `default`, `permissions`) VALUES (2, 'Reporter', 1, 50);
INSERT INTO `collector`.`Roles` (`id`, `name`, `default`, `permissions`) VALUES (3, 'Charger', 0, 30);
INSERT INTO `collector`.`Roles` (`id`, `name`, `default`, `permissions`) VALUES (4, 'Administrator', 0, 254);
INSERT INTO `collector`.`Roles` (`id`, `name`, `default`, `permissions`) VALUES (5, 'Auditor', 0, 510);
INSERT INTO `collector`.`Roles` (`id`, `name`, `default`, `permissions`) VALUES (6, 'God', 0, 4095);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Users`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Users` (`id`, `username`, `role_id`, `email`, `password_hash`, `confirmed`, `CC_Id`) VALUES (1, 'gvalera', 4, 'gvalera@emtecgroup.net', 'pbkdf2:sha1:1000$00zgMbi7$fbfce9d2dae139caa8f3292f38034af9d920573a', 1, 1);
INSERT INTO `collector`.`Users` (`id`, `username`, `role_id`, `email`, `password_hash`, `confirmed`, `CC_Id`) VALUES (2, 'admin', 4, 'admin_collector@email.com', 'pbkdf2:sha1:1000$vahNJ55E$c83864399cdee6b09e49b5466dafd3faa0be8d42', 1, 1);
INSERT INTO `collector`.`Users` (`id`, `username`, `role_id`, `email`, `password_hash`, `confirmed`, `CC_Id`) VALUES (3, 'reporter', 2, 'reporter_collector@email.com', 'pbkdf2:sha1:1000$V2Z9cCpK$606122c48e02546fe958dcd6d10cb7fb958243da', 1, 1);
INSERT INTO `collector`.`Users` (`id`, `username`, `role_id`, `email`, `password_hash`, `confirmed`, `CC_Id`) VALUES (4, 'charger', 3, 'charger_collector@email.com', 'pbkdf2:sha1:1000$84fgaNC7$34b48fe45a56e64568a7319278fe99711aad2ecd', 1, 1);
INSERT INTO `collector`.`Users` (`id`, `username`, `role_id`, `email`, `password_hash`, `confirmed`, `CC_Id`) VALUES (5, 'customer', 1, 'customer@email.com', 'pbkdf2:sha1:1000$SmupDW8t$60698bb6775cf9c870ced2547a1f0caf261f9b2f', 1, 1);
INSERT INTO `collector`.`Users` (`id`, `username`, `role_id`, `email`, `password_hash`, `confirmed`, `CC_Id`) VALUES (6, 'auditor', 5, 'auditor@email.com', 'pbkdf2:sha1:1000$CXI2LsFR$2c0440ec7bb25f9d3285c80398c2a5bf171a7bdc', 1, 1);
INSERT INTO `collector`.`Users` (`id`, `username`, `role_id`, `email`, `password_hash`, `confirmed`, `CC_Id`) VALUES (7, 'linux', 1, 'linux@email.com', 'pbkdf2:sha1:1000$L2oMWyIa$de9daf8e7a5266aec15d046739f3fbe06308b329', 1, 1);
INSERT INTO `collector`.`Users` (`id`, `username`, `role_id`, `email`, `password_hash`, `confirmed`, `CC_Id`) VALUES (8, 'windows', 1, 'windows@email.com', 'pbkdf2:sha1:1000$HxIvGI6f$f2f99d6e691e47337cc6c2f37047c8bce6d01c00', 1, 1);

COMMIT;

