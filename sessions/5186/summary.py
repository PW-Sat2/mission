PHOTO_SESSIONS = list(range(5172, session.session_number))

photos = ['p1_n_480', 'p1_w_480', 'p2_n_480', 'p2_w_480']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))