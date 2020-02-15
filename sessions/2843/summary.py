PHOTO_SESSIONS = []

photos = range(0, 9)

for p in lr_photos:
    extract_file('p{}_480'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480'.format(p), output_file_name='assembled/p{}_480.jpg'.format(p))