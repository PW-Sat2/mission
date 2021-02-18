PHOTO_SESSIONS = list(range(5182, session.session_number))

photos = ['n01n', 'n01w', 'n02n', 'n02w']

for p in photos:
    extract_file('{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))
