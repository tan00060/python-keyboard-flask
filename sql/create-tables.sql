CREATE USER keyboard WITH PASSWORD 'password';
CREATE DATABASE keyboard WITH OWNER keyboard

CREATE TABLE keyboard_type (
  id SERIAL,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE switch_type (
  id SERIAL,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE keycap_profile (
  id SERIAL,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE switch (
  id SERIAL,
  name VARCHAR(50) NOT NULL,
  switch_type_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY (switch_type_id) REFERENCES switch_type(id)
);

CREATE TABLE keycap (
  id SERIAL,
  name VARCHAR(50) NOT NULL,
  keycap_profile_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY (keycap_profile_id) REFERENCES keycap_profile(id)
);

CREATE TABLE keyboard (
  id SERIAL,
  name VARCHAR(50) NOT NULL,
  keyboard_type_id INTEGER NOT NULL,
  switch_id INTEGER NOT NULL,
  keycap_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY (keyboard_type_id) REFERENCES keyboard_type(id),
  FOREIGN KEY (switch_id) REFERENCES switch(id),
  FOREIGN KEY (keycap_id) REFERENCES keycap(id)
);