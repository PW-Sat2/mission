PHOTO_SESSIONS = [3343, 3344, 3345, 3346, 3347, 3348]

for p in range(1, 10):
    extract_file('a{}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/a{}n_480_0'.format(p), output_file_name='assembled/a{}n_480_0.jpg'.format(p))

    extract_file('a{}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/a{}w_480_0'.format(p), output_file_name='assembled/a{}w_480_0.jpg'.format(p))