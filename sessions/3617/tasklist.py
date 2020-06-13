tasks = [
    # Generated on 2020-06-13 11:52:34.562000, contains telemetry from sessions 3616 to 3617.
    # The session starts on 2020-06-13 12:52:51+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [2, 52, 102, 152, 202, 27, 77, 127, 177, 15, 65, 115, 165, 215, 39, 89, 139, 189, 9, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [109, 159, 209, 21, 71, 121, 171, 221, 33, 83, 133, 183, 45, 95, 145, 195]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    [tc.DownloadFile(23, '/radfet_40', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],


    [tc.DownloadFile(100, '/p1_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p1_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p1_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p1_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p1_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p1_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p1_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p1_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(110, '/p2_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p2_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/p2_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/p2_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/p2_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/p2_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/p2_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/p2_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(120, '/p3_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/p3_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/p3_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/p3_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/p3_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/p3_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/p3_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/p3_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(130, '/p4_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/p4_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/p4_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/p4_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/p4_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/p4_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/p4_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/p4_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(140, '/p5_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/p5_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(142, '/p5_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(143, '/p5_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(144, '/p5_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(145, '/p5_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(146, '/p5_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(147, '/p5_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(150, '/p6_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/p6_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(152, '/p6_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/p6_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(154, '/p6_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(155, '/p6_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(156, '/p6_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(157, '/p6_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(160, '/p7_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(161, '/p7_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(162, '/p7_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(163, '/p7_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(164, '/p7_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(165, '/p7_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(166, '/p7_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(167, '/p7_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(170, '/p8_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(171, '/p8_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(172, '/p8_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(173, '/p8_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(174, '/p8_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(175, '/p8_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(176, '/p8_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(177, '/p8_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(180, '/p9_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(181, '/p9_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(182, '/p9_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(183, '/p9_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(184, '/p9_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(185, '/p9_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(186, '/p9_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(187, '/p9_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(190, '/p10_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(191, '/p10_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(192, '/p10_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(193, '/p10_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(194, '/p10_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(195, '/p10_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(196, '/p10_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(197, '/p10_0', range(140, 160)), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]