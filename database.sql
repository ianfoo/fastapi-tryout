CREATE DATABASE IF NOT EXISTS `fastapi_tryout` 
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- WARNING! This is a highly permissive grant for what
-- is an unsecured database. In general, do not use this!
-- It is only for the purposes of this tryout.
GRANT ALL ON `fastapi_tryout`.* TO ''@'localhost';
FLUSH PRIVILEGES;

USE `fastapi_tryout`;
CREATE TABLE IF NOT EXISTS `accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `vault_uuid` char(36) NOT NULL,
  `label` varchar(255) NOT NULL,
  `chain` varchar(50) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_account_uuid` (`uuid`)
);
