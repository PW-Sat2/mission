tasks = [
    [[tc.SetBitrate(26, 8), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(23, '/'), Send, WaitMode.Wait],
    
    # Telemetry between session 40 and 41
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1950, 2200, 15)]), Send, WaitMode.Wait],

    # Dense telemetry from past sessions
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(1150, 2100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1125, 2100, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(1112, 2100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(1137, 2100, 50)]), Send, WaitMode.Wait],

    # Beacon for fun and profit
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Download photo p4_480_0
    [tc.DownloadFile(40, '/p4_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p4_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p4_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p4_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],

    # Beacon for fun and profit
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Download photo p5_480_0
    [tc.DownloadFile(50, '/p5_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p5_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p5_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait], 
    [tc.DownloadFile(53, '/p5_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p5_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p5_480_0', [104, 105, 106, 108, 111, 112, 114, 119, 124, 130]), Send, WaitMode.Wait],

    # Beacon for fun and profit
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Moar oldie telemetry mate!
    [tc.DownloadFile(60, '/telemetry.previous', [i for i in range(1900, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.previous', [i for i in range(1950, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.previous', [i for i in range(1925, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.previous', [i for i in range(1912, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.previous', [i for i in range(1937, 2280, 50)]), Send, WaitMode.Wait],
    
    # Beacon for goodbye
    [tc.SendBeacon(), Send, WaitMode.Wait],
]
