tasks = [
    # Generated on 2020-08-08 11:43:34.434000, contains telemetry from sessions 3974 to 3975.
    # The session starts on 2020-08-08 12:55:16+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current',
                     [6, 56, 106, 156, 206, 31, 81, 131, 181, 19, 69, 119, 169, 219, 43, 93, 143, 193, 13, 63]), Send,
     WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current',
                     [113, 163, 213, 25, 75, 125, 175, 225, 37, 87, 137, 187, 49, 99, 149, 199]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(60, '/a_w_11_30_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a_n_11_30_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/a_w_11_31_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/a_n_11_31_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/a_w_11_32_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/a_n_11_32_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/a_w_11_40_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/a_n_11_40_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/a_w_11_41_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/a_n_11_41_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/a_w_11_42_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/a_n_11_42_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/a_w_11_57_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/a_n_11_57_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/a_w_11_58_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/a_n_11_58_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/a_w_11_59_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/a_n_11_59_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/a_w_12_59_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/a_n_12_59_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/a_w_13_00_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/a_n_13_00_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/a_w_13_01_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/a_n_13_01_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(80, '/a_w_11_30_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/a_n_11_30_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/a_w_11_31_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/a_n_11_31_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/a_w_11_32_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/a_n_11_32_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/a_w_11_40_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/a_n_11_40_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/a_w_11_41_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/a_n_11_41_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/a_w_11_42_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/a_n_11_42_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/a_w_11_57_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/a_n_11_57_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/a_w_11_58_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/a_n_11_58_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/a_w_11_59_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/a_n_11_59_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/a_w_12_59_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/a_n_12_59_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/a_w_13_00_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/a_n_13_00_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/a_w_13_01_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/a_n_13_01_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(100, '/a_w_11_30_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/a_n_11_30_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/a_w_11_31_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/a_n_11_31_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/a_w_11_32_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/a_n_11_32_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/a_w_11_40_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/a_n_11_40_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/a_w_11_41_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/a_n_11_41_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/a_w_11_42_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/a_n_11_42_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/a_w_11_57_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/a_n_11_57_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/a_w_11_58_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/a_n_11_58_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/a_w_11_59_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/a_n_11_59_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/a_w_12_59_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/a_n_12_59_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/a_w_13_00_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/a_n_13_00_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(130, '/a_w_13_01_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/a_n_13_01_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(132, '/radfet_44', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
