PHOTO_SESSIONS = [4344]

files = [
    't_w_22_40_0',
    't_w_22_41_0',
    't_w_22_42_0',
]

for f in files:
    extract_file(f, also=PHOTO_SESSIONS)
    decode_photo('assembled/' + f, output_file_name='assembled/' + f + '.jpg')