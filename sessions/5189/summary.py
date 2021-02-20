PHOTO_SESSIONS = list(range(5186, session.session_number))

photos = ['p1_n_480_0', 'p1_w_480_0', 'p2_n_480_0', 'p2_w_480_0']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))