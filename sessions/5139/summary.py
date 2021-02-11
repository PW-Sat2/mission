PHOTO_SESSIONS = list(range(5139, session.session_number))

photos = [1, 2]

for p in photos:
    extract_file('photo0{}n_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/photo0{}n_0'.format(p), output_file_name='assembled/photo0{}n_0.jpg'.format(p))

    extract_file('photo0{}w_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/photo0{}w_0'.format(p), output_file_name='assembled/photo0{}w_0.jpg'.format(p))
