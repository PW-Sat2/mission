tasks = [
    [[tc.SetBitrate(10, BaudRate.BaudRate9600), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(11, '/'), Send, WaitMode.Wait],

    # Telemetry between session 66 and 67
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1100, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1104, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1108, 1300, 12)]), Send, WaitMode.Wait],

    # Missing SunS experiment 3 secondary file
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(15, '/suns_3_sec', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/suns_3_sec', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/suns_3_sec', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/suns_3_sec', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],

    # Remove photos - with no wait - experimental
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(19, '/p14_480_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(20, '/p15_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(21, '/p8_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(22, '/suns_3'), Send, WaitMode.NoWait],

    [tc.ListFiles(23, '/'), Send, WaitMode.Wait],

    # Much more telemetry between session 64 and 65 (over SAA)
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(176, '/telemetry.current', [i for i in range(302, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(177, '/telemetry.current', [i for i in range(306, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(178, '/telemetry.current', [i for i in range(310, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(179, '/telemetry.current', [i for i in range(314, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(180, '/telemetry.current', [i for i in range(322, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(181, '/telemetry.current', [i for i in range(326, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(182, '/telemetry.current', [i for i in range(330, 1150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(183, '/telemetry.current', [i for i in range(332, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(184, '/telemetry.current', [i for i in range(334, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(185, '/telemetry.current', [i for i in range(338, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(186, '/telemetry.current', [i for i in range(340, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(187, '/telemetry.current', [i for i in range(342, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(189, '/telemetry.current', [i for i in range(346, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(190, '/telemetry.current', [i for i in range(348, 1150, 50)]), Send, WaitMode.Wait],

    # More telemetry between session 66 and 67
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(200, '/telemetry.current', [i for i in range(1101, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.current', [i for i in range(1102, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.current', [i for i in range(1103, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.current', [i for i in range(1105, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(204, '/telemetry.current', [i for i in range(1106, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(205, '/telemetry.current', [i for i in range(1107, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(206, '/telemetry.current', [i for i in range(1109, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(207, '/telemetry.current', [i for i in range(1110, 1300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(208, '/telemetry.current', [i for i in range(1111, 1300, 12)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
