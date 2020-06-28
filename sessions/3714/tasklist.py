tasks = [
    # Generated on 2020-06-28 13:35:05.503000, contains telemetry from sessions 3712 to 3714.
    # The session starts on 2020-06-28 20:57:10+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(44, '/telemetry.current', [350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 375, 425]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 363, 413, 463, 513]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 387, 437, 487, 537, 587, 637]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [687, 737, 787, 837, 887, 937, 987, 1037, 1087, 1137, 1187, 1237, 357, 407, 457, 507, 557, 607, 657, 707]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [869, 919, 969, 1019, 1069, 1119, 1169, 1219, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [981, 1031, 1081, 1131, 1181, 1231, 393, 443, 493, 543, 593, 643, 693, 743, 793, 843, 893, 943, 993, 1043]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1093, 1143, 1193]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(145, '/a_n_17_00_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/dummy_15_33_0', [80, 100, 102, 104, 107, 114, 115, 116, 117, 118, 119, 120, 121, 122]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/dummy_15_33_0', [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/dummy_16_33_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/dummy_16_33_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/dummy_16_33_0', [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/dummy_16_33_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/dummy_16_33_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/dummy_16_33_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/dummy_18_04_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/dummy_18_04_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/dummy_18_04_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/dummy_18_04_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/dummy_18_04_0', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    # DEEP SLEEP
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