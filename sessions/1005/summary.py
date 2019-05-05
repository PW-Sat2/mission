PHOTO_SESSIONS = [997, 998, 1001, 1002, 1004]

lr_photos = [5, 8]
hr_photos = [2, 3, 8, 9, 10]
for p in lr_photos:
    extract_file('p{}_128_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_128_0'.format(p), output_file_name='assembled/p{}_128_0.jpg'.format(p))

for p in hr_photos:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))

