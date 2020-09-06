tasks = [
    # Generated on 2020-09-07 00:03:43.719000, contains telemetry from sessions 4164 to 4165.
    # The session starts on 2020-09-07 00:58:52+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(31, '/m_w_11_41_0', [151, 159, 162, 163, 165, 166, 167]), Send, WaitMode.Wait],

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [1850, 1900, 1950, 2000, 2050, 1875, 1925, 1975, 2025, 1863, 1913, 1963, 2013, 2063, 1887, 1937, 1987, 2037, 1857, 1907]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1957, 2007, 2057, 1869, 1919, 1969, 2019, 2069, 1881, 1931, 1981, 2031, 1893, 1943, 1993, 2043, 1684]), Send, WaitMode.Wait],
    # auto-generated telemetry end
       


    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]