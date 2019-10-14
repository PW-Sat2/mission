tasks = [
    # Generated on 2019-10-14 11:34:18.553000, contains telemetry from sessions 2028 to 2029.
    # The session starts on 2019-10-14 12:47:01+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [2147, 2197, 2247, 2172, 2222, 2272, 2160, 2210, 2260, 2184, 2234, 2154, 2204, 2254, 2166, 2216, 2266, 2178, 2228, 2278]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [17, 67, 42, 30, 80, 4, 54, 24, 74, 36, 86, 48, 10, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2190, 2240]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    # missing from previous session start
    [tc.DownloadFile(30, '/t24n_480_0', [47, 48, 49, 50, 52, 55, 56, 57, 58]), Send, WaitMode.Wait],
    # missing from previous session end



    # if good session:    
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