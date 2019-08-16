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
  `CC_Id` INT NOT NULL,
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
  CONSTRAINT `fk_Charge_Units_Cost_Centers1`
    FOREIGN KEY (`CC_Id`)
    REFERENCES `collector`.`Cost_Centers` (`CC_Id`)
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
CREATE INDEX `fk_Charge_Units_Cost_Centers1_idx` ON `collector`.`Charge_Units` (`CC_Id` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_CU_Operations1_idx` ON `collector`.`Charge_Units` (`CU_Operation` ASC) VISIBLE;

SHOW WARNINGS;
CREATE INDEX `fk_Charge_Units_CIT_Generations1_idx` ON `collector`.`Charge_Units` (`CIT_Generation` ASC) VISIBLE;

SHOW WARNINGS;
