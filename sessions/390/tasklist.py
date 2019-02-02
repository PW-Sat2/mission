tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

     # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [305, 355, 405, 455, 505, 330, 380, 430, 480, 318, 368, 418, 468, 518, 342, 392, 442, 492, 312, 362]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [412, 462, 512, 324, 374, 424, 474, 524, 336, 386, 436, 486, 348, 398, 448, 498]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Missings from session 389
    [tc.DownloadFile(132, '/p7_128_0', [12]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/p9_128_0', [4, 7, 8, 9, 11, 12]), Send, WaitMode.Wait],
    
    # High res photos
    [tc.DownloadFile(50, '/p1_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p1_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p1_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p1_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p1_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p1_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p1_480_0', [i for i in range(120, 149, 1)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(60, '/p2_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p2_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p2_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p2_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p2_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p2_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p2_480_0', [i for i in range(120, 133, 1)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(70, '/p8_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p8_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p8_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p8_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p8_480_0', [i for i in range(80, 102, 1)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(80, '/p5_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p5_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p5_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p5_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/p5_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/p5_480_0', [i for i in range(100, 123, 1)]), Send, WaitMode.Wait],
    
    # Remove downloaded photos
    [tc.RemoveFile(100, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(101, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(102, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(103, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(104, '/p5_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(105, '/p6_128_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(106, '/p8_128_0'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]