tasks = [
    # Generated on 2020-08-09 11:27:23.598000, contains telemetry from sessions 3981 to 3982.
    # The session starts on 2020-08-09 12:42:10+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(63, '/telemetry.current', [354, 404, 454, 504, 554, 379, 429, 479, 529, 367, 417, 467, 517, 567, 391, 441, 491, 541, 361, 411]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [461, 511, 561, 373, 423, 473, 523, 573, 385, 435, 485, 535, 397, 447, 497, 547]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],
    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],
    
    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [330, 380]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2010, 2060, 2110, 2160, 2210, 2260]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a_n_11_32_0', [53, 54, 55, 106]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/a_n_11_40_0', [61, 62, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_n_11_41_0', [41]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_w_11_31_0', [61, 77, 78, 79, 81, 83, 85, 87, 88, 89, 90, 91, 93, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_w_11_31_0', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_w_11_32_0', [20, 47, 48, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_w_11_40_0', [40, 41, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_w_11_40_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_w_11_40_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_w_11_40_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a_w_11_40_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a_w_11_40_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a_w_11_41_0', [28, 40, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a_w_11_41_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_w_11_42_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a_w_11_42_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a_w_11_42_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a_w_11_57_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a_w_11_57_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a_w_11_58_0', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_w_11_58_0', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a_w_11_58_0', [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_w_11_59_0', [25, 26, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_w_11_59_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/a_w_12_59_0', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/a_w_12_59_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/a_w_12_59_0', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_w_12_59_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/a_w_13_00_0', [70, 78, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a_w_13_01_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/a_w_13_01_0', [72, 73, 74, 75, 76, 80, 81, 103, 104, 105, 107, 108, 122, 125]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]