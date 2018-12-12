for i in range(0, 29):
    if session.has_artifact('hor_{}'.format(i)):
        extract_file('hor_{}'.format(i), also=[49])
        decode_photo('assembled/hor_{}'.format(i))