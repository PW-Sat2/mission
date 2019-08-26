tasks = [
    # Generated on 2019-08-26 12:18:32.688856, contains telemetry from sessions 1724 to 1725.
    # The session starts on 2019-08-26 13:22:39+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(20, '/telemetry.current', [880, 930, 980, 1030, 1080, 905, 955, 1005, 1055, 893, 943, 993, 1043, 1093, 917, 967, 1017, 1067, 887, 937]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [987, 1037, 1087, 899, 949, 999, 1049, 1099, 911, 961, 1011, 1061, 923, 973, 1023, 1073]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/t17w_128_0', [24]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t12w_480_0', [49, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t13w_128_0', [32]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t14w_128_0', [6]), Send, WaitMode.Wait],
    # missing from previous session end


    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]