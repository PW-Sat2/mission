tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Remove downloaded photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(100, '/p1_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, '/p2_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(102, '/p3_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(104, '/p5_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(105, '/p6_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(106, '/p7_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(107, '/p8_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(108, '/p9_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(109, '/p10_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(110, '/p5_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(111, '/p6_480_0'), Send, WaitMode.NoWait],

    # Power cycle EPS B
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(6, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(7, '/'), Send, WaitMode.Wait],

    # Telemetry between session 182 and 183
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(0, 900, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(2170, 2280, 6)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(24, 900, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(12, 900, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(36, 900, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(6, 900, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(18, 900, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(30, 900, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(42, 900, 48)]), Send, WaitMode.Wait],

    # High res photos missings
    [tc.DownloadFile(21, '/p4_480_0', [105]), Send, WaitMode.Wait],

    [tc.DownloadFile(21, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p1_480_0', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p1_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/p1_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/p1_480_0', [75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],

    [tc.DownloadFile(26, '/p2_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/p2_480_0', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/p2_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/p2_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p2_480_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],

    [tc.DownloadFile(31, '/p3_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p3_480_0', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p3_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p3_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p3_480_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p3_480_0', [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]