PHOTO_SESSIONS = [3707]

files = [
    'dummy_14_33_0',
    'dummy_15_33_0',
    'dummy_16_33_0',
    'a_w_17_00_0',
    'a_n_17_00_0',
    'a_w_17_01_0',
    'a_n_17_01_0',
    'a_w_17_02_0',
    'a_n_17_02_0',
    'a_w_17_03_0',
    'a_n_17_03_0',
    'a_w_17_04_0',
    'a_n_17_04_0',
    'dummy_18_04_0',
    'dummy_19_04_0',
    'a_w_20_02_0',
    'a_n_20_02_0',
    'a_w_20_03_0',
    'a_n_20_03_0',
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')