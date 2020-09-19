tasks = [
    # Generated on 2020-09-19 22:04:39.476000, contains telemetry from sessions 4246 to 4247.
    # The session starts on 2020-09-19 23:17:51+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [14, 64, 114, 164, 214, 39, 89, 139, 189, 27, 77, 127, 177, 227, 51, 101, 151, 201, 21, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [121, 171, 221, 33, 83, 133, 183, 45, 95, 145, 195, 57, 107, 157, 207]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(132, '/radfet_47', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(32, '/t_n_21_52_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t_n_21_52_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/t_w_21_52_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t_w_21_52_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/t_w_21_53_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t_n_21_53_0', range(0, 20)), Send, WaitMode.Wait],    

    [tc.DownloadFile(34, '/t_n_21_52_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t_n_21_52_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t_n_21_52_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t_n_21_52_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t_n_21_52_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t_n_21_52_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/t_w_21_52_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t_w_21_52_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    # auto-generated file download end

    [tc.DownloadFile(66, '/t_w_21_53_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t_n_21_53_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/t_w_21_53_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t_n_21_53_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(74, '/t_w_21_53_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t_n_21_53_0', range(60, 80)), Send, WaitMode.Wait],

    [tc.DownloadFile(78, '/t_w_21_53_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t_n_21_53_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(82, '/t_w_21_53_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/t_n_21_53_0', range(100, 120)), Send, WaitMode.Wait],

    [tc.DownloadFile(86, '/t_w_21_53_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/t_n_21_53_0', range(120, 140)), Send, WaitMode.Wait],
    
    [tc.DownloadFile(90, '/t_w_21_53_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/t_n_21_53_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(95, '/t_w_21_53_0', range(160, 170)), Send, WaitMode.Wait],

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