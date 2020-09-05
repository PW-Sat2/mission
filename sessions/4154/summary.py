PHOTO_SESSIONS = [4153, 4154]

files = [
    'm_w_11_23_0',
    'm_n_11_23_0',
    'm_w_11_24_0',
    'm_n_11_24_0',
    'm_w_11_26_0',
    'm_n_11_26_0',
    'm_w_11_27_0',
    'm_n_11_27_0',
    'm_w_11_28_0',
    'm_n_11_28_0',
    'm_w_11_29_0',
    'm_n_11_29_0',
    'm_w_11_38_0',
    'm_n_11_38_0',
    'm_w_11_41_0',
    'm_n_11_41_0',
    'm_w_12_36_0',
    'm_n_12_36_0',
    'm_w_12_37_0',
    'm_n_12_37_0',
    'm_w_12_38_0',
    'm_n_12_38_0',
    'm_w_12_39_0',
    'm_n_12_39_0',
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')