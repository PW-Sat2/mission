PHOTO_SESSIONS = []

photos = [1, 2]

for p in photos:
    extract_file('p{}_480_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/p{}_480_0'.format(p), output_file_name='assembled/p{}_480_0.jpg'.format(p))


dump_scrubbing_status(2)