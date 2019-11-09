PHOTO_SESSIONS = [2204, 2205]

lr_photos = []

hr_photos = ['t01n_480_0', 't01w_480_0', 't02n_480_0', 't02w_480_0', 't03n_480_0', 't03w_480_0', 't04n_480_0', 't04w_480_0', 't05n_480_0', 't05w_480_0', 't06n_480_0', 't06w_480_0', 't07n_480_0', 't07w_480_0', 't08n_480_0', 't08w_480_0', 't09n_480_0', 't09w_480_0']

for p in lr_photos:
    extract_file('t02w_240_{}'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/t02w_240_{}'.format(p), output_file_name='assembled/t02w_240_{}.jpg'.format(p))

for p in hr_photos:
    extract_file(p, also=PHOTO_SESSIONS)
    decode_photo('assembled/{}'.format(p), output_file_name='assembled/{}.jpg'.format(p))