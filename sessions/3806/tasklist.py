tasks = [
    # Generated on 2020-07-12 23:14:16.486000, contains telemetry from sessions 3805 to 3806.
    # The session starts on 2020-07-13 00:32:32+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1528, 1578, 1628, 1678, 1728, 1553, 1603, 1653, 1703, 1541, 1591, 1641, 1691, 1741, 1565, 1615, 1665, 1715, 1535, 1585]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1635, 1685, 1735, 1547, 1597, 1647, 1697, 1747, 1559, 1609, 1659, 1709, 1571, 1621, 1671, 1721]), Send, WaitMode.Wait],
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