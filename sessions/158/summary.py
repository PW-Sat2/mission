photos = [5,11,15,21,25,31,35,41,45,47,51,53,55,57,59,61,63,67,69,73,79,85]

for p in photos:
    decode_photo('sail.photo_{}'.format(p), output_file_name='sail_photo_{}.jpg'.format(p))