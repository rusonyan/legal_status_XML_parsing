/*
 Navicat Premium Data Transfer

 Source Server         : B5
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : 192.168.2.5:3306
 Source Schema         : test1109

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 25/11/2021 17:13:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ls.av
-- ----------------------------
DROP TABLE IF EXISTS `ls.av`;
CREATE TABLE `ls.av`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_number` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `take_effect_date` date NOT NULL,
  `original_source` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 6921 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for ls.cf
-- ----------------------------
DROP TABLE IF EXISTS `ls.cf`;
CREATE TABLE `ls.cf`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_number` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `apply_date` date NULL DEFAULT NULL,
  `original_source` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 3348088 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for ls.cp
-- ----------------------------
DROP TABLE IF EXISTS `ls.cp`;
CREATE TABLE `ls.cp`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `before_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `after_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `before_address` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `after_address` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `take_effect_date` date NOT NULL,
  `original_source` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `province` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `city` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `zone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `street` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 133609 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.cx
-- ----------------------------
DROP TABLE IF EXISTS `ls.cx`;
CREATE TABLE `ls.cx`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_number` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `apply_date` date NULL DEFAULT NULL,
  `announcement_date` date NOT NULL,
  `original_source` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 112171 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for ls.dblog
-- ----------------------------
DROP TABLE IF EXISTS `ls.dblog`;
CREATE TABLE `ls.dblog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `handle_time` datetime NULL DEFAULT NULL,
  `announcement_date` date NULL DEFAULT NULL,
  `filename` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 845 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.dd
-- ----------------------------
DROP TABLE IF EXISTS `ls.dd`;
CREATE TABLE `ls.dd`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `recipient` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `file_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1197 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.ec
-- ----------------------------
DROP TABLE IF EXISTS `ls.ec`;
CREATE TABLE `ls.ec`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `contract` char(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `giver` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `assignee` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.ee
-- ----------------------------
DROP TABLE IF EXISTS `ls.ee`;
CREATE TABLE `ls.ee`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `contract` char(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `giver` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `assignee` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `license_type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 803 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.ip
-- ----------------------------
DROP TABLE IF EXISTS `ls.ip`;
CREATE TABLE `ls.ip`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `decision_num` int(11) NULL DEFAULT NULL,
  `decision_date` date NULL DEFAULT NULL,
  `commission_num` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `conclusion` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.iw
-- ----------------------------
DROP TABLE IF EXISTS `ls.iw`;
CREATE TABLE `ls.iw`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_number` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `decision_number` int(11) NULL DEFAULT NULL,
  `announcement_date` date NOT NULL,
  `original_source` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 4831 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for ls.pc
-- ----------------------------
DROP TABLE IF EXISTS `ls.pc`;
CREATE TABLE `ls.pc`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `license_num` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pledger` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `pledgee` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 395 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.pd
-- ----------------------------
DROP TABLE IF EXISTS `ls.pd`;
CREATE TABLE `ls.pd`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_number` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `release_security_date` date NULL DEFAULT NULL,
  `original_source` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 4021 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for ls.pe
-- ----------------------------
DROP TABLE IF EXISTS `ls.pe`;
CREATE TABLE `ls.pe`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `license_num` char(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `date` date NULL DEFAULT NULL,
  `pledger` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `pledgee` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 673 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.pm
-- ----------------------------
DROP TABLE IF EXISTS `ls.pm`;
CREATE TABLE `ls.pm`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date` date NULL DEFAULT NULL,
  `matter` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `before` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `after` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.pp
-- ----------------------------
DROP TABLE IF EXISTS `ls.pp`;
CREATE TABLE `ls.pp`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_number` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `take_effect_date` date NOT NULL,
  `original_source` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 6699 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Table structure for ls.rr
-- ----------------------------
DROP TABLE IF EXISTS `ls.rr`;
CREATE TABLE `ls.rr`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `original_decision` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `original_date` date NULL DEFAULT NULL,
  `date` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.statechange
-- ----------------------------
DROP TABLE IF EXISTS `ls.statechange`;
CREATE TABLE `ls.statechange`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `before_change` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `after_change` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `announcement_date` date NOT NULL,
  `patent_num` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `raw_data` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `change_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 4008093 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for ls.tr
-- ----------------------------
DROP TABLE IF EXISTS `ls.tr`;
CREATE TABLE `ls.tr`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patent_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `before_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `after_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `before_address` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `after_address` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `take_effect_date` date NULL DEFAULT NULL,
  `original_source` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `province` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `city` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `zone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `street` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 150089 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
