PHOTO_SESSIONS = [3438]

for p in range(1, 9):
    extract_file('m{}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/m{}n_480_0'.format(p), output_file_name='assembled/m{}n_480_0.jpg'.format(p))

    extract_file('m{}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/m{}w_480_0'.format(p), output_file_name='assembled/m{}w_480_0.jpg'.format(p))

