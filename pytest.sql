/*
Navicat MySQL Data Transfer

Source Server         : localhost_root
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : pytest

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-11-15 19:17:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jobs
-- ----------------------------
DROP TABLE IF EXISTS `jobs`;
CREATE TABLE `jobs` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `job` varchar(255) NOT NULL COMMENT '求职岗位',
  `company` varchar(255) NOT NULL COMMENT '招聘公司',
  `address` varchar(64) DEFAULT NULL COMMENT '所在区域',
  `lowest_salary` decimal(10,2) NOT NULL COMMENT '最低薪资',
  `highest_salary` decimal(10,2) NOT NULL COMMENT '最高薪资',
  `date` varchar(64) DEFAULT NULL COMMENT '招聘发布日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13636 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for lagou_job
-- ----------------------------
DROP TABLE IF EXISTS `lagou_job`;
CREATE TABLE `lagou_job` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `position_name` varchar(64) NOT NULL COMMENT '职位名称',
  `salary` varchar(64) DEFAULT NULL,
  `city` varchar(64) DEFAULT NULL COMMENT '城市',
  `address` varchar(64) DEFAULT NULL COMMENT '区域所在地',
  `business_zone` varchar(64) DEFAULT NULL COMMENT '商业热点地',
  `line_station` varchar(255) DEFAULT NULL COMMENT '通行交通线',
  `company` varchar(255) NOT NULL COMMENT '公司名称',
  `company_size` varchar(64) DEFAULT NULL COMMENT '公司规模',
  `education` varchar(64) DEFAULT NULL COMMENT '学历要求',
  `work_year` varchar(255) DEFAULT NULL COMMENT '要求工作年限',
  `finance_stage` varchar(64) DEFAULT NULL COMMENT '公司状态',
  `industry_field` varchar(255) DEFAULT NULL COMMENT '公司经营领域',
  `industry_label` varchar(255) DEFAULT NULL COMMENT '涉及技术领域',
  `company_advantage` varchar(255) DEFAULT NULL COMMENT '公司福利',
  `first_type` varchar(255) DEFAULT NULL COMMENT '招聘类型',
  `create_time` varchar(64) DEFAULT NULL COMMENT '发布日期',
  `gmt_create` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for titles
-- ----------------------------
DROP TABLE IF EXISTS `titles`;
CREATE TABLE `titles` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `url` varchar(255) DEFAULT NULL COMMENT '访问地址',
  `title` varchar(255) DEFAULT NULL COMMENT '文章标题',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8;
