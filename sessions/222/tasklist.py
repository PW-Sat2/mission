tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(2), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [437, 487, 537, 587, 637, 687, 737, 787, 837, 887, 937, 987, 1037, 1087, 1137, 1187, 1237, 1287, 1337, 1387]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 462, 512, 562, 612, 662, 712, 762, 812, 862, 912]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [962, 1012, 1062, 1112, 1162, 1212, 1262, 1312, 1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]