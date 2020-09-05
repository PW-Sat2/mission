tasks = [
    # Generated on 2020-09-05 11:35:51.015000, contains telemetry from sessions 4153 to 4154.
    # The session starts on 2020-09-05 12:52:04+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [169, 219, 269, 319, 369, 194, 244, 294, 344, 182, 232, 282, 332, 382, 206, 256, 306, 356, 176, 226]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [276, 326, 376, 188, 238, 288, 338, 388, 200, 250, 300, 350, 212, 262, 312, 362]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    [tc.DownloadFile(132, '/radfet_46', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/m_w_11_23_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/m_n_11_23_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/m_w_11_24_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/m_n_11_24_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/m_w_11_26_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/m_n_11_26_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/m_w_11_27_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/m_n_11_27_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/m_w_11_28_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/m_n_11_28_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/m_w_11_29_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/m_n_11_29_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/m_w_11_38_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/m_n_11_38_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/m_w_11_41_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/m_n_11_41_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/m_w_12_36_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/m_n_12_36_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/m_w_12_37_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/m_n_12_37_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/m_w_12_38_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/m_n_12_38_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/m_w_12_39_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/m_n_12_39_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(80, '/m_w_11_23_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/m_n_11_23_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/m_w_11_24_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/m_n_11_24_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/m_w_11_26_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/m_n_11_26_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/m_w_11_27_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/m_n_11_27_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/m_w_11_28_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/m_n_11_28_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/m_w_11_29_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/m_n_11_29_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/m_w_11_38_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/m_n_11_38_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/m_w_11_41_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/m_n_11_41_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/m_w_12_36_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/m_n_12_36_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/m_w_12_37_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/m_n_12_37_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/m_w_12_38_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/m_n_12_38_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/m_w_12_39_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/m_n_12_39_0', range(20, 40)), Send, WaitMode.Wait],

    [tc.DownloadFile(100, '/m_w_11_23_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/m_n_11_23_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/m_w_11_24_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/m_n_11_24_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/m_w_11_26_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/m_n_11_26_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/m_w_11_27_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/m_n_11_27_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/m_w_11_28_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/m_n_11_28_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/m_w_11_29_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/m_n_11_29_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/m_w_11_38_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/m_n_11_38_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/m_w_11_41_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/m_n_11_41_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/m_w_12_36_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/m_n_12_36_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/m_w_12_37_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/m_n_12_37_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/m_w_12_38_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/m_n_12_38_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(130, '/m_w_12_39_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/m_n_12_39_0', range(40, 60)), Send, WaitMode.Wait],


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end



    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]