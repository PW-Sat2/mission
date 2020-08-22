PHOTO_SESSIONS = [4066]

files = [
    'a_w_11_28_0',
    'a_n_11_28_0',
    'a_w_11_29_0',
    'a_n_11_29_0',
    'a_w_11_30_0',
    'a_n_11_30_0',
    'a_w_11_33_0',
    'a_n_11_33_0',
    'a_w_11_34_0',
    'a_n_11_34_0',
    'a_w_11_35_0',
    'a_n_11_35_0',
    'a_w_11_49_0',
    'a_n_11_49_0',
    'a_w_11_50_0',
    'a_n_11_50_0',
    'a_w_11_51_0',
    'a_n_11_51_0',
    'a_w_12_58_0',
    'a_n_12_58_0',
    'a_w_12_59_0',
    'a_n_12_59_0',
    'a_w_13_00_0',
    'a_n_13_00_0',
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')