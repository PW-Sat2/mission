PHOTO_SESSIONS = []

photos = [0, 1, 2]

for p in photos:
    extract_file('b_w_p480_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/b_w_p480_{}_0'.format(p), output_file_name='assembled/b_w_p480_{}_0.jpg'.format(p))

    extract_file('b_n_p480_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/b_n_p480_{}_0'.format(p), output_file_name='assembled/b_n_p480_{}_0.jpg'.format(p))