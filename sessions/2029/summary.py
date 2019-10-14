PHOTO_SESSIONS = [2017, 2018, 2019, 2021, 2022, 2025, 2026, 2028]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

for p in photos:
    extract_file('t{:02}w_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{:02}w_480_0'.format(p), output_file_name='assembled/t{:02}w_480_0.jpg'.format(p))

    extract_file('t{:02}n_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t{:02}n_480_0'.format(p), output_file_name='assembled/t{:02}n_480_0.jpg'.format(p))

photosDummy = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]

for p in photosDummy:
    extract_file('dummy_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/dummy_{}_0'.format(p), output_file_name='assembled/dummy_{}_0.jpg'.format(p))

# t01 - t10 - night photos of Korea and China
# t11 - t18 - night photos of Western Europa
# t19 - t26 - night photos of USA