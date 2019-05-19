tasks = [
    # Generated on 2019-05-19 21:24:47.931000, contains telemetry from sessions 1091 to 1092.
    # The session starts on 2019-05-19 22:42:14+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],


    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_4', [86, 88, 89, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_4', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    # missing from previous session end

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [1571, 1621, 1671, 1721, 1771, 1596, 1646, 1696, 1746, 1584, 1634, 1684, 1734, 1784, 1608, 1658, 1708, 1758, 1578, 1628]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1678, 1728, 1778, 1590, 1640, 1690, 1740, 1790, 1602, 1652, 1702, 1752, 1614, 1664, 1714, 1764]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]