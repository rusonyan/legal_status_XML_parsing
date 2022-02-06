/*
 CREATE BY RUSON YAN

 Sql Author       : 闫瑞松
 Phone Num        : 18531958592
 Notes            : 每个表的作用,以及每个字段对应的数据功能已加在表注释里,使用Navicat,右键设计表功能即可看见注释

*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for change_db_log
-- ----------------------------
DROP TABLE IF EXISTS `change_db_log`;
CREATE TABLE `change_db_log`
(
    `id`          int                                                    NOT NULL AUTO_INCREMENT,
    `handle_time` datetime                                               NULL DEFAULT NULL COMMENT '入库时间',
    `open_day`    date                                                   NULL DEFAULT NULL COMMENT '数据公开日',
    `source_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '源文件名',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '入库记录'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for constant
-- ----------------------------
DROP TABLE IF EXISTS `constant`;
CREATE TABLE `constant`
(
    `id`    int                                                          NOT NULL AUTO_INCREMENT,
    `code`  char(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci     NULL DEFAULT NULL COMMENT 'PDF的CP,只有CP01一种',
    `value` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci COMMENT = '变更代码    说明'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of constant
-- ----------------------------
INSERT INTO `constant`
VALUES (1, 'AV01', '专利权的主动放弃');
INSERT INTO `constant`
VALUES (2, 'CB03', '著录事项变更');
INSERT INTO `constant`
VALUES (3, 'CD02', '外观设计专利公报更正');
INSERT INTO `constant`
VALUES (4, 'CF01', '未缴年费专利权终止');
INSERT INTO `constant`
VALUES (5, 'CX01', '专利权有效期届满');
INSERT INTO `constant`
VALUES (6, 'CP01', '专利权人的姓名或者名称的变更');
INSERT INTO `constant`
VALUES (7, 'CP02', '专利权人的地址的变更');
INSERT INTO `constant`
VALUES (8, 'CP03', '专利权人的姓名或者名称、地址的变更');
INSERT INTO `constant`
VALUES (9, 'DD01', '文件的公告送达');
INSERT INTO `constant`
VALUES (10, 'EC01', '专利实施许可合同备案的注销');
INSERT INTO `constant`
VALUES (11, 'EE01', '专利实施许可合同备案的生效');
INSERT INTO `constant`
VALUES (12, 'EM01', '专利实施许可合同备案的变更');
INSERT INTO `constant`
VALUES (13, 'GR01', '外观设计专利权授予');
INSERT INTO `constant`
VALUES (14, 'IP01', '无效公告');
INSERT INTO `constant`
VALUES (15, 'IW01', '专利权全部无效');
INSERT INTO `constant`
VALUES (16, 'PC01', '专利权质押合同登记的注销');
INSERT INTO `constant`
VALUES (17, 'PE01', '专利权质押合同登记的生效');
INSERT INTO `constant`
VALUES (18, 'PM01', '专利权质押合同登记的变更');
INSERT INTO `constant`
VALUES (19, 'PD01', '专利权保全的解除');
INSERT INTO `constant`
VALUES (20, 'PP01', '专利权的保全');
INSERT INTO `constant`
VALUES (21, 'RR01', '权利的恢复');
INSERT INTO `constant`
VALUES (22, 'TR01', '专利权的转移');

-- ----------------------------
-- Table structure for cp
-- ----------------------------
DROP TABLE IF EXISTS `cp`;
CREATE TABLE `cp`
(
    `id`                      int                                                     NOT NULL AUTO_INCREMENT,
    `patent_id`               char(14) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL,
    `before_patentee`         varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更前主专利权人',
    `before_co_patent_holder` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更前共同专利权人',
    `after_patentee`          varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '变更后主专利权人',
    `after_co_patent_holder`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更后共同专利权人',
    `before_patentee_address` text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT '变更前主专利权人地址',
    `after_patentee_address`  text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT '变更后主专利权人地址',
    `take_effect_date`        date                                                    NOT NULL COMMENT '变更生效日',
    `original_source`         char(20) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL,
    `abcode`                  int                                                     NULL DEFAULT NULL COMMENT '中国行政地区代码(仅供参考,下同)',
    `province`                varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL,
    `city`                    varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL,
    `zones`                   varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL,
    `street`                  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '名称地址    变更'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for dd
-- ----------------------------
DROP TABLE IF EXISTS `dd`;
CREATE TABLE `dd`
(
    `id`        int                                                    NOT NULL AUTO_INCREMENT,
    `patent_id` char(14) CHARACTER SET utf8 COLLATE utf8_general_ci    NULL DEFAULT NULL,
    `recipient` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `file_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `pub_date`  date                                                   NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '文件公告    送达'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for ec
-- ----------------------------
DROP TABLE IF EXISTS `ec`;
CREATE TABLE `ec`
(
    `id`        int                                                    NOT NULL AUTO_INCREMENT,
    `patent_id` char(14) CHARACTER SET utf8 COLLATE utf8_general_ci    NULL DEFAULT NULL,
    `contract`  char(40) CHARACTER SET utf8 COLLATE utf8_general_ci    NULL DEFAULT NULL COMMENT '合同备案号',
    `giver`     text CHARACTER SET utf8 COLLATE utf8_general_ci        NULL COMMENT '让与人',
    `assignee`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '受让人',
    `pub_date`  date                                                   NULL DEFAULT NULL COMMENT '解除日',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利许可    注销'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for ee
-- ----------------------------
DROP TABLE IF EXISTS `ee`;
CREATE TABLE `ee`
(
    `id`           int                                                     NOT NULL AUTO_INCREMENT,
    `patent_id`    char(14) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL COMMENT '专利号',
    `contract`     char(40) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL COMMENT '合同备案号',
    `giver`        varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL COMMENT '让与人',
    `assignee`     varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL COMMENT '受让人',
    `product_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '使用外观设计的产品名称',
    `license_type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL COMMENT '许可种类',
    `pub_date`     date                                                    NULL DEFAULT NULL COMMENT '备案日',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利许可    生效'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for em
-- ----------------------------
DROP TABLE IF EXISTS `em`;
CREATE TABLE `em`
(
    `id`            int                                                     NOT NULL AUTO_INCREMENT,
    `patent_id`     char(14) CHARACTER SET utf8 COLLATE utf8_general_ci     NOT NULL,
    `contract`      varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci  NOT NULL COMMENT '合同备案号',
    `pub_date`      date                                                    NULL DEFAULT NULL,
    `matter`        text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT '变更事项',
    `before_change` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更前',
    `after_change`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更后',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利许可    变更'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for ip
-- ----------------------------
DROP TABLE IF EXISTS `ip`;
CREATE TABLE `ip`
(
    `id`             int                                                 NOT NULL AUTO_INCREMENT COMMENT '本表为部分无效表,全部无效表无对应表',
    `patent_id`      char(14) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `decision_num`   int                                                 NULL DEFAULT NULL COMMENT '无效宣告决定号',
    `decision_date`  date                                                NULL DEFAULT NULL COMMENT '无效宣告决定日',
    `commission_num` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '委内编号(PDF不提供这部分数据)',
    `conclusion`     text CHARACTER SET utf8 COLLATE utf8_general_ci     NULL COMMENT '审查结论(PDF不提供这部分数据)',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利无效    部分'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for patent_change_log
-- ----------------------------
DROP TABLE IF EXISTS `patent_change_log`;
CREATE TABLE `patent_change_log`
(
    `id`            int                                                     NOT NULL AUTO_INCREMENT,
    `code`          char(4) CHARACTER SET utf8 COLLATE utf8_general_ci      NOT NULL COMMENT '状态代码',
    `pub_date`      date                                                    NOT NULL COMMENT '事务公告日或事务生效日,以对应法律状态为准',
    `patent_num`    char(14) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL COMMENT '专利号',
    `raw_data`      text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT 'XML原始数据公告(PDF源数据模以XML公告生成此字段)',
    `change_id`     int                                                     NULL DEFAULT NULL,
    `source`        char(20) CHARACTER SET utf8 COLLATE utf8_general_ci     NOT NULL COMMENT 'PDF对应源数据文件名,XML对应事务公告日',
    `before_change` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '仅应用于cp和tr,表示前后专利权人信息变化',
    `after_change`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '仅应用于cp和tr,表示前后专利权人信息变化',
    PRIMARY KEY (`id`) USING BTREE,
    INDEX `patent_num_index` (`patent_num` ASC) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '总      表'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for pc
-- ----------------------------
DROP TABLE IF EXISTS `pc`;
CREATE TABLE `pc`
(
    `id`          int                                                 NOT NULL AUTO_INCREMENT,
    `patent_id`   char(14) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `license_num` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '登记号',
    `pledger`     text CHARACTER SET utf8 COLLATE utf8_general_ci     NULL COMMENT '出质人',
    `pledgee`     text CHARACTER SET utf8 COLLATE utf8_general_ci     NULL COMMENT '质权人',
    `pub_date`    date                                                NULL DEFAULT NULL COMMENT '解除日',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利质押    注销'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for pe
-- ----------------------------
DROP TABLE IF EXISTS `pe`;
CREATE TABLE `pe`
(
    `id`           int                                                     NOT NULL AUTO_INCREMENT,
    `patent_id`    char(14) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL,
    `license_num`  char(40) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL COMMENT '登记号',
    `pub_date`     date                                                    NULL DEFAULT NULL COMMENT '登记生效日',
    `pledger`      text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT '出质人',
    `pledgee`      text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT '质权人',
    `product_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '使用外观设计的产品名称',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利质押    生效'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for pm
-- ----------------------------
DROP TABLE IF EXISTS `pm`;
CREATE TABLE `pm`
(
    `id`            int                                                     NOT NULL AUTO_INCREMENT,
    `patent_id`     char(14) CHARACTER SET utf8 COLLATE utf8_general_ci     NOT NULL,
    `contract`      varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL COMMENT '登记号',
    `pub_date`      date                                                    NULL DEFAULT NULL COMMENT '变更日',
    `matter`        text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT '变更事项',
    `before_change` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更前',
    `after_change`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更后',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利质押    变更'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for rr
-- ----------------------------
DROP TABLE IF EXISTS `rr`;
CREATE TABLE `rr`
(
    `id`                int                                                    NOT NULL AUTO_INCREMENT,
    `patent_id`         char(14) CHARACTER SET utf8 COLLATE utf8_general_ci    NULL DEFAULT NULL,
    `original_decision` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    `original_date`     date                                                   NULL DEFAULT NULL,
    `pub_date`          date                                                   NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利权利    恢复'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for tr
-- ----------------------------
DROP TABLE IF EXISTS `tr`;
CREATE TABLE `tr`
(
    `id`                      int                                                     NOT NULL AUTO_INCREMENT,
    `patent_id`               char(14) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL,
    `before_patentee`         varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更前主专利权人',
    `before_co_patent_holder` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更前共同专利权人',
    `after_patentee`          varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更后主专利权人',
    `after_co_patent_holder`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '变更后共同专利权人',
    `before_patentee_address` text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT '变更前主专利权人地址',
    `after_patentee_address`  text CHARACTER SET utf8 COLLATE utf8_general_ci         NULL COMMENT '变更后专利权人地址',
    `take_effect_date`        date                                                    NULL DEFAULT NULL COMMENT '变更生效日',
    `original_source`         char(20) CHARACTER SET utf8 COLLATE utf8_general_ci     NULL DEFAULT NULL,
    `abcode`                  int                                                     NULL DEFAULT NULL COMMENT '中国行政区代码(仅供参考,下同)',
    `province`                varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL,
    `city`                    varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL,
    `zones`                   varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci  NULL DEFAULT NULL,
    `street`                  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  CHARACTER SET = utf8
  COLLATE = utf8_general_ci COMMENT = '专利权人    转移'
  ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Procedure structure for clear
-- ----------------------------
DROP PROCEDURE IF EXISTS `clear`;
delimiter ;;
CREATE PROCEDURE clear()
BEGIN
    #Routine body goes here...
    truncate table change_db_log;
    truncate table cp;
    truncate table dd;
    truncate table ec;
    truncate table ee;
    truncate table ip;
    truncate table patent_change_log;
    truncate table pc;
    truncate table pe;
    truncate table pm;
    truncate table rr;
    truncate table tr;

END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
