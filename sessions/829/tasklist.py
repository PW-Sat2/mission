tasks = [
    # Generated on 2019-04-09 21:16:07.708000, contains telemetry from sessions 828 to 829.
    # The session starts on 2019-04-09 22:30:34+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1745, 1795, 1845, 1895, 1945, 1770, 1820, 1870, 1920, 1758, 1808, 1858, 1908, 1958, 1782, 1832, 1882, 1932, 1752, 1802]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1852, 1902, 1952, 1764, 1814, 1864, 1914, 1964, 1776, 1826, 1876, 1926, 1788, 1838, 1888, 1938]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.RemoveFile(41, 'p9_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(42, 'suns_ps_3_sec'), Send, WaitMode.NoWait],
    [tc.RemoveFile(43, 'telemetry.previous'), Send, WaitMode.Wait],

    [tc.ListFiles(105, '/'), Send, WaitMode.Wait],

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