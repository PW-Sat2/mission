parse_experiment('suns_2')

configTOTAL_HEAP_SIZE = 352 * 1024
portBYTE_ALIGNMENT = 8

configADJUSTED_HEAP_SIZE = configTOTAL_HEAP_SIZE - portBYTE_ALIGNMENT 

(xNextFreeByte,) = unpack_binary_file('memory_content_13', '<L')
free_heap = configADJUSTED_HEAP_SIZE - xNextFreeByte
session.write_artifact('heap_13.txt', 'Free heap = {} bytes'.format(free_heap))

(xNextFreeByte,) = unpack_binary_file('memory_content_15', '<L')
free_heap = configADJUSTED_HEAP_SIZE - xNextFreeByte
session.write_artifact('heap_15.txt', 'Free heap = {} bytes'.format(free_heap))