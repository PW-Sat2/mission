PHOTO_SESSIONS = list(range(5090, session.session_number))

photos = [
	't01w_0',
	't01n_0',
    't02w_0',
    't02n_0',
]

for p in photos:
    extract_file(p, also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))
