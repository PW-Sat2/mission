tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 175 and 176
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1640, 1820, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1643, 1820, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Telemetry around SADS deployment
    [tc.DownloadFile(12, '/telemetry.current', [1641, 1642, 1644, 1645, 1647, 1648, 1650, 1651, 1653, 1654]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [1656, 1657, 1659, 1660, 1662, 1663, 1665, 1666, 1668, 1669]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # More telemetry between session 175 and 176
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1646, 1820, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(1649, 1820, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["More Telemetry between session 174 and 175", Print, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(408, 1700, 72)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(420, 1700, 72)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(432, 1700, 72)]), Send, WaitMode.Wait],


    ["SADS photo", Print, WaitMode.Wait],
    [tc.DownloadFile(100, '/sads.photo_wing', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/sads.photo_wing', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/sads.photo_wing', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/sads.photo_wing', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/sads.photo_wing', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/sads.photo_wing', [i for i in range(125, 150, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/sads.photo_wing', [i for i in range(150, 175, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(31, '/sads.exp', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
