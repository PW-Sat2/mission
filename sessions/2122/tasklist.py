tasks = [
    # Generated on 2019-10-28 10:21:11.008000, contains telemetry from sessions 2121 to 2122.
    # The session starts on 2019-10-28 11:23:54+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1799, 1849, 1899, 1949, 1999, 1824, 1874, 1924, 1974, 1812, 1862, 1912, 1962, 2012, 1836, 1886, 1936, 1986, 1806, 1856]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1906, 1956, 2006, 1818, 1868, 1918, 1968, 2018, 1830, 1880, 1930, 1980, 1842, 1892, 1942, 1992]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

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