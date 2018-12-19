configTOTAL_HEAP_SIZE = 352 * 1024
portBYTE_ALIGNMENT = 8

configADJUSTED_HEAP_SIZE = configTOTAL_HEAP_SIZE - portBYTE_ALIGNMENT 

(xNextFreeByte,) = unpack_binary_file('memory_content_2', '<L')
free_heap = configADJUSTED_HEAP_SIZE - xNextFreeByte
session.write_artifact('heap_2.txt', 'Free heap = {} bytes'.format(free_heap))

(xNextFreeByte,) = unpack_binary_file('memory_content_5', '<L')
free_heap = configADJUSTED_HEAP_SIZE - xNextFreeByte
session.write_artifact('heap_5.txt', 'Free heap = {} bytes'.format(free_heap))