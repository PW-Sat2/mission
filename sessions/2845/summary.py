PHOTO_SESSIONS = [2844]

photos = range(0, 9)

for p in lr_photos:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))