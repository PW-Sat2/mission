tasks = [
    # ============================================================================
    # Energy-saving session on 9600
    # ============================================================================

    ["Session 139", Print, WaitMode.NoWait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 136 and 139
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(506, 1965, 60)]), Send, WaitMode.Wait],

    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(515, 1965, 60)]), Send, WaitMode.Wait],

    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(521, 1965, 60)]), Send, WaitMode.Wait],

    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(531, 1965, 60)]), Send, WaitMode.Wait],

    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(544, 1965, 60)]), Send, WaitMode.Wait],


    # Telemetry between session 136 and 138 - missing from previous session
    [tc.DownloadFile(200, '/telemetry.current', [501, 502, 504, 505, 507, 508, 510, 511, 512, 513, 514, 519, 522, 523, 524, 550, 562, 587, 600, 1935]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.current', [612, 637, 656, 662, 687, 712, 737, 762, 800, 812, 825, 837, 850, 862, 887, 912, 937, 956, 962, 987, 1006]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.current', [1012, 1034, 1066, 1075, 1100, 1112, 1137, 1150, 1162, 1212, 1218, 1262, 1275, 1280, 1306, 1318, 1400, 1412, 1462, 1512]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.current', [1336, 1753, 1555, 1575, 1580, 1606, 1618, 1630, 1637, 1650, 1667, 1687, 1697, 1712, 1737, 1762, 1812, 1862]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]