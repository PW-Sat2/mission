PHOTO_SESSIONS = [3617, 3620, 3621]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for p in photos:
    extract_file('p{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_0'.format(p), output_file_name='assembled/p{}_0.jpg'.format(p))

for p in range(1, 6):
    extract_file('t{}n_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}n_0'.format(p), output_file_name='assembled/t{}n_0.jpg'.format(p))

    extract_file('t{}w_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{}w_0'.format(p), output_file_name='assembled/t{}w_0.jpg'.format(p))

