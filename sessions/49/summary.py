for i in range(0, 29):
    if session.has_artifact('hor_{}'.format(i)):
        decode_photo('hor_{}'.format(i))