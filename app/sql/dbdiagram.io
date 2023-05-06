Table keyboard {
  id integer [primary key]
  name varchar
  keyboard_type_id integer
  switch_id integer
  keycap_id integer
}

Table keyboard_type {
  id integer [primary key]
  keyboard_type varchar
}

Table switch_type {
  id integer [primary key]
  switch_type varchar
}

Table switch {
  id integer [primary key]
  name varchar
  switch_type_id integer
}

Table keycap_profile {
  id integer [primary key]
  profile_name varchar
}

Table keycap {
  id integer [primary key]
  name varchar
  keycap_profile_id integer
}

Ref: keyboard.keyboard_type_id - keyboard_type.id 
Ref: keyboard.switch_id - switch.id 
Ref: keyboard.keycap_id - keycap.id 


Ref: switch.switch_type_id - switch_type.id 
Ref: keycap.keycap_profile_id - keycap_profile.id