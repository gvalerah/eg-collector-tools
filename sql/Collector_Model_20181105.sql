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

-- -----------------------------------------------------
-- Table `collector`.`Cost_Centers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Cost_Centers` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Cost_Centers` (
  `CC_Id` INT NOT NULL AUTO_INCREMENT COMMENT 'Unique Colletor\'s System Id (Auto generated)\n',
  `CC_Code` VARCHAR(45) NULL COMMENT 'Known billing system code',
  `CC_Description` VARCHAR(45) NULL COMMENT 'Description of CC Location',
  `Cur_Code` VARCHAR(3) NOT NULL,
  PRIMARY KEY (`CC_Id`),
  CONSTRAINT `fk_Cost_Centers_Currencies1`
    FOREIGN KEY (`Cur_Code`)
    REFERENCES `collector`.`Currencies` (`Cur_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Cost_Centers_Currencies1_idx` ON `collector`.`Cost_Centers` (`Cur_Code` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `collector`.`Customers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Customers` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Customers` (
  `Cus_Id` INT NOT NULL AUTO_INCREMENT,
  `Cus_Name` VARCHAR(45) NOT NULL,
  `CC_Id` INT NOT NULL COMMENT 'Default CC in case CI does not have a defined CI-CC',
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
CREATE INDEX `fk_Customers_Cost_Centers1_idx` ON `collector`.`Customers` (`CC_Id` ASC) VISIBLE;

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
-- Table `collector`.`Configuration_Items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `collector`.`Configuration_Items` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `collector`.`Configuration_Items` (
  `CI_Id` INT NOT NULL AUTO_INCREMENT,
  `CI_Name` VARCHAR(45) NOT NULL,
  `CI_UUID` VARCHAR(45) NOT NULL,
  `Pla_Id` INT NOT NULL,
  `CC_Id` INT NOT NULL COMMENT 'Default CC in case CU does not have a defined CC',
  `CIT_Generation` INT NOT NULL DEFAULT 0,
  `Cus_Id` INT NOT NULL DEFAULT 1,
  PRIMARY KEY (`CI_Id`),
  CONSTRAINT `fk_Configuration_Items_Platforms1`
    FOREIGN KEY (`Pla_Id`)
    REFERENCES `collector`.`Platforms` (`Pla_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Configuration_Items_Cost_Centers1`
    FOREIGN KEY (`CC_Id`)
    REFERENCES `collector`.`Cost_Centers` (`CC_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Configuration_Items_Customers1`
    FOREIGN KEY (`Cus_Id`)
    REFERENCES `collector`.`Customers` (`Cus_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Configuration_Items_CIT_Generations1`
    FOREIGN KEY (`CIT_Generation`)
    REFERENCES `collector`.`CIT_Generations` (`CIT_Generation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Configuration_Items_Platforms1_idx` ON `collector`.`Configuration_Items` (`Pla_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Configuration_Items_Cost_Centers1_idx` ON `collector`.`Configuration_Items` (`CC_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Configuration_Items_Customers1_idx` ON `collector`.`Configuration_Items` (`Cus_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Configuration_Items_CIT_Generations1_idx` ON `collector`.`Configuration_Items` (`CIT_Generation` ASC) VISIBLE;

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
  `CU_Operations` VARCHAR(10) NOT NULL,
  `Value` VARCHAR(45) NULL,
  `Is_Multiply` TINYINT NULL,
  `Factor` INT NULL,
  PRIMARY KEY (`CU_Operations`))
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
  `CU_Operations` VARCHAR(10) NOT NULL,
  `Typ_Code` VARCHAR(10) NOT NULL,
  `CC_Id` INT NOT NULL,
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
  CONSTRAINT `fk_Charge_Units_Cost_Centers1`
    FOREIGN KEY (`CC_Id`)
    REFERENCES `collector`.`Cost_Centers` (`CC_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Charge_Units_CU_Operations1`
    FOREIGN KEY (`CU_Operations`)
    REFERENCES `collector`.`CU_Operations` (`CU_Operations`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_Configuration_Items1_idx` ON `collector`.`Charge_Units` (`CI_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_CU_Types1_idx` ON `collector`.`Charge_Units` (`Typ_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_Cost_Centers1_idx` ON `collector`.`Charge_Units` (`CC_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_CU_Operations1_idx` ON `collector`.`Charge_Units` (`CU_Operations` ASC) VISIBLE;

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
  `CU_Id` INT NOT NULL,
  `Rat_Price` DECIMAL(20,6) NULL,
  `Cur_Code` VARCHAR(3) NOT NULL,
  `MU_Code` VARCHAR(3) NOT NULL,
  `Rat_Period` INT NOT NULL,
  PRIMARY KEY (`Rat_Id`),
  CONSTRAINT `fk_Rate_Platform1`
    FOREIGN KEY (`Pla_Id`)
    REFERENCES `collector`.`Platforms` (`Pla_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rate_Cost_Center1`
    FOREIGN KEY (`CC_Id`)
    REFERENCES `collector`.`Cost_Centers` (`CC_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rate_Customer2`
    FOREIGN KEY (`Cus_Id`)
    REFERENCES `collector`.`Customers` (`Cus_Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rate_Charge_Unit1`
    FOREIGN KEY (`CU_Id`)
    REFERENCES `collector`.`Charge_Units` (`CU_Id`)
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
  CONSTRAINT `fk_Rates_Currencies1`
    FOREIGN KEY (`Cur_Code`)
    REFERENCES `collector`.`Currencies` (`Cur_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Rates_Rat_Periods1`
    FOREIGN KEY (`Rat_Period`)
    REFERENCES `collector`.`Rat_Periods` (`Rat_Period`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_Rate_Platform1_idx` ON `collector`.`Rates` (`Pla_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rate_Cost_Center1_idx` ON `collector`.`Rates` (`CC_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rate_Customer2_idx` ON `collector`.`Rates` (`Cus_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rate_Charge_Unit1_idx` ON `collector`.`Rates` (`CU_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_Measure_Units1_idx` ON `collector`.`Rates` (`MU_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_CU_Types1_idx` ON `collector`.`Rates` (`Typ_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_Currencies1_idx` ON `collector`.`Rates` (`Cur_Code` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Rates_Rat_Periods1_idx` ON `collector`.`Rates` (`Rat_Period` ASC) VISIBLE;

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
  `CU_Id` INT NOT NULL,
  `CIT_Date` DATE NOT NULL,
  `CIT_Time` TIME NOT NULL DEFAULT "00:00:00",
  `CIT_Quantity` DECIMAL(20,6) NOT NULL DEFAULT 0,
  `CIT_Status` INT NOT NULL DEFAULT 0,
  `CIT_Is_Active` TINYINT NULL DEFAULT 0,
  `Charge_Itemscol` VARCHAR(45) NULL DEFAULT 0,
  PRIMARY KEY (`CU_Id`, `CIT_Date`, `CIT_Time`),
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
  `ER_Factor` DECIMAL(20,6) NOT NULL DEFAULT 0.0,
  `ER_Date` DATE NOT NULL DEFAULT "2018-01-01",
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
CREATE INDEX `fk_Exchange_Rates_Currencies1_idx` ON `collector`.`Exchange_Rates` (`Cur_Code` ASC) VISIBLE;

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
CREATE UNIQUE INDEX `Cou_Code_UNIQUE` ON `collector`.`Countries` (`Cou_Code` ASC) VISIBLE;

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
			WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = PLATFORM AND Cus_Id = CUSTOMER AND CC_Id = CC AND CU_Id = ID
            LIMIT 1 INTO RATE;
		IF (RATE IS NULL) THEN
			SELECT Rat_Id FROM Rates
				WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = PLATFORM AND Cus_Id = CUSTOMER AND CC_Id = CC and CU_Id = 1
				LIMIT 1 INTO RATE;
			IF (RATE IS NULL) THEN
				SELECT Rat_Id FROM Rates
					WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = PLATFORM AND Cus_Id = CUSTOMER AND CC_Id = 1 and CU_Id = 1
					LIMIT 1 INTO RATE;
				IF (RATE IS NULL) THEN
					SELECT Rat_Id FROM Rates
						WHERE 	Typ_Code = TYPE_CODE AND PLa_Id = PLATFORM AND Cus_Id = 1 AND CC_Id = 1 and CU_Id = 1
						LIMIT 1 INTO RATE;
					IF (RATE IS NULL) THEN
						SELECT Rat_Id FROM Rates
							WHERE 	Typ_Code = TYPE_CODE AND Pla_Id = 1 AND Cus_Id = 1 AND CC_Id = 1 and CU_Id = 1
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
		IF 		PERIOD = 0 THEN
				SET PRICE_PER_HOUR = PRICE;
		ELSEIF 	PERIOD = 1 THEN
				SET PRICE_PER_HOUR = PRICE / 24 ;
		ELSEIF 	PERIOD = 2 THEN
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
		Charge_Units.CC_Id 								AS CC,
		Configuration_Items.CI_Id 						AS CI_ID,
        Configuration_Items.CI_Name 					AS CI,
		Charge_Units.CU_Id 								AS CU_ID,
		Charge_Units.CU_Description 					AS CU,
        Rates.Rat_Id									AS RATE,
        Rates.Rat_Price									AS RATE_PRICE,
        Rates.Cur_Code 									AS RATE_CUR,
		Rates.MU_Code									AS MU,
        IF(Rates.Rat_Period=0,"HOUR",
			IF(Rates.Rat_Period=1,"DAY",
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
	RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE XR 				FLOAT;
	DECLARE XRFROM 			FLOAT;
	DECLARE XRTO 			FLOAT;
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
	SET XR = XRFROM/XRTO;
 
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
CREATE FUNCTION `Get_CU_Id_From_UUID` (UUID VARCHAR(45),XCI_ID INT,XTYPE VARCHAR(10)) RETURNS INT DETERMINISTIC
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
	DECLARE _CI_ID	INT;
	DECLARE _CU_ID	INT;
	DECLARE _Q	 	DECIMAL(20,6);
	
    # Needs to be sure that recursion is possible
    SET @@max_sp_recursion_depth = 8;
    
    # Verifies if CI_UUID Corresponds to a valid Configuration Item
    
    SET _CI_ID = Get_CI_Id_From_UUID(CI_UUID);
    
    #call Tracer(concat("P1 Entrada CI_ID=",_CI_ID));
    
    IF _CI_ID IS NOT NULL THEN
		# Gets Configuration Unit Id from raw DataType of CU and UUID for CI and CU
		SET _CU_ID = Get_CU_Id_From_Data(CI_UUID,CU_UUID,CU_TYPE);

		#call Tracer (concat("P2 Entrada CU_ID=",_CU_ID));

        # Checks if a valid CU Id was found
		IF _CU_ID IS NOT NULL THEN
			#call Tracer("P3 INSERT");
			# Creates an Item billing record for the valud Charge Unit
            # ----------------------------------------------------------------------------
            SELECT CIT_Quantity FROM Charge_Items WHERE CU_Id=_CU_ID AND CIT_Date=X_DATE AND CIT_Time=X_TIME LIMIT 1 INTO _Q;

            IF _Q IS NULL THEN
				#call Tracer("P3.1 CIT_QUANTITY = NULL then INSERT ....");
				START TRANSACTION;
				INSERT IGNORE INTO Charge_Items VALUES(_CU_ID,X_DATE,X_TIME,QUANTITY,1,X_ACTIVE); # STATUS = 1 Created, Pending Approval
				COMMIT;
			ELSE 
				#call Tracer(concat("P3.2 CIT_QUANTITY = ",_Q," QUANTITY = ",QUANTITY," Check ..."));
				IF QUANTITY > _Q THEN
					call Tracer(concat("P3.3 CIT_QUANTITY = ",_Q," QUANTITY = ",QUANTITY," UPDATE ..."));
					START TRANSACTION;
					UPDATE Charge_Items SET CIT_QUANTITY = QUANTITY WHERE CU_Id=_CU_ID AND CIT_Date=X_DATE AND CIT_Time=X_TIME; # STATUS = 1 Created, Pending Approval
                    COMMIT;
				#ELSE
					#call Tracer(concat("P3.4 CIT_QUANTITY = ",_Q," QUANTITY = ",QUANTITY," No UPDATE Re_Quired ..."));					
                END IF;
            END IF;
            # ----------------------------------------------------------------------------
		ELSE 
			#call Tracer("P4 CU NO Encontrado llama a CALL Create CU");
			# Tries to complete DB Integrity by creating a Dummy Charge Unit
			CALL Create_Charge_Unit(_CI_ID,NULL, CU_UUID,1,1,QUANTITY,NULL,CU_TYPE,NULL); # 1 = Is Billeable
            SET _CU_ID =  Get_CU_Id_From_Data(CI_UUID,CU_UUID,CU_TYPE);
			
            #call Tracer(concat("P5 CU_ID=",_CU_ID));		# Checks if a valid CU Id was found
			
            IF _CU_ID IS NOT NULL THEN
           		call Tracer("P6 Llamada recursiva por CU recreado");		# Checks if a valid CU Id was found
				CALL Record_Item (CU_TYPE,CI_UUID,CU_UUID,QUANTITY,X_DATE,X_TIME,X_ACTIVE); # Recursive Call
            END IF;
		END IF;
	ELSE
		# Tries to complete DB Integrity by creating a Dummy Configuration Item
		#call Tracer("P6 CI NO Encontrado llama a CALL Create CI");
		CALL Create_Configuration_Item(NULL,CI_UUID,1,1,1,1);
        # Validates if a valid Configuration Item was created 
		SET _CI_ID = Get_CI_Id_From_UUID(CI_UUID);
   		#call Tracer (concat("P7 Creado CI_ID=",CI_ID));
		IF _CI_ID IS NOT NULL THEN
       		#call Tracer("P8 Llamada recursiva por CI recreado");		# Checks if a valid CU Id was found
			# If Configuration Item is valid now will try to create Charge item billing record
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
CREATE PROCEDURE `Create_Configuration_Item` (CI_NAME VARCHAR(45),CI_UUID VARCHAR(45),PLATFORM INT,CC INT,CIT_GEN INT,CUSTOMER INT)
BEGIN
	DECLARE XID		 	INT;
	DECLARE XNAME	 	VARCHAR(45);
	DECLARE XPLATFORM 	INT;
	DECLARE XCC			INT;
	DECLARE XCIT_GEN	INT;
	
	SET XNAME	 	= IF(CI_NAME IS NULL,"CI NO NAME",CI_NAME);
	SET XPLATFORM 	= IF(PLATFORM IS NULL,1,PLATFORM);
	SET XCC 		= IF(CC IS NULL,1,CC);
	SET XCIT_GEN	= IF(CIT_GEN IS NULL,1,CIT_GEN);
    
    # Checks for existence of CI
    SET XID 		= Get_CI_Id_From_UUID(CI_UUID);

	# If CI does not exists then creates it
	IF XID IS NULL THEN
			START TRANSACTION;
			INSERT INTO Configuration_Items VALUES(0,XNAME,CI_UUID,XPLATFORM,XCC,XCIT_GEN,CUSTOMER);
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
CREATE PROCEDURE `Create_Charge_Unit` (CI_ID INT,DESCRIPTION VARCHAR(45),CU_UUID VARCHAR(45),ISBILLEABLE BOOLEAN,ISALLWAYS BOOLEAN,QUANTITY DECIMAL(20,6),OPERATION VARCHAR(10),CU_TYPE VARCHAR(10),CC_ID INT)
BEGIN
	DECLARE CU_ID 				INT;
	DECLARE XDESCRIPTION	 	VARCHAR(45);
	DECLARE XISBILLEABLE	 	BOOLEAN;
	DECLARE XISALLWAYS	 		BOOLEAN;
	DECLARE XOPERATION			VARCHAR(10);
	DECLARE XCC_ID				VARCHAR(10);
	
	SET XDESCRIPTION = IF(DESCRIPTION IS NULL,"CU NO DESCRIPTION",DESCRIPTION);
	SET XISBILLEABLE = IF(ISBILLEABLE IS NULL,TRUE,ISBILLEABLE);
	SET XISALLWAYS   = IF(ISALLWAYS   IS NULL,TRUE,ISALLWAYS);
	SET XOPERATION   = IF(OPERATION   IS NULL,"NONE",OPERATION);
	SET XCC_ID	   	 = IF(CC_ID       IS NULL,1,CC_ID);
    
    # Checks for CU existence
    SET CU_ID = Get_CU_Id_From_UUID(CU_UUID,CI_ID,CU_TYPE);

	# If CU does not exist then creates it
	IF CU_ID IS NULL THEN
			START TRANSACTION;
			INSERT IGNORE INTO Charge_Units VALUES(0,CI_ID,XDESCRIPTION,CU_UUID,XISBILLEABLE,XISALLWAYS,QUANTITY,XOPERATION,CU_TYPE,XCC_ID);
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
-- procedure Fix_Rates
-- -----------------------------------------------------

USE `collector`;
DROP procedure IF EXISTS `collector`.`Fix_Rates`;
SHOW WARNINGS;

DELIMITER $$
USE `collector`$$
CREATE PROCEDURE `Fix_Rates` ()
BEGIN
	START TRANSACTION;
	UPDATE Rates
		SET 	Rat_Price_Hour=Rat_Price        , Rat_Price_Day=Rat_Price*24 , Rat_Price_Month=Rat_Price*24*30
		WHERE 	Rat_Id>0 
			AND Rat_Period=0;
	UPDATE Rates 
		SET 	Rat_Price_Hour=Rat_Price/24     , Rat_Price_Day=Rat_Price   , Rat_Price_Month=Rat_Price*30
        WHERE 	Rat_Id>0
			AND Rat_Period=1;
	UPDATE Rates 
		SET 	Rat_Price_Hour=(Rat_Price/24)/30, Rat_Price_Day=Rat_Price/24, Rat_Price_Month=Rat_Price
        WHERE 	Rat_Id>0
			AND Rat_Period=2;
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

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `collector`.`Platforms`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (1, 'DEFAULT', 'localhost', '80', 'user', 'password');
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (2, 'DC Primario Cluster P1', 'localhost', '60000', 'collector', 'collector');
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (3, 'DC Primario Cluster P2', 'localhost', '70000', 'collector', 'collector');
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (4, 'DC Secundario Cluster S1', 'localhost', '80000', 'collector', 'collector');
INSERT INTO `collector`.`Platforms` (`Pla_Id`, `Pla_Name`, `Pla_Host`, `Pla_Port`, `Pla_User`, `Pla_Password`) VALUES (5, 'DC Secundario Cluster S2', 'localhost', '90000', 'collector', 'collector');

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
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (1, 'DEFAULT-CC-CODE', 'DEFAULT-CC_Description', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (2, 'CODE-2-X', 'CC-CUS-SERTECHNO', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (3, 'CODE-3-X', 'CC-CUS-SERTECHNO CHILE', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (4, 'CODE-4-X', 'CC-CUS-SERTECHNO COLOMBIA', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (5, 'CODE-5-X', 'CC-CUS-SERTECHNO PERU', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (6, 'CODE-6-X', 'CC-CUS-EMTEC GROUP', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (7, 'CODE-7-X', 'CC-CUS-EMTEC CHILE', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (8, 'CODE-8-X', 'CC-CUS-EMTEC PERU', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (9, 'CODE-9-X', 'CC-CUS-EMTEC COLOMBIA', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (10, 'CODE-10-X', 'CC-CUS-Business Unit 10 - Corp', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (11, 'CODE-11-X', 'CC-CUS-Business Unit 11 - CL', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (12, 'CODE-12-X', 'CC-CUS-Business Unit 12 - PE', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (13, 'CODE-13-X', 'CC-CUS-Business Unit 13 - CO', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (14, 'CODE-10001-X', 'CC-CI-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (15, 'CODE-10001001-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (16, 'CODE-10001002-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (17, 'CODE-10001003-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (18, 'CODE-10001004-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (19, 'CODE-10001005-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (20, 'CODE-10001006-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (21, 'CODE-10001007-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (22, 'CODE-10001008-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (23, 'CODE-10001009-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (24, 'CODE-10001010-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (25, 'CODE-10001011-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (26, 'CODE-10001012-X', 'CC-CU-VM-BU-10-PL-P1-1', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (27, 'CODE-10002-X', 'CC-CI-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (28, 'CODE-10002013-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (29, 'CODE-10002014-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (30, 'CODE-10002015-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (31, 'CODE-10002016-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (32, 'CODE-10002017-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (33, 'CODE-10002018-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (34, 'CODE-10002019-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (35, 'CODE-10002020-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (36, 'CODE-10002021-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (37, 'CODE-10002022-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (38, 'CODE-10002023-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (39, 'CODE-10002024-X', 'CC-CU-VM-BU-10-PL-P2-2', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (40, 'CODE-10003-X', 'CC-CI-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (41, 'CODE-10003025-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (42, 'CODE-10003026-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (43, 'CODE-10003027-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (44, 'CODE-10003028-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (45, 'CODE-10003029-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (46, 'CODE-10003030-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (47, 'CODE-10003031-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (48, 'CODE-10003032-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (49, 'CODE-10003033-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (50, 'CODE-10003034-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (51, 'CODE-10003035-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (52, 'CODE-10003036-X', 'CC-CU-VM-BU-10-PL-S1-3', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (53, 'CODE-10004-X', 'CC-CI-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (54, 'CODE-10004037-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (55, 'CODE-10004038-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (56, 'CODE-10004039-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (57, 'CODE-10004040-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (58, 'CODE-10004041-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (59, 'CODE-10004042-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (60, 'CODE-10004043-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (61, 'CODE-10004044-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (62, 'CODE-10004045-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (63, 'CODE-10004046-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (64, 'CODE-10004047-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (65, 'CODE-10004048-X', 'CC-CU-VM-BU-10-PL-S2-4', 'USD');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (66, 'CODE-11005-X', 'CC-CI-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (67, 'CODE-11005049-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (68, 'CODE-11005050-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (69, 'CODE-11005051-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (70, 'CODE-11005052-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (71, 'CODE-11005053-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (72, 'CODE-11005054-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (73, 'CODE-11005055-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (74, 'CODE-11005056-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (75, 'CODE-11005057-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (76, 'CODE-11005058-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (77, 'CODE-11005059-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (78, 'CODE-11005060-X', 'CC-CU-VM-BU-11-PL-P1-5', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (79, 'CODE-11006-X', 'CC-CI-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (80, 'CODE-11006061-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (81, 'CODE-11006062-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (82, 'CODE-11006063-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (83, 'CODE-11006064-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (84, 'CODE-11006065-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (85, 'CODE-11006066-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (86, 'CODE-11006067-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (87, 'CODE-11006068-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (88, 'CODE-11006069-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (89, 'CODE-11006070-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (90, 'CODE-11006071-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (91, 'CODE-11006072-X', 'CC-CU-VM-BU-11-PL-P2-6', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (92, 'CODE-11007-X', 'CC-CI-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (93, 'CODE-11007073-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (94, 'CODE-11007074-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (95, 'CODE-11007075-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (96, 'CODE-11007076-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (97, 'CODE-11007077-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (98, 'CODE-11007078-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (99, 'CODE-11007079-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (100, 'CODE-11007080-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (101, 'CODE-11007081-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (102, 'CODE-11007082-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (103, 'CODE-11007083-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (104, 'CODE-11007084-X', 'CC-CU-VM-BU-11-PL-S1-7', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (105, 'CODE-11008-X', 'CC-CI-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (106, 'CODE-11008085-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (107, 'CODE-11008086-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (108, 'CODE-11008087-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (109, 'CODE-11008088-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (110, 'CODE-11008089-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (111, 'CODE-11008090-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (112, 'CODE-11008091-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (113, 'CODE-11008092-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (114, 'CODE-11008093-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (115, 'CODE-11008094-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (116, 'CODE-11008095-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (117, 'CODE-11008096-X', 'CC-CU-VM-BU-11-PL-S2-8', 'UF');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (118, 'CODE-12009-X', 'CC-CI-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (119, 'CODE-12009097-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (120, 'CODE-12009098-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (121, 'CODE-12009099-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (122, 'CODE-12009100-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (123, 'CODE-12009101-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (124, 'CODE-12009102-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (125, 'CODE-12009103-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (126, 'CODE-12009104-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (127, 'CODE-12009105-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (128, 'CODE-12009106-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (129, 'CODE-12009107-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (130, 'CODE-12009108-X', 'CC-CU-VM-BU-12-PL-P1-9', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (131, 'CODE-12010-X', 'CC-CI-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (132, 'CODE-12010109-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (133, 'CODE-12010110-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (134, 'CODE-12010111-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (135, 'CODE-12010112-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (136, 'CODE-12010113-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (137, 'CODE-12010114-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (138, 'CODE-12010115-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (139, 'CODE-12010116-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (140, 'CODE-12010117-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (141, 'CODE-12010118-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (142, 'CODE-12010119-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (143, 'CODE-12010120-X', 'CC-CU-VM-BU-12-PL-P2-10', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (144, 'CODE-12011-X', 'CC-CI-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (145, 'CODE-12011121-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (146, 'CODE-12011122-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (147, 'CODE-12011123-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (148, 'CODE-12011124-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (149, 'CODE-12011125-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (150, 'CODE-12011126-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (151, 'CODE-12011127-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (152, 'CODE-12011128-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (153, 'CODE-12011129-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (154, 'CODE-12011130-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (155, 'CODE-12011131-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (156, 'CODE-12011132-X', 'CC-CU-VM-BU-12-PL-S1-11', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (157, 'CODE-12012-X', 'CC-CI-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (158, 'CODE-12012133-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (159, 'CODE-12012134-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (160, 'CODE-12012135-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (161, 'CODE-12012136-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (162, 'CODE-12012137-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (163, 'CODE-12012138-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (164, 'CODE-12012139-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (165, 'CODE-12012140-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (166, 'CODE-12012141-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (167, 'CODE-12012142-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (168, 'CODE-12012143-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (169, 'CODE-12012144-X', 'CC-CU-VM-BU-12-PL-S2-12', 'PEN');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (170, 'CODE-13013-X', 'CC-CI-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (171, 'CODE-13013145-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (172, 'CODE-13013146-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (173, 'CODE-13013147-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (174, 'CODE-13013148-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (175, 'CODE-13013149-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (176, 'CODE-13013150-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (177, 'CODE-13013151-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (178, 'CODE-13013152-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (179, 'CODE-13013153-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (180, 'CODE-13013154-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (181, 'CODE-13013155-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (182, 'CODE-13013156-X', 'CC-CU-VM-BU-13-PL-P1-13', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (183, 'CODE-13014-X', 'CC-CI-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (184, 'CODE-13014157-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (185, 'CODE-13014158-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (186, 'CODE-13014159-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (187, 'CODE-13014160-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (188, 'CODE-13014161-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (189, 'CODE-13014162-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (190, 'CODE-13014163-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (191, 'CODE-13014164-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (192, 'CODE-13014165-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (193, 'CODE-13014166-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (194, 'CODE-13014167-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (195, 'CODE-13014168-X', 'CC-CU-VM-BU-13-PL-P2-14', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (196, 'CODE-13015-X', 'CC-CI-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (197, 'CODE-13015169-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (198, 'CODE-13015170-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (199, 'CODE-13015171-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (200, 'CODE-13015172-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (201, 'CODE-13015173-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (202, 'CODE-13015174-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (203, 'CODE-13015175-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (204, 'CODE-13015176-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (205, 'CODE-13015177-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (206, 'CODE-13015178-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (207, 'CODE-13015179-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (208, 'CODE-13015180-X', 'CC-CU-VM-BU-13-PL-S1-15', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (209, 'CODE-13016-X', 'CC-CI-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (210, 'CODE-13016181-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (211, 'CODE-13016182-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (212, 'CODE-13016183-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (213, 'CODE-13016184-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (214, 'CODE-13016185-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (215, 'CODE-13016186-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (216, 'CODE-13016187-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (217, 'CODE-13016188-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (218, 'CODE-13016189-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (219, 'CODE-13016190-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (220, 'CODE-13016191-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');
INSERT INTO `collector`.`Cost_Centers` (`CC_Id`, `CC_Code`, `CC_Description`, `Cur_Code`) VALUES (221, 'CODE-13016192-X', 'CC-CU-VM-BU-13-PL-S2-16', 'COP');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Customers`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (1, 'DEFAULT', 1);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (2, 'SERTECHNO', 2);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (3, 'SERTECHNO CHILE', 3);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (4, 'SERTECHNO COLOMBIA', 4);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (5, 'SERTECHNO PERU', 5);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (6, 'EMTEC GROUP', 6);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (7, 'EMTEC CHILE', 7);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (8, 'EMTEC PERU', 8);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (9, 'EMTEC COLOMBIA', 9);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (10, 'Business Unit 10 - Corp', 10);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (11, 'Business Unit 11 - CL', 11);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (12, 'Business Unit 12 - PE', 12);
INSERT INTO `collector`.`Customers` (`Cus_Id`, `Cus_Name`, `CC_Id`) VALUES (13, 'Business Unit 13 - CO', 13);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`CIT_Generations`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`CIT_Generations` (`CIT_Generation`, `Value`) VALUES (0, 'Undefined');
INSERT INTO `collector`.`CIT_Generations` (`CIT_Generation`, `Value`) VALUES (1, 'Daemon (Automatic generation)');
INSERT INTO `collector`.`CIT_Generations` (`CIT_Generation`, `Value`) VALUES (2, 'Manual');
INSERT INTO `collector`.`CIT_Generations` (`CIT_Generation`, `Value`) VALUES (3, 'Montly');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Configuration_Items`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (1, 'DEFAULT-CI', 'DEFAULT-CI-UUID', 1, 1, DEFAULT, 1);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (2, 'VM-BU-10-PL-P1-1', 'UUID-BU-10-PL-P1-VM-1', 2, 14, DEFAULT, 10);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (3, 'VM-BU-10-PL-P2-2', 'UUID-BU-10-PL-P2-VM-2', 3, 20, DEFAULT, 10);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (4, 'VM-BU-10-PL-S1-3', 'UUID-BU-10-PL-S1-VM-3', 4, 26, DEFAULT, 10);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (5, 'VM-BU-10-PL-S2-4', 'UUID-BU-10-PL-S2-VM-4', 5, 32, DEFAULT, 10);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (6, 'VM-BU-11-PL-P1-5', 'UUID-BU-11-PL-P1-VM-5', 2, 38, DEFAULT, 11);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (7, 'VM-BU-11-PL-P2-6', 'UUID-BU-11-PL-P2-VM-6', 3, 44, DEFAULT, 11);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (8, 'VM-BU-11-PL-S1-7', 'UUID-BU-11-PL-S1-VM-7', 4, 50, DEFAULT, 11);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (9, 'VM-BU-11-PL-S2-8', 'UUID-BU-11-PL-S2-VM-8', 5, 56, DEFAULT, 11);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (10, 'VM-BU-12-PL-P1-9', 'UUID-BU-12-PL-P1-VM-9', 2, 62, DEFAULT, 12);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (11, 'VM-BU-12-PL-P2-10', 'UUID-BU-12-PL-P2-VM-10', 3, 68, DEFAULT, 12);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (12, 'VM-BU-12-PL-S1-11', 'UUID-BU-12-PL-S1-VM-11', 4, 74, DEFAULT, 12);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (13, 'VM-BU-12-PL-S2-12', 'UUID-BU-12-PL-S2-VM-12', 5, 80, DEFAULT, 12);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (14, 'VM-BU-13-PL-P1-13', 'UUID-BU-13-PL-P1-VM-13', 2, 86, DEFAULT, 13);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (15, 'VM-BU-13-PL-P2-14', 'UUID-BU-13-PL-P2-VM-14', 3, 92, DEFAULT, 13);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (16, 'VM-BU-13-PL-S1-15', 'UUID-BU-13-PL-S1-VM-15', 4, 98, DEFAULT, 13);
INSERT INTO `collector`.`Configuration_Items` (`CI_Id`, `CI_Name`, `CI_UUID`, `Pla_Id`, `CC_Id`, `CIT_Generation`, `Cus_Id`) VALUES (17, 'VM-BU-13-PL-S2-16', 'UUID-BU-13-PL-S2-VM-16', 5, 104, DEFAULT, 13);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`CU_Types`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`CU_Types` (`Typ_Code`, `Typ_Description`) VALUES ('NUL', 'DEFAULT');
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

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`CU_Operations`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('NONE', 'No Conversion', 1, 1);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('BTOKB', 'Byte to KB', 0, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('BTOMB', 'Byte to MB', 0, 1048576);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('BTOGB', 'Byte to GB', 0, 1073741824);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('KBTOB', 'Kilobyte to Byte', 1, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('KBTOMG', 'Kilobyte to MB', 0, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('KBTOGB', 'Kilobyte to GB', 0, 1048576);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MBTOB', 'Megabyte to Byte', 1, 1048576);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MBTOKB', 'Megabyte to KB', 1, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MBTOGB', 'Megabyte to GB', 0, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('GBTOB', 'Gigabyte to Bytes', 0, 1073741824);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('GBTOKB', 'Gigabyte to KB', NULL, 1048576);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('GBTOMB', 'Gigabyte to MB', NULL, 1024);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('HTOD', 'Hours to Days', 0, 24);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('HTOM', 'Hours to Months', 0, 720);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('DTOH', 'Days to Hours', 1, 24);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('DTOM', 'Days to Months', 0, 30);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MTOH', 'Months to Hours', 1, 720);
INSERT INTO `collector`.`CU_Operations` (`CU_Operations`, `Value`, `Is_Multiply`, `Factor`) VALUES ('MTOD', 'Months to Days', 1, 30);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Charge_Units`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (1, 1, 'DEFAULT-CU_Description', 'DEFAULT-CU_UUID', 1, 1, 0, 'NONE', 'NUL', 1);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (2, 2, 'VM-BU-10-PL-P1-1 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 15);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (3, 2, 'VM-BU-10-PL-P1-1 - Node', '', 1, 1, 1, 'NONE', 'NOD', 16);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (4, 2, 'VM-BU-10-PL-P1-1 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 17);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (5, 2, 'VM-BU-10-PL-P1-1 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 18);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (6, 2, 'VM-BU-10-PL-P1-1 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 19);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (7, 2, 'VM-BU-10-PL-P1-1 - Virtual Disk Drive', 'UUID-VM-BU-10-PL-P1-1-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 20);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (8, 2, 'VM-BU-10-PL-P1-1 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 21);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (9, 2, 'VM-BU-10-PL-P1-1 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 22);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (10, 2, 'VM-BU-10-PL-P1-1 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 23);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (11, 2, 'VM-BU-10-PL-P1-1 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 24);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (12, 2, 'VM-BU-10-PL-P1-1 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 25);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (13, 3, 'VM-BU-10-PL-P2-2 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 27);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (14, 3, 'VM-BU-10-PL-P2-2 - Node', '', 1, 1, 1, 'NONE', 'NOD', 28);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (15, 3, 'VM-BU-10-PL-P2-2 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 29);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (16, 3, 'VM-BU-10-PL-P2-2 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 30);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (17, 3, 'VM-BU-10-PL-P2-2 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 31);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (18, 3, 'VM-BU-10-PL-P2-2 - Virtual Disk Drive', 'UUID-VM-BU-10-PL-P2-2-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 32);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (19, 3, 'VM-BU-10-PL-P2-2 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 33);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (20, 3, 'VM-BU-10-PL-P2-2 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 34);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (21, 3, 'VM-BU-10-PL-P2-2 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 35);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (22, 3, 'VM-BU-10-PL-P2-2 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 36);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (23, 3, 'VM-BU-10-PL-P2-2 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 37);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (24, 4, 'VM-BU-10-PL-S1-3 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 39);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (25, 4, 'VM-BU-10-PL-S1-3 - Node', '', 1, 1, 1, 'NONE', 'NOD', 40);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (26, 4, 'VM-BU-10-PL-S1-3 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 41);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (27, 4, 'VM-BU-10-PL-S1-3 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 42);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (28, 4, 'VM-BU-10-PL-S1-3 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 43);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (29, 4, 'VM-BU-10-PL-S1-3 - Virtual Disk Drive', 'UUID-VM-BU-10-PL-S1-3-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 44);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (30, 4, 'VM-BU-10-PL-S1-3 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 45);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (31, 4, 'VM-BU-10-PL-S1-3 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 46);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (32, 4, 'VM-BU-10-PL-S1-3 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 47);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (33, 4, 'VM-BU-10-PL-S1-3 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 48);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (34, 4, 'VM-BU-10-PL-S1-3 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 49);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (35, 5, 'VM-BU-10-PL-S2-4 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 51);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (36, 5, 'VM-BU-10-PL-S2-4 - Node', '', 1, 1, 1, 'NONE', 'NOD', 52);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (37, 5, 'VM-BU-10-PL-S2-4 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 53);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (38, 5, 'VM-BU-10-PL-S2-4 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 54);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (39, 5, 'VM-BU-10-PL-S2-4 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 55);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (40, 5, 'VM-BU-10-PL-S2-4 - Virtual Disk Drive', 'UUID-VM-BU-10-PL-S2-4-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 56);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (41, 5, 'VM-BU-10-PL-S2-4 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 57);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (42, 5, 'VM-BU-10-PL-S2-4 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 58);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (43, 5, 'VM-BU-10-PL-S2-4 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 59);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (44, 5, 'VM-BU-10-PL-S2-4 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 60);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (45, 5, 'VM-BU-10-PL-S2-4 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 61);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (46, 6, 'VM-BU-11-PL-P1-5 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 63);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (47, 6, 'VM-BU-11-PL-P1-5 - Node', '', 1, 1, 1, 'NONE', 'NOD', 64);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (48, 6, 'VM-BU-11-PL-P1-5 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 65);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (49, 6, 'VM-BU-11-PL-P1-5 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 66);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (50, 6, 'VM-BU-11-PL-P1-5 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 67);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (51, 6, 'VM-BU-11-PL-P1-5 - Virtual Disk Drive', 'UUID-VM-BU-11-PL-P1-5-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 68);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (52, 6, 'VM-BU-11-PL-P1-5 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 69);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (53, 6, 'VM-BU-11-PL-P1-5 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 70);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (54, 6, 'VM-BU-11-PL-P1-5 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 71);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (55, 6, 'VM-BU-11-PL-P1-5 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 72);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (56, 6, 'VM-BU-11-PL-P1-5 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 73);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (57, 7, 'VM-BU-11-PL-P2-6 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 75);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (58, 7, 'VM-BU-11-PL-P2-6 - Node', '', 1, 1, 1, 'NONE', 'NOD', 76);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (59, 7, 'VM-BU-11-PL-P2-6 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 77);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (60, 7, 'VM-BU-11-PL-P2-6 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 78);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (61, 7, 'VM-BU-11-PL-P2-6 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 79);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (62, 7, 'VM-BU-11-PL-P2-6 - Virtual Disk Drive', 'UUID-VM-BU-11-PL-P2-6-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 80);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (63, 7, 'VM-BU-11-PL-P2-6 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 81);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (64, 7, 'VM-BU-11-PL-P2-6 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 82);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (65, 7, 'VM-BU-11-PL-P2-6 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 83);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (66, 7, 'VM-BU-11-PL-P2-6 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 84);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (67, 7, 'VM-BU-11-PL-P2-6 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 85);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (68, 8, 'VM-BU-11-PL-S1-7 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 87);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (69, 8, 'VM-BU-11-PL-S1-7 - Node', '', 1, 1, 1, 'NONE', 'NOD', 88);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (70, 8, 'VM-BU-11-PL-S1-7 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 89);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (71, 8, 'VM-BU-11-PL-S1-7 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 90);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (72, 8, 'VM-BU-11-PL-S1-7 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 91);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (73, 8, 'VM-BU-11-PL-S1-7 - Virtual Disk Drive', 'UUID-VM-BU-11-PL-S1-7-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 92);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (74, 8, 'VM-BU-11-PL-S1-7 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 93);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (75, 8, 'VM-BU-11-PL-S1-7 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 94);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (76, 8, 'VM-BU-11-PL-S1-7 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 95);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (77, 8, 'VM-BU-11-PL-S1-7 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 96);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (78, 8, 'VM-BU-11-PL-S1-7 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 97);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (79, 9, 'VM-BU-11-PL-S2-8 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 99);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (80, 9, 'VM-BU-11-PL-S2-8 - Node', '', 1, 1, 1, 'NONE', 'NOD', 100);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (81, 9, 'VM-BU-11-PL-S2-8 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 101);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (82, 9, 'VM-BU-11-PL-S2-8 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 102);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (83, 9, 'VM-BU-11-PL-S2-8 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 103);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (84, 9, 'VM-BU-11-PL-S2-8 - Virtual Disk Drive', 'UUID-VM-BU-11-PL-S2-8-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 104);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (85, 9, 'VM-BU-11-PL-S2-8 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 105);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (86, 9, 'VM-BU-11-PL-S2-8 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 106);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (87, 9, 'VM-BU-11-PL-S2-8 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 107);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (88, 9, 'VM-BU-11-PL-S2-8 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 108);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (89, 9, 'VM-BU-11-PL-S2-8 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 109);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (90, 10, 'VM-BU-12-PL-P1-9 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 111);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (91, 10, 'VM-BU-12-PL-P1-9 - Node', '', 1, 1, 1, 'NONE', 'NOD', 112);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (92, 10, 'VM-BU-12-PL-P1-9 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 113);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (93, 10, 'VM-BU-12-PL-P1-9 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 114);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (94, 10, 'VM-BU-12-PL-P1-9 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 115);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (95, 10, 'VM-BU-12-PL-P1-9 - Virtual Disk Drive', 'UUID-VM-BU-12-PL-P1-9-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 116);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (96, 10, 'VM-BU-12-PL-P1-9 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 117);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (97, 10, 'VM-BU-12-PL-P1-9 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 118);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (98, 10, 'VM-BU-12-PL-P1-9 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 119);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (99, 10, 'VM-BU-12-PL-P1-9 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 120);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (100, 10, 'VM-BU-12-PL-P1-9 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 121);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (101, 11, 'VM-BU-12-PL-P2-10 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 123);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (102, 11, 'VM-BU-12-PL-P2-10 - Node', '', 1, 1, 1, 'NONE', 'NOD', 124);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (103, 11, 'VM-BU-12-PL-P2-10 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 125);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (104, 11, 'VM-BU-12-PL-P2-10 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 126);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (105, 11, 'VM-BU-12-PL-P2-10 - RAM Unit', '', 1, 1, 2, 'NONE', 'RAM', 127);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (106, 11, 'VM-BU-12-PL-P2-10 - Virtual Disk Drive', 'UUID-VM-BU-12-PL-P2-10-Virtual Disk Drive', 1, 1, 40, 'NONE', 'DSK', 128);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (107, 11, 'VM-BU-12-PL-P2-10 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 129);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (108, 11, 'VM-BU-12-PL-P2-10 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 130);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (109, 11, 'VM-BU-12-PL-P2-10 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 131);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (110, 11, 'VM-BU-12-PL-P2-10 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 132);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (111, 11, 'VM-BU-12-PL-P2-10 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 133);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (112, 12, 'VM-BU-12-PL-S1-11 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 135);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (113, 12, 'VM-BU-12-PL-S1-11 - Node', '', 1, 1, 1, 'NONE', 'NOD', 136);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (114, 12, 'VM-BU-12-PL-S1-11 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 137);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (115, 12, 'VM-BU-12-PL-S1-11 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 138);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (116, 12, 'VM-BU-12-PL-S1-11 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 139);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (117, 12, 'VM-BU-12-PL-S1-11 - Virtual Disk Drive', 'UUID-VM-BU-12-PL-S1-11-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 140);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (118, 12, 'VM-BU-12-PL-S1-11 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 141);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (119, 12, 'VM-BU-12-PL-S1-11 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 142);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (120, 12, 'VM-BU-12-PL-S1-11 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 143);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (121, 12, 'VM-BU-12-PL-S1-11 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 144);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (122, 12, 'VM-BU-12-PL-S1-11 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 145);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (123, 13, 'VM-BU-12-PL-S2-12 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 147);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (124, 13, 'VM-BU-12-PL-S2-12 - Node', '', 1, 1, 1, 'NONE', 'NOD', 148);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (125, 13, 'VM-BU-12-PL-S2-12 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 149);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (126, 13, 'VM-BU-12-PL-S2-12 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 150);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (127, 13, 'VM-BU-12-PL-S2-12 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 151);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (128, 13, 'VM-BU-12-PL-S2-12 - Virtual Disk Drive', 'UUID-VM-BU-12-PL-S2-12-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 152);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (129, 13, 'VM-BU-12-PL-S2-12 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 153);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (130, 13, 'VM-BU-12-PL-S2-12 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 154);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (131, 13, 'VM-BU-12-PL-S2-12 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 155);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (132, 13, 'VM-BU-12-PL-S2-12 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 156);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (133, 13, 'VM-BU-12-PL-S2-12 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 157);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (134, 14, 'VM-BU-13-PL-P1-13 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 159);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (135, 14, 'VM-BU-13-PL-P1-13 - Node', '', 1, 1, 1, 'NONE', 'NOD', 160);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (136, 14, 'VM-BU-13-PL-P1-13 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 161);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (137, 14, 'VM-BU-13-PL-P1-13 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 162);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (138, 14, 'VM-BU-13-PL-P1-13 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 163);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (139, 14, 'VM-BU-13-PL-P1-13 - Virtual Disk Drive', 'UUID-VM-BU-13-PL-P1-13-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 164);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (140, 14, 'VM-BU-13-PL-P1-13 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 165);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (141, 14, 'VM-BU-13-PL-P1-13 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 166);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (142, 14, 'VM-BU-13-PL-P1-13 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 167);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (143, 14, 'VM-BU-13-PL-P1-13 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 168);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (144, 14, 'VM-BU-13-PL-P1-13 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 169);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (145, 15, 'VM-BU-13-PL-P2-14 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 171);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (146, 15, 'VM-BU-13-PL-P2-14 - Node', '', 1, 1, 1, 'NONE', 'NOD', 172);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (147, 15, 'VM-BU-13-PL-P2-14 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 173);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (148, 15, 'VM-BU-13-PL-P2-14 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 174);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (149, 15, 'VM-BU-13-PL-P2-14 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 175);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (150, 15, 'VM-BU-13-PL-P2-14 - Virtual Disk Drive', 'UUID-VM-BU-13-PL-P2-14-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 176);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (151, 15, 'VM-BU-13-PL-P2-14 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 177);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (152, 15, 'VM-BU-13-PL-P2-14 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 178);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (153, 15, 'VM-BU-13-PL-P2-14 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 179);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (154, 15, 'VM-BU-13-PL-P2-14 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 180);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (155, 15, 'VM-BU-13-PL-P2-14 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 181);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (156, 16, 'VM-BU-13-PL-S1-15 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 183);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (157, 16, 'VM-BU-13-PL-S1-15 - Node', '', 1, 1, 1, 'NONE', 'NOD', 184);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (158, 16, 'VM-BU-13-PL-S1-15 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 185);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (159, 16, 'VM-BU-13-PL-S1-15 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 186);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (160, 16, 'VM-BU-13-PL-S1-15 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 187);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (161, 16, 'VM-BU-13-PL-S1-15 - Virtual Disk Drive', 'UUID-VM-BU-13-PL-S1-15-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 188);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (162, 16, 'VM-BU-13-PL-S1-15 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 189);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (163, 16, 'VM-BU-13-PL-S1-15 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 190);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (164, 16, 'VM-BU-13-PL-S1-15 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 191);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (165, 16, 'VM-BU-13-PL-S1-15 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 192);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (166, 16, 'VM-BU-13-PL-S1-15 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 193);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (167, 17, 'VM-BU-13-PL-S2-16 - Cluster', '', 1, 1, 1, 'NONE', 'CLU', 195);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (168, 17, 'VM-BU-13-PL-S2-16 - Node', '', 1, 1, 1, 'NONE', 'NOD', 196);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (169, 17, 'VM-BU-13-PL-S2-16 - Virtual Machine', '', 1, 1, 1, 'NONE', 'VM', 197);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (170, 17, 'VM-BU-13-PL-S2-16 - CPU Unit', '', 1, 1, 1, 'NONE', 'CPU', 198);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (171, 17, 'VM-BU-13-PL-S2-16 - RAM Unit', '', 1, 1, 2, 'KBTOGB', 'RAM', 199);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (172, 17, 'VM-BU-13-PL-S2-16 - Virtual Disk Drive', 'UUID-VM-BU-13-PL-S2-16-Virtual Disk Drive', 1, 1, 40, 'BTOGB', 'DSK', 200);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (173, 17, 'VM-BU-13-PL-S2-16 - Virtual CDROM', '', 1, 1, 1, 'NONE', 'CDR', 201);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (174, 17, 'VM-BU-13-PL-S2-16 - VGA Console', '', 1, 1, 1, 'NONE', 'VGA', 202);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (175, 17, 'VM-BU-13-PL-S2-16 - Cores per CPU', '', 1, 1, 2, 'NONE', 'COR', 203);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (176, 17, 'VM-BU-13-PL-S2-16 - Housing', '', 1, 1, 1, 'NONE', 'HOU', 204);
INSERT INTO `collector`.`Charge_Units` (`CU_Id`, `CI_Id`, `CU_Description`, `CU_UUID`, `CU_Is_Billeable`, `CU_Is_Always_Billeable`, `CU_Quantity`, `CU_Operations`, `Typ_Code`, `CC_Id`) VALUES (177, 17, 'VM-BU-13-PL-S2-16 - Hosting', '', 1, 1, 1, 'NONE', 'HOS', 205);

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
INSERT INTO `collector`.`Rat_Periods` (`Rat_Period`, `Value`) VALUES (0, 'Undefined');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Rates`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (1, 'NUL', 1, 1, 1, 1, 0.0, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (2, 'CLU', 1, 1, 1, 1, 1000.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (3, 'NOD', 1, 1, 1, 1, 500.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (4, 'VM', 1, 1, 1, 1, 100.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (5, 'CPU', 1, 1, 1, 1, 10.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (6, 'RAM', 1, 1, 1, 1, 5.000000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (7, 'DSK', 1, 1, 1, 1, 3.000000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (8, 'CDR', 1, 1, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (9, 'VGA', 1, 1, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (10, 'COR', 1, 1, 1, 1, 1.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (11, 'HOU', 1, 1, 1, 1, 30.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (12, 'HOS', 1, 1, 1, 1, 15.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (13, 'CLU', 10, 1, 1, 1, 900.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (14, 'NOD', 10, 1, 1, 1, 450.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (15, 'VM', 10, 1, 1, 1, 90.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (16, 'CPU', 10, 1, 1, 1, 9.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (17, 'RAM', 10, 1, 1, 1, 4.500000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (18, 'DSK', 10, 1, 1, 1, 2.700000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (19, 'CDR', 10, 1, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (20, 'VGA', 10, 1, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (21, 'COR', 10, 1, 1, 1, 0.900000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (22, 'HOU', 10, 1, 1, 1, 27.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (23, 'HOS', 10, 1, 1, 1, 13.500000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (24, 'CLU', 11, 1, 1, 1, 21.915360, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (25, 'NOD', 11, 1, 1, 1, 10.957680, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (26, 'VM', 11, 1, 1, 1, 2.191536, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (27, 'CPU', 11, 1, 1, 1, 0.219154, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (28, 'RAM', 11, 1, 1, 1, 0.109577, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (29, 'DSK', 11, 1, 1, 1, 0.065746, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (30, 'CDR', 11, 1, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (31, 'VGA', 11, 1, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (32, 'COR', 11, 1, 1, 1, 0.021915, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (33, 'HOU', 11, 1, 1, 1, 0.657461, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (34, 'HOS', 11, 1, 1, 1, 0.328730, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (35, 'CLU', 12, 1, 1, 1, 2816.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (36, 'NOD', 12, 1, 1, 1, 1408.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (37, 'VM', 12, 1, 1, 1, 281.600000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (38, 'CPU', 12, 1, 1, 1, 28.160000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (39, 'RAM', 12, 1, 1, 1, 14.080000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (40, 'DSK', 12, 1, 1, 1, 8.448000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (41, 'CDR', 12, 1, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (42, 'VGA', 12, 1, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (43, 'COR', 12, 1, 1, 1, 2.816000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (44, 'HOU', 12, 1, 1, 1, 84.480000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (45, 'HOS', 12, 1, 1, 1, 42.240000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (46, 'CLU', 13, 1, 1, 1, 5829.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (47, 'NOD', 13, 1, 1, 1, 2914.500000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (48, 'VM', 13, 1, 1, 1, 582.900000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (49, 'CPU', 13, 1, 1, 1, 58.290000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (50, 'RAM', 13, 1, 1, 1, 29.145000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (51, 'DSK', 13, 1, 1, 1, 17.487000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (52, 'CDR', 13, 1, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (53, 'VGA', 13, 1, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (54, 'COR', 13, 1, 1, 1, 5.829000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (55, 'HOU', 13, 1, 1, 1, 174.870000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (56, 'HOS', 13, 1, 1, 1, 87.435000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (57, 'CLU', 10, 2, 1, 1, 840.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (58, 'CLU', 10, 3, 1, 1, 810.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (59, 'CLU', 10, 4, 1, 1, 780.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (60, 'CLU', 10, 5, 1, 1, 750.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (61, 'NOD', 10, 2, 1, 1, 420.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (62, 'NOD', 10, 3, 1, 1, 405.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (63, 'NOD', 10, 4, 1, 1, 390.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (64, 'NOD', 10, 5, 1, 1, 375.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (65, 'VM', 10, 2, 1, 1, 84.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (66, 'VM', 10, 3, 1, 1, 81.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (67, 'VM', 10, 4, 1, 1, 78.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (68, 'VM', 10, 5, 1, 1, 75.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (69, 'CPU', 10, 2, 1, 1, 8.400000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (70, 'CPU', 10, 3, 1, 1, 8.100000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (71, 'CPU', 10, 4, 1, 1, 7.800000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (72, 'CPU', 10, 5, 1, 1, 7.500000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (73, 'RAM', 10, 2, 1, 1, 4.200000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (74, 'RAM', 10, 3, 1, 1, 4.050000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (75, 'RAM', 10, 4, 1, 1, 3.900000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (76, 'RAM', 10, 5, 1, 1, 3.750000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (77, 'DSK', 10, 2, 1, 1, 2.520000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (78, 'DSK', 10, 3, 1, 1, 2.430000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (79, 'DSK', 10, 4, 1, 1, 2.340000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (80, 'DSK', 10, 5, 1, 1, 2.250000, 'USD', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (81, 'CDR', 10, 2, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (82, 'CDR', 10, 3, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (83, 'CDR', 10, 4, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (84, 'CDR', 10, 5, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (85, 'VGA', 10, 2, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (86, 'VGA', 10, 3, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (87, 'VGA', 10, 4, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (88, 'VGA', 10, 5, 1, 1, 0.000000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (89, 'COR', 10, 2, 1, 1, 0.840000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (90, 'COR', 10, 3, 1, 1, 0.810000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (91, 'COR', 10, 4, 1, 1, 0.780000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (92, 'COR', 10, 5, 1, 1, 0.750000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (93, 'HOU', 10, 2, 1, 1, 25.200000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (94, 'HOU', 10, 3, 1, 1, 24.300000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (95, 'HOU', 10, 4, 1, 1, 23.400000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (96, 'HOU', 10, 5, 1, 1, 22.500000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (97, 'HOS', 10, 2, 1, 1, 12.600000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (98, 'HOS', 10, 3, 1, 1, 12.150000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (99, 'HOS', 10, 4, 1, 1, 11.700000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (100, 'HOS', 10, 5, 1, 1, 11.250000, 'USD', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (101, 'CLU', 11, 2, 1, 1, 20.437920, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (102, 'CLU', 11, 3, 1, 1, 19.699200, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (103, 'CLU', 11, 4, 1, 1, 18.960480, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (104, 'CLU', 11, 5, 1, 1, 18.221760, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (105, 'NOD', 11, 2, 1, 1, 10.218960, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (106, 'NOD', 11, 3, 1, 1, 9.849600, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (107, 'NOD', 11, 4, 1, 1, 9.480240, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (108, 'NOD', 11, 5, 1, 1, 9.110880, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (109, 'VM', 11, 2, 1, 1, 2.043792, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (110, 'VM', 11, 3, 1, 1, 1.969920, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (111, 'VM', 11, 4, 1, 1, 1.896048, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (112, 'VM', 11, 5, 1, 1, 1.822176, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (113, 'CPU', 11, 2, 1, 1, 0.204379, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (114, 'CPU', 11, 3, 1, 1, 0.196992, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (115, 'CPU', 11, 4, 1, 1, 0.189605, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (116, 'CPU', 11, 5, 1, 1, 0.182218, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (117, 'RAM', 11, 2, 1, 1, 0.102190, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (118, 'RAM', 11, 3, 1, 1, 0.098496, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (119, 'RAM', 11, 4, 1, 1, 0.094802, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (120, 'RAM', 11, 5, 1, 1, 0.091109, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (121, 'DSK', 11, 2, 1, 1, 0.061314, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (122, 'DSK', 11, 3, 1, 1, 0.059098, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (123, 'DSK', 11, 4, 1, 1, 0.056881, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (124, 'DSK', 11, 5, 1, 1, 0.054665, 'UF', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (125, 'CDR', 11, 2, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (126, 'CDR', 11, 3, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (127, 'CDR', 11, 4, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (128, 'CDR', 11, 5, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (129, 'VGA', 11, 2, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (130, 'VGA', 11, 3, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (131, 'VGA', 11, 4, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (132, 'VGA', 11, 5, 1, 1, 0.000000, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (133, 'COR', 11, 2, 1, 1, 0.020438, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (134, 'COR', 11, 3, 1, 1, 0.019699, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (135, 'COR', 11, 4, 1, 1, 0.018960, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (136, 'COR', 11, 5, 1, 1, 0.018222, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (137, 'HOU', 11, 2, 1, 1, 0.613138, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (138, 'HOU', 11, 3, 1, 1, 0.590976, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (139, 'HOU', 11, 4, 1, 1, 0.568814, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (140, 'HOU', 11, 5, 1, 1, 0.546653, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (141, 'HOS', 11, 2, 1, 1, 0.306569, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (142, 'HOS', 11, 3, 1, 1, 0.295488, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (143, 'HOS', 11, 4, 1, 1, 0.284407, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (144, 'HOS', 11, 5, 1, 1, 0.273326, 'UF', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (145, 'CLU', 12, 2, 1, 1, 2624.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (146, 'CLU', 12, 3, 1, 1, 2528.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (147, 'CLU', 12, 4, 1, 1, 2432.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (148, 'CLU', 12, 5, 1, 1, 2336.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (149, 'NOD', 12, 2, 1, 1, 1312.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (150, 'NOD', 12, 3, 1, 1, 1264.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (151, 'NOD', 12, 4, 1, 1, 1216.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (152, 'NOD', 12, 5, 1, 1, 1168.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (153, 'VM', 12, 2, 1, 1, 262.400000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (154, 'VM', 12, 3, 1, 1, 252.800000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (155, 'VM', 12, 4, 1, 1, 243.200000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (156, 'VM', 12, 5, 1, 1, 233.600000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (157, 'CPU', 12, 2, 1, 1, 26.240000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (158, 'CPU', 12, 3, 1, 1, 25.280000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (159, 'CPU', 12, 4, 1, 1, 24.320000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (160, 'CPU', 12, 5, 1, 1, 23.360000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (161, 'RAM', 12, 2, 1, 1, 13.120000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (162, 'RAM', 12, 3, 1, 1, 12.640000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (163, 'RAM', 12, 4, 1, 1, 12.160000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (164, 'RAM', 12, 5, 1, 1, 11.680000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (165, 'DSK', 12, 2, 1, 1, 7.872000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (166, 'DSK', 12, 3, 1, 1, 7.584000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (167, 'DSK', 12, 4, 1, 1, 7.296000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (168, 'DSK', 12, 5, 1, 1, 7.008000, 'PEN', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (169, 'CDR', 12, 2, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (170, 'CDR', 12, 3, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (171, 'CDR', 12, 4, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (172, 'CDR', 12, 5, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (173, 'VGA', 12, 2, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (174, 'VGA', 12, 3, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (175, 'VGA', 12, 4, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (176, 'VGA', 12, 5, 1, 1, 0.000000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (177, 'COR', 12, 2, 1, 1, 2.624000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (178, 'COR', 12, 3, 1, 1, 2.528000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (179, 'COR', 12, 4, 1, 1, 2.432000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (180, 'COR', 12, 5, 1, 1, 2.336000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (181, 'HOU', 12, 2, 1, 1, 78.720000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (182, 'HOU', 12, 3, 1, 1, 75.840000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (183, 'HOU', 12, 4, 1, 1, 72.960000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (184, 'HOU', 12, 5, 1, 1, 70.080000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (185, 'HOS', 12, 2, 1, 1, 39.360000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (186, 'HOS', 12, 3, 1, 1, 37.920000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (187, 'HOS', 12, 4, 1, 1, 36.480000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (188, 'HOS', 12, 5, 1, 1, 35.040000, 'PEN', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (189, 'CLU', 13, 2, 1, 1, 5427.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (190, 'CLU', 13, 3, 1, 1, 5226.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (191, 'CLU', 13, 4, 1, 1, 5025.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (192, 'CLU', 13, 5, 1, 1, 4824.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (193, 'NOD', 13, 2, 1, 1, 2713.500000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (194, 'NOD', 13, 3, 1, 1, 2613.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (195, 'NOD', 13, 4, 1, 1, 2512.500000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (196, 'NOD', 13, 5, 1, 1, 2412.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (197, 'VM', 13, 2, 1, 1, 542.700000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (198, 'VM', 13, 3, 1, 1, 522.600000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (199, 'VM', 13, 4, 1, 1, 502.500000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (200, 'VM', 13, 5, 1, 1, 482.400000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (201, 'CPU', 13, 2, 1, 1, 54.270000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (202, 'CPU', 13, 3, 1, 1, 52.260000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (203, 'CPU', 13, 4, 1, 1, 50.250000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (204, 'CPU', 13, 5, 1, 1, 48.240000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (205, 'RAM', 13, 2, 1, 1, 27.135000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (206, 'RAM', 13, 3, 1, 1, 26.130000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (207, 'RAM', 13, 4, 1, 1, 25.125000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (208, 'RAM', 13, 5, 1, 1, 24.120000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (209, 'DSK', 13, 2, 1, 1, 16.281000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (210, 'DSK', 13, 3, 1, 1, 15.678000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (211, 'DSK', 13, 4, 1, 1, 15.075000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (212, 'DSK', 13, 5, 1, 1, 14.472000, 'COP', 'GB', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (213, 'CDR', 13, 2, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (214, 'CDR', 13, 3, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (215, 'CDR', 13, 4, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (216, 'CDR', 13, 5, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (217, 'VGA', 13, 2, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (218, 'VGA', 13, 3, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (219, 'VGA', 13, 4, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (220, 'VGA', 13, 5, 1, 1, 0.000000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (221, 'COR', 13, 2, 1, 1, 5.427000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (222, 'COR', 13, 3, 1, 1, 5.226000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (223, 'COR', 13, 4, 1, 1, 5.025000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (224, 'COR', 13, 5, 1, 1, 4.824000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (225, 'HOU', 13, 2, 1, 1, 162.810000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (226, 'HOU', 13, 3, 1, 1, 156.780000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (227, 'HOU', 13, 4, 1, 1, 150.750000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (228, 'HOU', 13, 5, 1, 1, 144.720000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (229, 'HOS', 13, 2, 1, 1, 81.405000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (230, 'HOS', 13, 3, 1, 1, 78.390000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (231, 'HOS', 13, 4, 1, 1, 75.375000, 'COP', 'UNT', 1);
INSERT INTO `collector`.`Rates` (`Rat_Id`, `Typ_Code`, `Cus_Id`, `Pla_Id`, `CC_Id`, `CU_Id`, `Rat_Price`, `Cur_Code`, `MU_Code`, `Rat_Period`) VALUES (232, 'HOS', 13, 5, 1, 1, 72.360000, 'COP', 'UNT', 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`CIT_Statuses`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (0, 'Undefined');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (1, 'Created, Pending Approval');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (2, 'Claimed');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (3, 'Rejected');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (4, 'Approved');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (5, 'Billed');
INSERT INTO `collector`.`CIT_Statuses` (`CIT_Status`, `Value`) VALUES (6, 'Paid');

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Charge_Items`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (2, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (3, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (4, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (5, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (6, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (7, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (8, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (9, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (10, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (11, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (12, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (13, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (14, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (15, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (16, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (17, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (18, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (19, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (20, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (21, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (22, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (23, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (24, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (25, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (26, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (27, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (28, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (29, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (30, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (31, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (32, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (33, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (34, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (35, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (36, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (37, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (38, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (39, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (40, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (41, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (42, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (43, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (44, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (45, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (46, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (47, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (48, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (49, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (50, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (51, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (52, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (53, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (54, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (55, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (56, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (57, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (58, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (59, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (60, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (61, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (62, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (63, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (64, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (65, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (66, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (67, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (68, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (69, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (70, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (71, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (72, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (73, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (74, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (75, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (76, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (77, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (78, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (79, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (80, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (81, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (82, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (83, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (84, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (85, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (86, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (87, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (88, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (89, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (90, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (91, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (92, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (93, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (94, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (95, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (96, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (97, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (98, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (99, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (100, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (101, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (102, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (103, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (104, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (105, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (106, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (107, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (108, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (109, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (110, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (111, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (112, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (113, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (114, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (115, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (116, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (117, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (118, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (119, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (120, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (121, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (122, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (123, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (124, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (125, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (126, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (127, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (128, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (129, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (130, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (131, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (132, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (133, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (134, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (135, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (136, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (137, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (138, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (139, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (140, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (141, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (142, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (143, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (144, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (145, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (146, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (147, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (148, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (149, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (150, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (151, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (152, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (153, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (154, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (155, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (156, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (157, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (158, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (159, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (160, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (161, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (162, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (163, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (164, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (165, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (166, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (167, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (168, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (169, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (170, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (171, '2018-10-24', '13:45:23', 2097152, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (172, '2018-10-24', '13:45:23', 42949672960, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (173, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (174, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (175, '2018-10-24', '13:45:23', 2, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (176, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);
INSERT INTO `collector`.`Charge_Items` (`CU_Id`, `CIT_Date`, `CIT_Time`, `CIT_Quantity`, `CIT_Status`, `CIT_Is_Active`, `Charge_Itemscol`) VALUES (177, '2018-10-24', '13:45:23', 1, DEFAULT, 1, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `collector`.`Exchange_Rates`
-- -----------------------------------------------------
START TRANSACTION;
USE `collector`;
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (1, 'USD', 1, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'EUR', 1.3, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'CLP', 0.001538, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'UF', 41.71, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'PEN', 0.312500, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'COP', 0.001000, '2018-01-01');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'EUR', 1.35, '2018-09-15');
INSERT INTO `collector`.`Exchange_Rates` (`ER_Id`, `Cur_Code`, `ER_Factor`, `ER_Date`) VALUES (0, 'CLP', 0.00151515, '2018-09-15');

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

