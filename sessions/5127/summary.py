PHOTO_SESSIONS = list(range(5125, session.session_number))

photos = ['l01w_0', 'l01n_0', 'l02w_0', 'l02n_0']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))