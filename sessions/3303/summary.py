PHOTO_SESSIONS = [3299, 3300, 3301, 3302]

for p in range(1, 5):
    extract_file('t{}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}n_480_0'.format(p), output_file_name='assembled/t{}n_480_0.jpg'.format(p))

    extract_file('t{}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}w_480_0'.format(p), output_file_name='assembled/t{}w_480_0.jpg'.format(p))