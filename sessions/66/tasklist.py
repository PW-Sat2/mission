tasks = [
    [[tc.SetBitrate(10, BaudRate.BaudRate9600), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(11, '/'), Send, WaitMode.Wait],

    # Telemetry between session 65 and 66
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(950, 1150, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(956, 1150, 12)]), Send, WaitMode.Wait],

    # Missing telemetry between session 60 and 00:00
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(930, 1350, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(942, 1350, 25)]), Send, WaitMode.Wait],

    # Missing telemetry between session 63 and 65
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(100, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(108, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(116, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(132, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(140, 1150, 50)]), Send, WaitMode.Wait],

    # SunS experiment 3 file
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(21, '/suns_3', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/suns_3', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/suns_3', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/suns_3', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/suns_3', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/suns_3', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(27, '/suns_3', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/suns_3', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/suns_3', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/suns_3', [i for i in range(180, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_3', [i for i in range(200, 220, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_3', [i for i in range(220, 240, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_3', [i for i in range(240, 250, 1)]), Send, WaitMode.Wait],

    # Some missing chunks in low res photos
    [tc.DownloadFile(98, '/p7_128_0', [5]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/p9_128_0', [6]), Send, WaitMode.Wait],

    # Remove photos
    [tc.RemoveFile(203, '/p4_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(204, '/p5_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(205, '/p6_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(106, '/p7_128_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(107, '/p8_128_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(108, '/p9_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(208, '/p9_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(209, '/p10_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(110, '/p11_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(210, '/p11_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(111, '/p12_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(211, '/p12_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(112, '/p13_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(212, '/p13_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(113, '/p14_128_0'), Send, WaitMode.Wait],
    # [tc.RemoveFile(213, '/p14_480_0'), Send, WaitMode.Wait], # pink sun 1

    [tc.RemoveFile(114, '/p15_128_0'), Send, WaitMode.Wait],
    # [tc.RemoveFile(214, '/p15_480_0'), Send, WaitMode.Wait], # pink sun 2

    [tc.RemoveFile(115, '/p16_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(215, '/p16_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(116, '/p17_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(216, '/p17_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(117, '/p18_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(217, '/p18_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(118, '/p19_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(218, '/p19_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(119, '/p20_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(219, '/p20_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(66, '/'), Send, WaitMode.Wait],

    # Hi res photos
    [tc.DownloadFile(220, '/p14_480_0', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(230, '/p14_480_0', [i for i in range(10, 20, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(221, '/p14_480_0', [i for i in range(20, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(231, '/p14_480_0', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(222, '/p14_480_0', [i for i in range(40, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(232, '/p14_480_0', [i for i in range(50, 60, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(223, '/p14_480_0', [i for i in range(60, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(233, '/p14_480_0', [i for i in range(70, 80, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(224, '/p14_480_0', [i for i in range(80, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(234, '/p14_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],


    [tc.DownloadFile(225, '/p15_480_0', [i for i in range(0, 11, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(235, '/p15_480_0', [i for i in range(11, 22, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(226, '/p15_480_0', [i for i in range(22, 33, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(236, '/p15_480_0', [i for i in range(33, 44, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(227, '/p15_480_0', [i for i in range(44, 55, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(237, '/p15_480_0', [i for i in range(55, 66, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(228, '/p15_480_0', [i for i in range(66, 77, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(238, '/p15_480_0', [i for i in range(77, 88, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 63 and 65
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(150, '/telemetry.current', [i for i in range(104, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/telemetry.current', [i for i in range(112, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(152, '/telemetry.current', [i for i in range(120, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/telemetry.current', [i for i in range(124, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(154, '/telemetry.current', [i for i in range(128, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(155, '/telemetry.current', [i for i in range(136, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(156, '/telemetry.current', [i for i in range(144, 1150, 50)]), Send, WaitMode.Wait],

    # More telemetry between 0:00 and session 62
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(157, '/telemetry.previous', [i for i in range(1358, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(158, '/telemetry.previous', [i for i in range(1368, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(159, '/telemetry.previous', [i for i in range(1376, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(160, '/telemetry.previous', [i for i in range(1382, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(161, '/telemetry.previous', [i for i in range(1390, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(162, '/telemetry.previous', [i for i in range(1395, 2280, 50)]), Send, WaitMode.Wait],

    # SunS experiment 3 secondary file
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(170, '/suns_3_sec', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(171, '/suns_3_sec', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(172, '/suns_3_sec', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(173, '/suns_3_sec', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(174, '/suns_3_sec', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(175, '/suns_3_sec', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],

    # Much more telemetry between session 64 and 65 (over SAA)
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(176, '/telemetry.current', [i for i in range(302, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(177, '/telemetry.current', [i for i in range(306, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(178, '/telemetry.current', [i for i in range(310, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(179, '/telemetry.current', [i for i in range(314, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(180, '/telemetry.current', [i for i in range(322, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(181, '/telemetry.current', [i for i in range(326, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(182, '/telemetry.current', [i for i in range(330, 1150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(183, '/telemetry.current', [i for i in range(332, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(184, '/telemetry.current', [i for i in range(334, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(185, '/telemetry.current', [i for i in range(338, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(186, '/telemetry.current', [i for i in range(340, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(187, '/telemetry.current', [i for i in range(342, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(189, '/telemetry.current', [i for i in range(346, 1150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(190, '/telemetry.current', [i for i in range(348, 1150, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
