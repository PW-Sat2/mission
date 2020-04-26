tasks = [
    # Generated on 2020-04-26 12:02:07.557661, contains telemetry from sessions 3305 to 3306.
    # The session starts on 2020-04-26 12:44:22+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(46, '/telemetry.current', [357, 407, 457, 507, 557, 382, 432, 482, 532, 370, 420, 470, 520, 570, 394, 444, 494, 544, 364, 414]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [464, 514, 564, 376, 426, 476, 526, 576, 388, 438, 488, 538, 400, 450, 500, 550]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [36, 99, 117, 149, 243, 329]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1379, 1435, 1479, 1503, 1535, 1566, 1603, 1609, 1616, 1653, 1659, 1666, 2191, 2273, 2279]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t4w_480_0', [118]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t5n_480_0', [38, 43, 53, 75, 76, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t5w_480_0', [35]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a1w_480_0', [36, 37, 47, 48, 49, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a1w_480_0', [68, 69, 70, 71, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a1w_480_0', [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a1w_480_0', [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a1n_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a1n_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a1n_480_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a1n_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a1n_480_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a1n_480_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a1n_480_0', [130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]