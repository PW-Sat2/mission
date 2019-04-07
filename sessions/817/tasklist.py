tasks = [
    # Generated on 2019-04-07 21:21:11.255000, contains telemetry from sessions 816 to 817.
    # The session starts on 2019-04-07 22:23:40+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1568, 1618, 1668, 1718, 1768, 1593, 1643, 1693, 1743, 1581, 1631, 1681, 1731, 1781, 1605, 1655, 1705, 1755, 1575, 1625]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1675, 1725, 1775, 1587, 1637, 1687, 1737, 1787, 1599, 1649, 1699, 1749, 1611, 1661, 1711, 1761, 620, 1462, 1488, 1562]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(41, 'p4_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(42, 'suns_ps_3'), Send, WaitMode.NoWait],
    [tc.RemoveFile(43, 'suns_ps_3_sec'), Send, WaitMode.Wait],

    # Going back to deep sleep
    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

     ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

     # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

     # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

     # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]