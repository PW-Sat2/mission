tasks = [
    # Generated on 2019-12-08 21:10:31.705000, contains telemetry from sessions 2397 to 2398.
    # The session starts on 2019-12-08 21:55:50+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(45, '/telemetry.current', [686, 736, 786, 836, 886, 711, 761, 811, 861, 699, 749, 799, 849, 899, 723, 773, 823, 873, 693, 743]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [793, 843, 893, 705, 755, 805, 855, 905, 717, 767, 817, 867, 729, 779, 829, 879]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/t01w_240_21', [69]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t01w_240_22', [20, 24, 29, 30, 32, 33, 34, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t01w_240_25', [45, 49, 52, 53, 54, 55, 56, 57, 59, 60, 62, 63, 65, 67, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t01w_240_25', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t01w_240_26', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t01w_240_26', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t01w_240_26', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t01w_240_27', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t01w_240_27', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t01w_240_27', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t01w_240_27', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t01w_240_28', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t01w_240_28', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t01w_240_28', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t01w_240_28', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
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


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]