tasks = [
    # Generated on 2020-12-26 11:59:04.362000, contains telemetry from sessions 4860 to 4861.
    # The session starts on 2020-12-26 12:50:11+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [5, 55, 105, 155, 205, 30, 80, 130, 180, 18, 68, 118, 168, 218, 42, 92, 142, 192, 12, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [112, 162, 212, 24, 74, 124, 174, 36, 86, 136, 186, 48, 98, 148, 198]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # download experiment and photos

    [tc.DownloadFile(33, '/radfet_55', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/a_w_p480_11_22_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_n_p480_11_22_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a_w_p480_11_26_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a_n_p480_11_26_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a_w_p480_11_32_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a_n_p480_11_32_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/a_w_p480_11_40_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/a_n_p480_11_40_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/a_w_p480_11_52_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/a_n_p480_11_52_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/a_w_p480_11_56_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/a_n_p480_11_56_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/a_w_p480_12_00_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/a_n_p480_12_00_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/a_w_p480_12_04_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/a_n_p480_12_04_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/a_w_p480_11_22_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a_n_p480_11_22_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_w_p480_11_26_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a_n_p480_11_26_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_w_p480_11_32_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_n_p480_11_32_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/a_w_p480_11_40_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/a_n_p480_11_40_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/a_w_p480_11_52_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/a_n_p480_11_52_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/a_w_p480_11_56_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/a_n_p480_11_56_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/a_w_p480_12_00_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/a_n_p480_12_00_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/a_w_p480_12_04_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/a_n_p480_12_04_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/a_w_p480_11_22_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a_n_p480_11_22_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/a_w_p480_11_26_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/a_n_p480_11_26_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/a_w_p480_11_32_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/a_n_p480_11_32_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/a_w_p480_11_40_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/a_n_p480_11_40_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/a_w_p480_11_52_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/a_n_p480_11_52_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/a_w_p480_11_56_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/a_n_p480_11_56_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/a_w_p480_12_00_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/a_n_p480_12_00_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/a_w_p480_12_04_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/a_n_p480_12_04_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/a_w_p480_11_22_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/a_n_p480_11_22_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/a_w_p480_11_26_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/a_n_p480_11_26_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/a_w_p480_11_32_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/a_n_p480_11_32_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/a_w_p480_11_40_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/a_n_p480_11_40_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/a_w_p480_11_52_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/a_n_p480_11_52_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/a_w_p480_11_56_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/a_n_p480_11_56_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/a_w_p480_12_00_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/a_n_p480_12_00_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/a_w_p480_12_04_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/a_n_p480_12_04_0', range(60, 80)), Send, WaitMode.Wait],



    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]