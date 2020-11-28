PHOTO_SESSIONS = [4692]

photos = [0, 1]

for p in photos:
    extract_file('n_p480_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/n_p480_{}_0'.format(p), output_file_name='assembled/n_p480_{}_0.jpg'.format(p))

    extract_file('w_p480_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/w_p480_{}_0'.format(p), output_file_name='assembled/w_p480_{}_0.jpg'.format(p))
