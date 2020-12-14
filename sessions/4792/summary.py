PHOTO_SESSIONS = [4789, 4790, 4791]

photos = [    
    '16_08',
    '16_09',
    '16_10',
    '16_11',
    '16_12',
    '17_41',
    '17_42',
    '17_43',
    '17_44',
    '17_45',
    '17_46',
    ]

for p in photos:
    extract_file('n_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/n_{}_0'.format(p), output_file_name='assembled/n_{}_0.jpg'.format(p))

    extract_file('w_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/w_{}_0'.format(p), output_file_name='assembled/w_{}_0.jpg'.format(p))


small_photos = [    
    '13_42',
    '14_42',
    '15_42', 
    '17_11', 
    ]

for p in small_photos:
    extract_file('x_{}_0'.format(p), also=PHOTO_SESSIONS)
    decode_photo('assembled/x_{}_0'.format(p), output_file_name='assembled/x_{}_0.jpg'.format(p))
