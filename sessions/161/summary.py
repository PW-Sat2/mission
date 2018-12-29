PHOTO_SESSIONS = [158, 160]

photos = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87]

for p in photos:
    extract_file('sail.photo_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/sail.photo_{}'.format(p), output_file_name='assembled/sail_photo_{}.jpg'.format(p))
