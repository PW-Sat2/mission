PHOTO_SESSIONS = [1798]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

extract_file('radfet_21a', also=[1798])

for p in photos:
    extract_file('t{:02}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{:02}w_480_0'.format(p), output_file_name='assembled/t{:02}w_480_0.jpg'.format(p))

    extract_file('t{:02}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{:02}n_480_0'.format(p), output_file_name='assembled/t{:02}n_480_0.jpg'.format(p))

photosDummy = [2, 3, 4, 5]

for p in photosDummy:
    extract_file('dummy{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/dummy{}_0'.format(p), output_file_name='assembled/dummy{}_0.jpg'.format(p))
