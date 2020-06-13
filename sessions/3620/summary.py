PHOTO_SESSIONS = [3617, 3620]

photos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for p in photos:
    extract_file('p{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_0'.format(p), output_file_name='assembled/p{}_0.jpg'.format(p))
