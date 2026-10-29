-- -----------------------------------------------------
-- Schema swolesociety
-- Project Group 8 Members: Gabrielle Abdon, Madalyne Cross
-- -----------------------------------------------------

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

--
-- Table structure for table `MembershipTypes`
--

DROP TABLE IF EXISTS `MembershipTypes`;
CREATE TABLE `MembershipTypes` (
  `membership_type_id` int NOT NULL AUTO_INCREMENT,
  `membership_name` varchar(50) NOT NULL,
  `attendance_limit` int NOT NULL COMMENT '-1 is unlimited',
  PRIMARY KEY (`membership_type_id`),
  UNIQUE KEY `membership_name_UNIQUE` (`membership_name`)
);

--
-- Table structure for table `Members`
--

DROP TABLE IF EXISTS `Members`;
CREATE TABLE `Members` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `member_email` varchar(100) NOT NULL,
  `member_first_name` varchar(45) NOT NULL,
  `member_last_name` varchar(45) NOT NULL,
  `membership_start_date` date NOT NULL,
  `membership_end_date` date DEFAULT NULL,
  `member_street` varchar(50) DEFAULT NULL,
  `member_city` varchar(50) DEFAULT NULL,
  `member_state` varchar(50) DEFAULT NULL,
  `member_zip` char(5) DEFAULT NULL,
  `member_phone` varchar(10) NOT NULL,
  `membership_type_id` int NOT NULL,
  PRIMARY KEY (`member_id`),
  UNIQUE KEY `email_UNIQUE` (`member_email`),
  KEY `fk_Members_MembershipTypes1_idx` (`membership_type_id`),
  CONSTRAINT `fk_Members_MembershipTypes1` FOREIGN KEY (`membership_type_id`) REFERENCES `MembershipTypes` (`membership_type_id`)
  ON DELETE CASCADE
);

--
-- Table structure for table `Coaches`
--

DROP TABLE IF EXISTS `Coaches`;
CREATE TABLE `Coaches` (
  `coach_id` int NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL,
  PRIMARY KEY (`coach_id`),
  KEY `fk_Coaches_Members1_idx` (`member_id`),
  CONSTRAINT `fk_Coaches_Members1` FOREIGN KEY (`member_id`) REFERENCES `Members` (`member_id`)
  ON DELETE CASCADE
);

--
-- Table structure for table `ClassTypes`
--

DROP TABLE IF EXISTS `ClassTypes`;
CREATE TABLE `ClassTypes` (
  `class_type_id` int NOT NULL AUTO_INCREMENT,
  `class_type_name` varchar(50) NOT NULL,
  PRIMARY KEY (`class_type_id`)
);

--
-- Table structure for table `Classes`
--

DROP TABLE IF EXISTS `Classes`;
CREATE TABLE `Classes` (
  `class_id` int NOT NULL AUTO_INCREMENT,
  `class_name` varchar(100) NOT NULL,
  `class_duration_min` int NOT NULL,
  `class_max_capacity` int NOT NULL,
  `class_date_time` DATETIME NOT NULL,
  `class_type_id` int NOT NULL,
  `coach_id` int NOT NULL,
  PRIMARY KEY (`class_id`),
  KEY `fk_Programs_Coaches1_idx` (`coach_id`),
  KEY `fk_Programs_ProgramType1_idx` (`class_type_id`),
  CONSTRAINT `fk_Programs_Coaches1` FOREIGN KEY (`coach_id`) REFERENCES `Coaches` (`coach_id`)
  ON DELETE CASCADE,
  CONSTRAINT `fk_Programs_ProgramType1` FOREIGN KEY (`class_type_id`) REFERENCES `ClassTypes` (`class_type_id`)
  ON DELETE CASCADE
);

--
-- Table structure for table `ClassEnrollments`
--

DROP TABLE IF EXISTS `ClassEnrollments`;
CREATE TABLE `ClassEnrollments` (
  `class_enrollment_id` int NOT NULL AUTO_INCREMENT,
  `class_id` int NOT NULL,
  `member_id` int NOT NULL,
  PRIMARY KEY (`class_enrollment_id`),
  UNIQUE KEY `classID_memberID_UNIQUE` (`class_id`, `member_id`),
  KEY `fk_Members_has_Programs_Programs1_idx` (`class_id`),
  KEY `fk_Members_has_Programs_Members1_idx` (`member_id`),
  CONSTRAINT `fk_Members_has_Programs_Members1` FOREIGN KEY (`member_id`) REFERENCES `Members` (`member_id`)
  ON DELETE CASCADE,
  CONSTRAINT `fk_Members_has_Programs_Programs1` FOREIGN KEY (`class_id`) REFERENCES `Classes` (`class_id`)
  ON DELETE CASCADE
);

-- SAMPLE DATA

INSERT INTO ClassTypes 
(class_type_name)
VALUES
('HIIT'),
('Olympic Lifting'),
('Mobility');

INSERT INTO MembershipTypes 
(membership_name, attendance_limit)
VALUES
('Basic', 2),
('Plus', 4),
('Unlimited', -1);

INSERT INTO Members
(
    member_email,
    member_first_name,
    member_last_name,
    membership_start_date,
    member_street,
    member_city,
    member_state,
    member_zip,
    member_phone,
    membership_type_id
)
VALUES
(
    'michelletantan@gmail.com',
    'Michelle',
    'Tanner',
    '2024-01-03',
    '1709 Broderick St',
    'San Francisco',
    'CA',
    '94115',
    '4151234567',
    2
),
(
    'ted@swolesociety.com',
    'Ted',
    'Mosby',
    '2022-04-20',
    '521 W 82nd St Apt 4C',
    'San Francisco',
    'CA',
    '94201',
    '4155555555',
    3
),
(
    'bob@swolesociety.com',
    'Bob',
    'Saget',
    '2020-01-01',
    'Wander Lane',
    'San Francisco',
    'CA',
    '94201',
    '5555555555',
    1
);


INSERT INTO Coaches
(
    member_id
)
VALUES
(
    1
),
(
    2
),
(
    3
);

INSERT INTO Classes 
(
    class_name,
    class_duration_min,
    class_max_capacity,
    class_date_time,
    class_type_id,
    coach_id
)
VALUES 
(
	'Morning Mobility',
    60,
    5,
    '2026-12-01 09:00:00',
    3,
    1
), 
(
	'Evening Mobility',
    60,
    5,
    '2026-12-01 18:00:00',
    3,
    1
),
(
	'Morning Olympic Lifting',
    60,
    5,
    '2026-12-02 09:00:00',
    2,
    2
);

INSERT INTO ClassEnrollments
(
  class_id,
  member_id
)
VALUES
(
  1,
  2
),
(
  2,
  3
),
(
  3,
  2
);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;

-- Reworked from MySql Workbench Dump