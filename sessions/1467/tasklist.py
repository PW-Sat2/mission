tasks = [
    # Generated on 2019-07-14 12:09:37.593000, contains telemetry from sessions 1466 to 1467.
    # The session starts on 2019-07-14 13:07:33+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(45, '/telemetry.current', [371, 421, 471, 521, 571, 396, 446, 496, 546, 384, 434, 484, 534, 584, 408, 458, 508, 558, 378, 428]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [478, 528, 578, 390, 440, 490, 540, 590, 402, 452, 502, 552, 414, 464, 514, 564]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing from previous session start
    [tc.DownloadFile(30, '/p52_128_16', [16, 17, 19, 21, 22, 23, 25, 29, 30, 31, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2025, 2032, 2039, 2057, 2175, 2189, 2195, 2201, 2207, 2213, 2232, 2245, 2275]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p24_128_0', [20, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_9', [7, 19, 20, 26, 27, 28, 29, 32, 34, 35, 44, 48, 53, 54, 83, 84, 85, 86, 103, 104]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_9', [106, 107, 108, 109, 110, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 124, 125, 127, 128, 129]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_9', [130, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_9', [153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/suns_ps_9', [173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_9', [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/suns_ps_9', [212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_9', [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p41_128_0', [4, 5]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p20_128_0', [25]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p27_128_0', [0, 3, 4, 6, 7, 8]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(70, '/p52_128_0', [i for i in range(35, 37)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p52_128_10', [i for i in range(35, 37)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p52_128_15', [i for i in range(35, 37)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p52_128_20', [i for i in range(35, 37)]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/p52_128_25', [i for i in range(35, 37)]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/p52_128_5', [i for i in range(35, 36)]), Send, WaitMode.Wait],

    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]