PHOTO_SESSIONS = [4246]

files = [
    't_w_21_52_0',
    't_n_21_52_0',
    't_w_21_53_0',
    't_n_21_53_0',
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')