PHOTO_SESSIONS = list(range(5175, session.session_number))

photos = ['p5174_0_n_p480_0', 'p5174_1_w_p480_0']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))