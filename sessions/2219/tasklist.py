tasks = [
    # Generated on 2019-11-11 20:27:06.862000, contains telemetry from sessions 2218 to 2219.
    # The session starts on 2019-11-11 21:42:20+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(48, '/telemetry.current', [875, 925, 975, 1025, 1075, 900, 950, 1000, 1050, 888, 938, 988, 1038, 1088, 912, 962, 1012, 1062, 882, 932]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [982, 1032, 1082, 894, 944, 994, 1044, 906, 956, 1006, 1056, 918, 968, 1018, 1068]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(32, '/t10w_480_0', [77]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t15n_480_0', [16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t17w_480_0', [23, 66, 67, 84, 85, 90, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t18n_480_0', [49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t18w_480_0', [20, 35, 38, 43, 44, 45, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t18w_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t21w_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t21w_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t21w_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t21w_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t07w_480_0', [51, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t07w_480_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t07w_480_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t14w_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t14w_480_0', [79, 87, 97, 99, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 131, 138]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t14w_480_0', [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]), Send, WaitMode.Wait],
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