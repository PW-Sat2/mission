PHOTO_SESSIONS = [3887, 3889, 3890]

files = [
    'a_w_12_46_0',
    'a_n_12_46_0',
    'a_w_12_48_0',
    'a_n_12_48_0',
    'a_w_12_50_0',
    'a_n_12_50_0',
    'a_w_14_10_0',
    'a_n_14_10_0',
    'a_w_14_12_0',
    'a_n_14_12_0',
    'a_w_14_14_0',
    'a_n_14_14_0',
    'a_w_14_16_0',
    'a_n_14_16_0',
    'a_n_13_29_0',
    'a_n_14_08_0',
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')