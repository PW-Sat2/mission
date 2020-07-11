PHOTO_SESSIONS = [3797, 3798, 3799, 3800]

files = [
    'a_w_12_28_0',
    'a_n_12_28_0',
    'a_w_12_29_0',
    'a_n_12_29_0',
    'a_w_12_30_0',
    'a_n_12_30_0',
    'a_w_13_02_0',
    'a_n_13_02_0',
    'a_w_13_03_0',
    'a_n_13_03_0',
    'a_w_13_04_0',
    'a_n_13_04_0',
    'a_w_13_46_0',
    'a_n_13_46_0',
    'a_w_13_47_0',
    'a_n_13_47_0',
    'a_w_13_48_0',
    'a_n_13_48_0'
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')