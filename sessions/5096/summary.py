PHOTO_SESSIONS = []

photos = ['wro_w_p480_21_45_0', 'wro_n_p480_21_45_0', 'wro_w_p480_22_24_0', 'wro_n_p480_22_24_0']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))