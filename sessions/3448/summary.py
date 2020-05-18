PHOTO_SESSIONS = [3438, 3439, 3445, 3448]

for p in range(1, 10):
    extract_file('m{}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/m{}n_480_0'.format(p), output_file_name='assembled/m{}n_480_0.jpg'.format(p))

    extract_file('m{}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/m{}w_480_0'.format(p), output_file_name='assembled/m{}w_480_0.jpg'.format(p))

