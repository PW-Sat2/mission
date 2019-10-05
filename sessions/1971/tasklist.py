tasks = [
    # Generated on 2019-10-06 00:10:05.865000, contains telemetry from sessions 1970 to 1971.
    # The session starts on 2019-10-06 09:49:32+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(39, '/telemetry.previous', [1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279, 1404]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [49, 99, 149, 199, 24, 74, 124, 174, 224, 12, 62, 112, 162, 212, 36, 86, 136, 186, 6, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1454, 1504, 1554, 1604, 1654, 1704, 1754, 1804, 1854, 1904, 1954, 2004, 2054, 2104, 2154, 2204, 2254, 1392, 1442, 1492]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892, 1942, 1992, 2042, 2092, 2142, 2192, 2242, 1416, 1466, 1516, 1566, 1616]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 1386, 1436, 1486, 1536, 1586, 1636, 1686]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [106, 156, 206, 18, 68, 118, 168, 218, 30, 80, 130, 180, 230, 42, 92, 142, 192]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [1848, 1898, 1948, 1998, 2048, 2098, 2148, 2198, 2248, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1960, 2010, 2060, 2110, 2160, 2210, 2260, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [2072, 2122, 2172, 2222, 2272, 1257, 1269, 1357]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(31, '/t01n_480_0', [9]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t01w_480_0', [20, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t02n_480_0', [19, 22, 24, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t02w_480_0', [35, 36]), Send, WaitMode.Wait],

    [tc.DownloadFile(35, '/t03n_480_0', [24, 28, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t03w_480_0', [18, 20, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t04n_480_0', [7, 8, 11, 31, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t04w_480_0', [3, 29, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(52, '/t03n_480_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t03n_480_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t03n_480_0', [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]), Send, WaitMode.Wait],

    [tc.DownloadFile(58, '/t03w_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t03w_480_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t03w_480_0', [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t03w_480_0', [103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],

    [tc.DownloadFile(65, '/t04n_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t04n_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t04n_480_0', [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t04n_480_0', [106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t04n_480_0', [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],

    [tc.DownloadFile(73, '/t04w_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t04w_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t04w_480_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],

    [tc.DownloadFile(76, '/suns_ps_15', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/suns_ps_15', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/suns_ps_15', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/suns_ps_15', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/suns_ps_15', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/suns_ps_15', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/suns_ps_15', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/suns_ps_15', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/suns_ps_15', [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/suns_ps_15', [180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/suns_ps_15', [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/suns_ps_15', [220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/suns_ps_15', [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/suns_ps_15', [260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/suns_ps_15', [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/suns_ps_15', [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/suns_ps_15', [320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/suns_ps_15', [340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/suns_ps_15', [360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/suns_ps_15', [379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/suns_ps_15', [398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]