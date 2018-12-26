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

    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(537, 1965, 60)]), Send, WaitMode.Wait],


    # Telemetry between session 136 and 138 - missing from previous session
    [tc.DownloadFile(200, '/telemetry.current', [501, 502, 504, 505, 507, 508, 510, 511, 512, 513, 514, 519, 522, 523, 524, 550, 562, 575, 587, 600]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.current', [612, 637, 650, 662, 687, 712, 737, 762, 800, 812, 825, 837, 862, 887, 912, 937, 950, 962, 987, 1000]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.current', [1012, 1062, 1075, 1100, 1112, 1137, 1162, 1175, 1212, 1225, 1262, 1275, 1287, 1300, 1312, 1362, 1400, 1412, 1462, 1512]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.current', [1550, 1562, 1575, 1587, 1600, 1612, 1625, 1637, 1650, 1662, 1687, 1712, 1737, 1762, 1775, 1812, 1862]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]