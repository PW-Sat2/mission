PHOTO_SESSIONS = [2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

for p in photos:
    extract_file('t{:02}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{:02}w_480_0'.format(p), output_file_name='assembled/t{:02}w_480_0.jpg'.format(p))

    extract_file('t{:02}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{:02}n_480_0'.format(p), output_file_name='assembled/t{:02}n_480_0.jpg'.format(p))

photosDummy = [1, 2, 3, 4, 6, 7, 8]

for p in photosDummy:
    extract_file('dummy_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/dummy_{}_0'.format(p), output_file_name='assembled/dummy_{}_0.jpg'.format(p))

# t01 - t09 - India
# t10 - t22 - Hawaii
