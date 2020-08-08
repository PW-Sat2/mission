PHOTO_SESSIONS = [3975, 3976]

files = [
    'a_w_11_30_0',
    'a_n_11_30_0',
    'a_w_11_31_0',
    'a_n_11_31_0',
    'a_w_11_32_0',
    'a_n_11_32_0',
    'a_w_11_40_0',
    'a_n_11_40_0',
    'a_w_11_41_0',
    'a_n_11_41_0',
    'a_w_11_42_0',
    'a_n_11_42_0',
    'a_w_11_57_0',
    'a_n_11_57_0',
    'a_w_11_58_0',
    'a_n_11_58_0',
    'a_w_11_59_0',
    'a_n_11_59_0',
    'a_w_12_59_0',
    'a_n_12_59_0',
    'a_w_13_00_0',
    'a_n_13_00_0',
    'a_w_13_01_0',
    'a_n_13_01_0',
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')