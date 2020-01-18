PHOTO_SESSIONS = [2663]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for p in photos:
    extract_file('p{:02}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{:02}w_480_0'.format(p), output_file_name='assembled/p{:02}w_480_0.jpg'.format(p))

    extract_file('p{:02}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{:02}n_480_0'.format(p), output_file_name='assembled/p{:02}n_480_0.jpg'.format(p))

