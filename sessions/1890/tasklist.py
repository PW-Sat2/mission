tasks = [
    # Generated on 2019-09-22 23:19:50.046000, contains telemetry from sessions 1889 to 1890.
    # The session starts on 2019-09-23 00:04:14+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [875, 925, 975, 1025, 1075, 900, 950, 1000, 1050, 1100, 888, 938, 988, 1038, 1088, 912, 962, 1012, 1062, 882]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [932, 982, 1032, 1082, 894, 944, 994, 1044, 1094, 906, 956, 1006, 1056, 918, 968, 1018, 1068]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/t13w_480_0', [135]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t14w_480_0', [105, 130]), Send, WaitMode.Wait],
    # missing from previous session end


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