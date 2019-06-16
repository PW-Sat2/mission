PHOTO_SESSIONS = [1279, 1281, 1282]

photos_hr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for p in photos_hr:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))
