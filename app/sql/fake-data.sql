INSERT INTO keyboard_type (id, name)
    VALUES
        (DEFAULT,'Solder'),
        (DEFAULT,'Hotswap'),
        (DEFAULT,'Unbuilt');

INSERT INTO switch_type (id, name)
    VALUES
        (DEFAULT, 'Linear'),
        (DEFAULT, 'Tactile'),
        (DEFAULT, 'Clicky');

INSERT INTO keycap_profile (id, name)
    VALUES
        (DEFAULT, 'SA'),
        (DEFAULT, 'Cherry'),
        (DEFAULT, 'XDA'),
        (DEFAULT, 'DSA'),
        (DEFAULT, 'KAT'),
        (DEFAULT, 'OEM');


INSERT INTO keycap (id, name, keycap_profile_id)
    VALUES
        (DEFAULT, 'GMK Pono', 2);

INSERT INTO switch (id, name, switch_type_id)
    VALUES
        (DEFAULT, 'Cherry MX Blacks', 1);

INSERT INTO keyboard (id, name, keyboard_type_id, switch_id, keycap_id)
    VALUES
        (DEFAULT, 'Grey Polaris', 2, 1, 1);
