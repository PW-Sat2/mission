tasks = [
    # Generated on 2021-01-24 09:32:45.195000, contains telemetry from sessions 5031 to 5032.
    # The session starts on 2021-01-24 10:38:48+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(48, '/telemetry.previous', [1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 1918, 1968, 2018, 2068, 2118]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 0, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 38, 88, 138]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [2168, 2218, 2268, 1942, 1992, 2042, 2092, 2142, 2192, 2242, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1924, 1974]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788, 838, 888, 12, 62, 112, 162, 212]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [262, 312, 362, 412, 462, 512, 562, 612, 662, 712, 762, 812, 862, 32, 82, 132, 182, 232, 282, 332]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 44, 94, 144, 194, 244, 294, 344, 394, 444]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [2024, 2074, 2124, 2174, 2224, 2274, 1936, 1986, 2036, 2086, 2136, 2186, 2236, 1948, 1998, 2048, 2098, 2148, 2198, 2248]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [494, 544, 594, 644, 694, 744, 794, 844, 894, 6, 56, 106, 156, 206, 256, 306, 356, 406, 456, 506]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [556, 606, 656, 706, 756, 806, 856, 18, 68, 118, 168, 218, 268, 318, 368, 418, 468, 518, 568, 618]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [668, 718, 768, 818, 868]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file download start
    [tc.DownloadFile(59, '/radfet_57', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    # auto-generated file download end

    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_19', [80, 123, 124, 147, 171, 172, 173, 198, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_19', [211, 212, 217, 218, 219, 222, 223, 224, 225, 242, 243, 244, 267, 268, 269, 270, 313, 315, 318]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_19', [329, 330, 331, 332, 343, 346, 350, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_19', [364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 383, 384, 385, 386]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p2_n_p480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p0_n_p480_0', [8, 10, 11, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p0_n_p480_0', [72, 74, 75, 76, 77, 78, 92, 106, 107, 139, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p1_w_p480_0', [20, 40, 51, 54, 56, 59, 60, 62, 64, 65, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p1_w_p480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p2_n_p480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p2_n_p480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 73, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p3_w_p480_0', [25, 26, 27, 28, 29, 30, 31, 32, 33, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p3_w_p480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p3_w_p480_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p3_w_p480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p3_w_p480_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p3_w_p480_0', [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p3_w_p480_0', [146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait],
    # missing from previous session end



    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]