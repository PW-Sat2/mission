tasks = [
    # Generated on 2019-06-30 22:29:43.037000, contains telemetry from sessions 1383 to 1384.
    # The session starts on 2019-06-30 23:47:27+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1562, 1612, 1662, 1712, 1762, 1587, 1637, 1687, 1737, 1575, 1625, 1675, 1725, 1775, 1599, 1649, 1699, 1749, 1569, 1619]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1669, 1719, 1769, 1581, 1631, 1681, 1731, 1781, 1593, 1643, 1693, 1743, 1605, 1655, 1705, 1755]), Send, WaitMode.Wait],
    # auto-generated telemetry end

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
