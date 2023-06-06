CREATE TABLE `tbl_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `tbl_user`
  (`name`,`email`)
VALUES 
  ('Jacinto Silva', 'joao@crud.com'),
  ('Carina Oliveira', 'cariliv@ter.com'),
  ('Dominic Souza', 'domsa@crud.com'),
  ('Dimitry Regreto', 'regreto@crud.com');