PHOTO_SESSIONS = [4557, 4558, 4559, 4560, 4561, 4562, 4563]

photos = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for p in photos:
    extract_file('n_w_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/n_w_{}_0'.format(p), output_file_name='assembled/n_w_{}_0.jpg'.format(p))

    extract_file('n_n_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/n_n_{}_0'.format(p), output_file_name='assembled/n_n_{}_0.jpg'.format(p))
