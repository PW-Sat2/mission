tasks = [
    # Generated on 2020-04-11 12:14:24.902000, contains telemetry from sessions 3207 to 3208.
    # The session starts on 2020-04-11 13:15:14+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [5, 55, 105, 155, 205, 30, 80, 130, 180, 18, 68, 118, 168, 218, 42, 92, 142, 192, 12, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [112, 162, 212, 24, 74, 124, 174, 224, 36, 86, 136, 186, 48, 98, 148, 198]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end

    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=3), 5, datetime.timedelta(seconds=10), 'suns_ps_17'), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/radfet_36', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(41, '/p1_128_0', [2, 3, 4, 5, 6, 14, 23, 25]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/p2_128_0', range(0, 30)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p3_128_0', range(0, 30)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p4_128_0', range(0, 30)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p5_128_0', range(0, 30)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p6_128_0', range(0, 30)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p7_128_0', range(0, 30)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p8_128_0', range(0, 30)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p9_128_0', range(0, 30)), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p10_128_0', range(0, 30)), Send, WaitMode.Wait],

    [tc.DownloadFile(51, '/p1_480_0', [2, 3, 4, 7, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p1_480_0', [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p1_480_0', [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p1_480_0', [64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p1_480_0', [83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p1_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p1_480_0', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p1_480_0', [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]), Send, WaitMode.Wait],


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
