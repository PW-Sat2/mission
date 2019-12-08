tasks = [
    # Generated on 2019-12-08 18:48:33.775000, contains telemetry from sessions 2395 to 2396.
    # The session starts on 2019-12-08 18:51:36+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(105, '/telemetry.previous', [2127, 2177, 2227, 2277, 2152, 2202, 2252, 2140, 2190, 2240, 2164, 2214, 2264, 2134, 2184, 2234, 2146, 2196, 2246, 2158]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547, 22, 72, 122, 172, 222, 272, 322, 372, 422]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.current', [472, 522, 10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 34, 84, 134, 184, 234, 284]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.current', [334, 384, 434, 484, 534, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504, 554, 16, 66, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.current', [166, 216, 266, 316, 366, 416, 466, 516, 566, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/telemetry.previous', [2208, 2258, 2170, 2220, 2270]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.current', [40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.current', [i for i in range(566, 700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.current', [i for i in range(572, 700, 12)]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.previous', [930, 992, 1006, 1018, 1030, 1042, 1056, 1068, 1080, 1092, 1106, 1118, 1130, 1142, 1168, 1180, 1953, 1960, 1966]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1978, 1990, 2003, 2010, 2016, 2028, 2040, 2053, 2060, 2066, 2078, 2090, 2103, 2110, 2116, 2128, 2140, 2153, 2166]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t01w_240_9', [17, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t01w_240_9', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t01w_240_15', [40, 61, 64, 65, 67, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t01w_240_17', [18, 19, 20, 22, 23, 28, 43, 44, 46, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t01w_240_18', [27, 30, 31, 32, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t01w_240_18', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t01w_240_19', [16, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t01w_240_19', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t01w_240_19', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t01w_240_20', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t01w_240_20', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t01w_240_20', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t01w_240_21', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t01w_240_21', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t01w_240_21', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t01w_240_22', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t01w_240_22', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t01w_240_22', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t01w_240_23', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t01w_240_23', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t01w_240_23', [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t01w_240_24', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t01w_240_24', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t01w_240_24', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t01w_240_24', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t01w_240_24', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t01w_240_25', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t01w_240_25', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t01w_240_25', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t01w_240_25', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t01w_240_26', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t01w_240_26', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t01w_240_26', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t01w_240_27', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t01w_240_27', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t01w_240_27', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t01w_240_27', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t01w_240_28', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t01w_240_28', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t01w_240_28', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/t01w_240_28', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]