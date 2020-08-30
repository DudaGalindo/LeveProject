-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: datacamp
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cursos`
--

DROP TABLE IF EXISTS `Cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cursos` (
  `ID` int(25) DEFAULT NULL,
  `course_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cursos`
--

LOCK TABLES `Cursos` WRITE;
/*!40000 ALTER TABLE `Cursos` DISABLE KEYS */;
INSERT INTO `Cursos` VALUES (1,'Administração'),(2,'Ciências Contábeis'),(3,'Engenharia'),(4,'Direito'),(5,'Letras'),(6,'Medicina'),(7,'Odontologia'),(8,'Ciências da Computação'),(1,'Administração'),(2,'Ciências Contábeis'),(3,'Engenharia'),(4,'Direito'),(5,'Letras'),(6,'Medicina'),(7,'Odontologia'),(8,'Ciências da Computação'),(1,'Administração'),(2,'Ciências Contábeis'),(3,'Engenharia'),(4,'Direito'),(5,'Letras'),(6,'Medicina'),(7,'Odontologia'),(8,'Ciências da Computação'),(1,'Administração'),(2,'Ciências Contábeis'),(3,'Engenharia'),(4,'Direito'),(5,'Letras'),(6,'Medicina'),(7,'Odontologia'),(8,'Ciências da Computação'),(1,'Administração'),(2,'Ciências Contábeis'),(3,'Engenharia'),(4,'Direito'),(5,'Letras'),(6,'Medicina'),(7,'Odontologia'),(8,'Ciências da Computação'),(1,'Administração'),(2,'Ciências Contábeis'),(3,'Engenharia'),(4,'Direito'),(5,'Letras'),(6,'Medicina'),(7,'Odontologia'),(8,'Ciências da Computação');
/*!40000 ALTER TABLE `Cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cursos` (
  `ID` int(25) DEFAULT NULL,
  `course_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-29 21:42:06
