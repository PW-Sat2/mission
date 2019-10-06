tasks = [
    # Generated on 2019-10-06 10:24:12.346000, contains telemetry from sessions 1971 to 1972.
    # The session starts on 2019-10-06 11:23:28+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(80, '/telemetry.current', [190, 240, 290, 340, 390, 215, 265, 315, 365, 203, 253, 303, 353, 403, 227, 277, 327, 377, 197, 247]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [297, 347, 397, 209, 259, 309, 359, 409, 221, 271, 321, 371, 233, 283, 333, 383]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(43, '/telemetry.previous', [1257, 1269, 1357, 1386, 1392, 1398, 1410, 1416, 1422, 1436, 1442, 1448, 1454, 1460, 1466, 1472, 1486, 1492, 1498]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1504, 1510, 1516, 1522, 1536, 1542, 1548, 1554, 1560, 1566, 1572, 1586, 1592, 1598, 1604, 1610, 1616, 1622, 1636]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1642, 1648, 1654, 1660, 1666, 1672, 1686, 1692, 1698, 1704, 1710, 1716, 1722, 1736, 1742, 1748, 1754, 1760]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [1766, 1772, 1786, 1792, 1798, 1804, 1810, 1816, 1822, 1836, 1842, 1848, 1854, 1860, 1866, 1872, 1886, 1892]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1898, 1904, 1910, 1916, 1922, 1936, 1942, 1948, 1954, 1960, 1966, 1972, 1986, 1992, 1998, 2004, 2010, 2016]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [2022, 2036, 2042, 2048, 2054, 2060, 2066, 2072, 2086, 2092, 2098, 2104, 2110, 2116, 2122, 2136, 2142, 2148]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [2154, 2160, 2166, 2172, 2186, 2192, 2198, 2204, 2210, 2216, 2222, 2236, 2242, 2248, 2254, 2260, 2266, 2272]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [6, 12, 18, 24, 30, 36, 42, 49, 56, 62, 68, 74, 80, 86, 92, 99, 106, 112, 118]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [124, 130, 136, 142, 149, 156, 162, 168, 174, 180, 186, 192, 199, 206, 212, 218, 224, 230]), Send, WaitMode.Wait],

    [tc.DownloadFile(41, '/t01w_480_0', [20, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t01n_480_0', [9]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t02n_480_0', [19, 22, 24, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t02w_480_0', [35, 36]), Send, WaitMode.Wait],

    [tc.DownloadFile(30, '/t04n_480_0', [7, 8, 11, 31, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t04n_480_0', [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t04n_480_0', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t04n_480_0', [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t04n_480_0', [122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t03w_480_0', [18, 20, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t03w_480_0', [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t03w_480_0', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t03w_480_0', [103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t04w_480_0', [3, 29, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t04w_480_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t04w_480_0', [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t04w_480_0', [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(77, '/t03n_480_0', [24, 28, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t03n_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t03n_480_0', [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]), Send, WaitMode.Wait],

    [tc.DownloadFile(54, '/suns_ps_15', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_15', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/suns_ps_15', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/suns_ps_15', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/suns_ps_15', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/suns_ps_15', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/suns_ps_15', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/suns_ps_15', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/suns_ps_15', [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/suns_ps_15', [180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/suns_ps_15', [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/suns_ps_15', [220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/suns_ps_15', [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/suns_ps_15', [260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/suns_ps_15', [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/suns_ps_15', [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/suns_ps_15', [320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/suns_ps_15', [340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/suns_ps_15', [360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/suns_ps_15', [379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/suns_ps_15', [398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416]), Send, WaitMode.Wait],
    # missing from previous session end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]