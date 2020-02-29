PHOTO_SESSIONS = [2938, 2939]

photos = range(0, 5)

for p in photos:
    extract_file('t{}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}w_480_0'.format(p), output_file_name='assembled/t{}w_480_0.jpg'.format(p))

    extract_file('t{}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}n_480_0'.format(p), output_file_name='assembled/t{}n_480_0.jpg'.format(p))