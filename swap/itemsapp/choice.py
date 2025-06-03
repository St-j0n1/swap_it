Item_status = (
    ('new', 'New'),
    ('used', 'Used'),
    ('like_new', 'Like New'),
    ('damaged', 'Damaged'),
)

Rarity = (
    ('common', 'Common',),
    ('uncommon', 'Uncommon'),
    ('rare', 'Rare'),
    ('epic', 'Epic'),
    ('legendary', 'Legendary'),
    ('mythic', 'Mythic'),
    ('artifact', 'Artifact'),
    ('exotic', 'Exotic'),
    ('unique', 'Unique'),
    ('limited', 'Limited Edition'),
)

Item_type = (
    ('game', 'Game'),
    ('book', 'Book'),
)

Book_genre_choice = (
    ('fiction', 'Fiction'),
    ('non_fiction', 'Non-Fiction'),
    ('sci_fi', 'Science Fiction'),
    ('fantasy', 'Fantasy'),
    ('biography', 'Biography'),
    ('history', 'History'),
    ('other', 'Other'),
)

Clothes_size_choice = (
    ('xs', 'Extra Small'),
    ('s', 'Small'),
    ('m', 'Medium'),
    ('l', 'Large'),
    ('xl', 'Extra Large'),
    ('xxl', 'Double Extra Large'),
)

Clothes_type_choice = (
    ('shirt', 'Shirt'),
    ('pants', 'Pants'),
    ('dress', 'Dress'),
    ('jacket', 'Jacket'),
    ('shoes', 'Shoes'),
    ('accessory', 'Accessory'),
    ('other', 'Other'),
)

Game_platform_choice = (
    ('pc', 'PC'),
    ('playstation', 'PlayStation'),
    ('xbox', 'Xbox'),
    ('nintendo', 'Nintendo'),
    ('mobile', 'Mobile'),
    ('other', 'Other'),
)

Game_genre_choice = (
    ('action', 'Action'),
    ('adventure', 'Adventure'),
    ('rpg', 'Role-Playing Game'),
    ('strategy', 'Strategy'),
    ('sports', 'Sports'),
    ('simulation', 'Simulation'),
    ('other', 'Other'),
)

Screen_size_choice = (
    ("14", "14 inches"),
    ('15', '15 inches'),
    ('16', '16 inches'),
    ('17', '17 inches'),
    ('18', '18 inches'),
    ('19', '19 inches'),
    ('20', '20 inches'),
    ('24', '24 inches'),
    ('27', '27 inches'),
    ('30', '30 inches'),
    ('32', '32 inches'),
    ('40', '40 inches'),
    ('50', '50 inches'),
    ('55', '55 inches'),
    ('65', '65 inches'),
    ('75', '75 inches'),
    ('other', 'Other'),
)

Screen_type_choice = (
    ('led', 'LED'),
    ('oled', 'OLED'),
    ('qled', 'QLED'),
    ('lcd', 'LCD'),
    ('plasma', 'Plasma'),
    ('other', 'Other'),
)

PC_form_factor_choice = (
    ('desktop', 'Desktop'),
    ('laptop', 'Laptop'),
    ('all_in_one', 'All-in-One'),
    ('other', 'Other'),
)

Operation_system_choice = (
    ('windows', 'Windows'),
    ('macos', 'macOS'),
    ('linux', 'Linux'),
    ('chrome_os', 'Chrome OS'),
    ('freebsd', 'FreeBSD'),
    ('other', 'Other'),
)

CPU_Choice = (
    ('intel', 'Intel'),
    ('amd', 'AMD'),
    ('apple', 'Apple'),
    ('other', 'Other'),
)

Ram_architecture_choice = (
    ('ddr3', 'DDR3'),
    ('ddr4', 'DDR4'),
    ('ddr5', 'DDR5'),
    ('other', 'Other'),
)

Winchester_type_choice = (
    ('hdd', 'HDD'),
    ('ssd', 'SSD'),
    ('nvme', 'NVMe'),
    ('m2', 'M.2'),
    ('sata', 'SATA'),
    ('other', 'Other'),
)

Xbox_console_choice = (
    ('xbox_one', 'Xbox One'),
    ('xbox_series_x', 'Xbox Series X'),
    ('xbox_series_s', 'Xbox Series S'),
    ('other', 'Other'),
)

PlayStation_console_choice = (
    ('playstation_1', 'PlayStation 1'),
    ('playstation_2', 'PlayStation 2'),
    ('PlayStation_3', 'PlayStation 3'),
    ('playstation_4', 'PlayStation 4'),
    ('playstation_5', 'PlayStation 5'),
    ('playstation_portable', 'PlayStation Portable'),
    ('other', 'Other'),
)

Nintendo_console_choice = (
    ('nintendo_switch', 'Nintendo Switch'),
    ('nintendo_wii', 'Nintendo Wii'),
    ('nintendo_wii_u', 'Nintendo Wii U'),
    ('nintendo_3ds', 'Nintendo 3DS'),
    ('nintendo_ds', 'Nintendo DS'),
    ('other', 'Other'),
)

Tech_hardware_choices = (
    ('apple', 'Apple'),
    ('samsung', 'Samsung'),
    ('google', 'Google'),
    ('microsoft', 'Microsoft'),
    ('amazon', 'Amazon'),
    ('sony', 'Sony'),
    ('lg', 'LG'),
    ('dell', 'Dell'),
    ('hp', 'HP'),
    ('lenovo', 'Lenovo'),
    ('asus', 'ASUS'),
    ('acer', 'Acer'),
    ('msi', 'MSI'),
    ('gigabyte', 'Gigabyte'),
    ('nvidia', 'NVIDIA'),
    ('amd', 'AMD'),
    ('intel', 'Intel'),
    ('qualcomm', 'Qualcomm'),
    ('broadcom', 'Broadcom'),
    ('mediatek', 'MediaTek'),
    ('huawei', 'Huawei'),
    ('xiaomi', 'Xiaomi'),
    ('oppo', 'OPPO'),
    ('vivo', 'Vivo'),
    ('oneplus', 'OnePlus'),
    ('realme', 'Realme'),
    ('motorola', 'Motorola'),
    ('nokia', 'Nokia'),
    ('tcl', 'TCL'),
    ('hisense', 'Hisense'),
    ('panasonic', 'Panasonic'),
    ('toshiba', 'Toshiba'),
    ('fujitsu', 'Fujitsu'),
    ('hitachi', 'Hitachi'),
    ('sharp', 'Sharp'),
    ('canon', 'Canon'),
    ('nikon', 'Nikon'),
    ('epson', 'Epson'),
    ('brother', 'Brother'),
    ('cisco', 'Cisco'),
    ('netgear', 'Netgear'),
    ('tp_link', 'TP-Link'),
    ('d_link', 'D-Link'),
    ('ubiquiti', 'Ubiquiti'),
    ('corsair', 'Corsair'),
    ('logitech', 'Logitech'),
    ('razer', 'Razer'),
    ('steelseries', 'SteelSeries'),
    ('hyperx', 'HyperX'),
    ('seagate', 'Seagate'),
    ('western_digital', 'Western Digital'),
    ('sandisk', 'SanDisk'),
    ('kingston', 'Kingston'),
    ('crucial', 'Crucial'),
    ('evga', 'EVGA'),
    ('zotac', 'ZOTAC'),
    ('sapphire', 'Sapphire'),
    ('powercolor', 'PowerColor'),
    ('asrock', 'ASRock'),
    ('biostar', 'Biostar'),
    ('supermicro', 'Supermicro'),
    ('synology', 'Synology'),
    ('qnap', 'QNAP'),
    ('buffalo', 'Buffalo'),
    ('garmin', 'Garmin'),
    ('fitbit', 'Fitbit'),
    ('polar', 'Polar'),
    ('gopro', 'GoPro'),
    ('dji', 'DJI'),
    ('tesla', 'Tesla'),
    ('rivian', 'Rivian'),
    ('meta', 'Meta'),
    ('valve', 'Valve'),
    ('nintendo', 'Nintendo'),
    ('playstation', 'PlayStation'),
    ('xbox', 'Xbox'),
)