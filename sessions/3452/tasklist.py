tasks = [
    # Generated on 2020-05-18 22:04:53.415000, contains telemetry from sessions 3451 to 3452.
    # The session starts on 2020-05-18 23:19:22+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1855, 1905, 1955, 2005, 2055, 1880, 1930, 1980, 2030, 1868, 1918, 1968, 2018, 2068, 1892, 1942, 1992, 2042, 1862, 1912]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1962, 2012, 2062, 1874, 1924, 1974, 2024, 2074, 1886, 1936, 1986, 2036, 1898, 1948, 1998, 2048]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    [tc.DownloadFile(34, '/telemetry.current', [968, 1868, 1893, 1881, 1855, 1875, 1887, 1899, 1861]), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(30, '/m9w_480_0', [112, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    # When everything is downloaded, switch to deep-sleep
    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(6), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]