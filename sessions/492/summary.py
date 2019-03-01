PHOTO_SESSIONS = [490, 491]
PHOTO_SESSIONS_480 = [491]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
photos_480 = [1, 6, 7]

for p in photos:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

for p in photos_480:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS_480)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))
dump_scrubbing_status(2)
