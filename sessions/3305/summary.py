PHOTO_SESSIONS = [3299, 3300, 3301, 3302, 3303, 3304]

for p in range(1, 5):
    extract_file('t{}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}n_480_0'.format(p), output_file_name='assembled/t{}n_480_0.jpg'.format(p))

    extract_file('t{}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}w_480_0'.format(p), output_file_name='assembled/t{}w_480_0.jpg'.format(p))

p=1

extract_file('a{}n_480_0'.format(p), also=PHOTO_SESSIONS)
decode_photo('assembled/a{}n_480_0'.format(p), output_file_name='assembled/a{}n_480_0.jpg'.format(p))

extract_file('a{}w_480_0'.format(p), also=PHOTO_SESSIONS)
decode_photo('assembled/a{}w_480_0'.format(p), output_file_name='assembled/a{}w_480_0.jpg'.format(p))