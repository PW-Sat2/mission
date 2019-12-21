tasks = [
    # Generated on 2019-12-21 10:44:43.015000, contains telemetry from sessions 2475 to 2476.
    # The session starts on 2019-12-21 11:53:10+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [2, 52, 102, 152, 202, 27, 77, 127, 177, 15, 65, 115, 165, 215, 39, 89, 139, 189, 9, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [109, 159, 209, 21, 71, 121, 171, 221, 33, 83, 133, 183, 45, 95, 145, 195]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_28'), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/t01w_240_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t01w_240_1', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t01w_240_2', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t01w_240_3', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t01w_240_4', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t01w_240_5', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t01w_240_6', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t01w_240_7', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t01w_240_8', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t01w_240_9', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t01w_240_10', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t01w_240_11', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t01w_240_12', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t01w_240_13', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t01w_240_14', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t01w_240_15', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t01w_240_16', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t01w_240_17', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t01w_240_18', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t01w_240_19', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t01w_240_20', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t01w_240_21', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t01w_240_22', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t01w_240_23', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t01w_240_24', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t01w_240_25', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t01w_240_26', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t01w_240_27', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t01w_240_28', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/t02w_240_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t02w_240_1', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t02w_240_2', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t02w_240_3', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t02w_240_4', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t02w_240_5', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t02w_240_6', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t02w_240_7', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t02w_240_8', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t02w_240_9', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/t02w_240_10', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/t02w_240_11', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/t02w_240_12', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/t02w_240_13', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/t02w_240_14', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/t02w_240_15', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/t02w_240_16', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/t02w_240_17', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/t02w_240_18', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/t02w_240_19', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/t02w_240_20', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/t02w_240_21', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/t02w_240_22', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/t02w_240_23', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/t02w_240_24', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/t02w_240_25', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/t02w_240_26', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/t02w_240_27', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/t02w_240_28', range(0, 20)), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]