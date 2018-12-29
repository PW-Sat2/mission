extract_file('sail.photo_45', also=[158])
extract_file('sail.photo_55', also=[158])
extract_file('sail.photo_67', also=[158])

decode_photo('assembled/sail.photo_45')
decode_photo('assembled/sail.photo_55')
decode_photo('assembled/sail.photo_67')

extract_file('sail.exp', also=[158])

photos = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 65, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87]

for p in photos:
    decode_photo('sail.photo_{}'.format(p), output_file_name='sail_photo_{}.jpg'.format(p))
