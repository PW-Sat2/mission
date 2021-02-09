PHOTO_SESSIONS = list(range(5130, session.session_number))

photos = ['n01w_0', 'n01n_0', 'n02w_0', 'n02n_0']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))