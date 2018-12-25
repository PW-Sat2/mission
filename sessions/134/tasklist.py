tasks = [
    # ============================================================================
    # SESSION 134
    # ============================================================================

    ["SESSION 134", Print, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["List files - 11 items expected", Print, WaitMode.NoWait],
    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 133 and 134
    ["Telemetry current between sessions  133 and 134", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],

    # More telemetry between session 133 and 134
    ["More telemetry current between sessions 133 and 134", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(1580, 1772, 10)]), Send, WaitMode.Wait],

    # Remove files
    ["Remove files - step #22", Print, WaitMode.Wait],

    [tc.RemoveFile(20, '/p6_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(21, '/p5_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(22, '/p8_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(23, '/suns_7_sec'), Send, WaitMode.NoWait],
    [tc.RemoveFile(24, '/suns_8_sec'), Send, WaitMode.Wait], # Probably already removed

    [tc.ListFiles(25, '/'), Send, WaitMode.Wait],

    # RadFET exp data download
    ["RadFET experiment data download - step #29", Print, WaitMode.Wait],
    [tc.DownloadFile(30, '/radfet_7', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # Previous, missing telemetry.previous
    ["Previous, missing telemetry.previous", Print, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.previous', [1429, 1438, 1479, 1488, 1529, 1538, 1579, 1588, 1629, 1638, 1679, 1688, 1729, 1738, 1752, 1779, 1788, 1829, 1838, 1879]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1888, 1929, 1938, 1954, 1979, 1988, 1997, 2029, 2038, 2079, 2088, 2102, 2129, 2138, 2179, 2188, 2190, 2229, 2238, 2279]), Send, WaitMode.Wait],

    # Telemetry between session 130 and 132
    ["Telemetry current between sessions  130 and 132", Print, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(301, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(302, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(131, 300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(132, 300, 12)]), Send, WaitMode.Wait],    
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(303, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(304, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(305, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(307, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(134, 300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [i for i in range(135, 300, 12)]), Send, WaitMode.Wait],    
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(308, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(309, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(310, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(311, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [i for i in range(313, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [i for i in range(314, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [i for i in range(315, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [i for i in range(137, 300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [i for i in range(138, 300, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],        
    [tc.DownloadFile(69, '/telemetry.current', [i for i in range(316, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(317, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(319, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(320, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(321, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(322, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(140, 300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(141, 300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(323, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/telemetry.current', [i for i in range(324, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [i for i in range(326, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(327, 1600, 60)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(81, '/telemetry.current', [i for i in range(328, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.current', [i for i in range(329, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.current', [i for i in range(330, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [i for i in range(332, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [i for i in range(333, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.current', [i for i in range(334, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.current', [i for i in range(335, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/telemetry.current', [i for i in range(336, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.current', [i for i in range(338, 1600, 60)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(90, '/telemetry.current', [i for i in range(339, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(340, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [i for i in range(341, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/telemetry.current', [i for i in range(342, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/telemetry.current', [i for i in range(344, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/telemetry.current', [i for i in range(345, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/telemetry.current', [i for i in range(346, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/telemetry.current', [i for i in range(347, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/telemetry.current', [i for i in range(348, 1600, 60)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(99, '/telemetry.current', [i for i in range(349, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(350, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(351, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(352, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(353, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(354, 1600, 60)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(355, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [i for i in range(356, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.current', [i for i in range(357, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.current', [i for i in range(358, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.current', [i for i in range(359, 1600, 60)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # Missing telemetry.current
    ["Missing telemetry.current", Print, WaitMode.NoWait],
    [tc.DownloadFile(200, '/telemetry.current', [385, 643, 720, 960, 1032, 1092, 1140, 1152, 1212, 1225, 1272, 1440]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],


    [tc.SendBeacon(), Send, WaitMode.Wait],
]