tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Telemetry between session 117 and 118
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1540, 1740, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1546, 1740, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1543, 1740, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1549, 1740, 12)]), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1541, 1740, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(1542, 1740, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(1544, 1740, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(1545, 1740, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(1547, 1740, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(1548, 1740, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(1550, 1740, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(1551, 1740, 12)]), Send, WaitMode.Wait],

    # Download low res photos
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/p1_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p2_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p3_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p4_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p5_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(35, '/p6_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p7_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p8_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p9_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p10_128', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # suns_7_sec missings download
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/suns_7_sec', [73, 104, 108, 109, 110, 121, 131, 133, 138, 139, 165, 185, 194, 204, 210, 215, 218, 219]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_7_sec', [221, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 237, 238, 239, 240, 241, 242]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_7_sec', [243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_7_sec', [261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_7_sec', [279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296]), Send, WaitMode.Wait],

    # Much more telemetry between session 116 and 117
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(651, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(652, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(654, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(655, 1540, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(657, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(658, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(660, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(661, 1540, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(78, '/telemetry.current', [i for i in range(663, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [i for i in range(664, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(666, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [i for i in range(667, 1540, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(82, '/telemetry.current', [i for i in range(669, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.current', [i for i in range(670, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [i for i in range(672, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [i for i in range(673, 1540, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(86, '/telemetry.current', [i for i in range(674, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.current', [i for i in range(676, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/telemetry.current', [i for i in range(677, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.current', [i for i in range(679, 1540, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(90, '/telemetry.current', [i for i in range(680, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(682, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [i for i in range(683, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/telemetry.current', [i for i in range(685, 1540, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(94, '/telemetry.current', [i for i in range(686, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/telemetry.current', [i for i in range(688, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/telemetry.current', [i for i in range(689, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/telemetry.current', [i for i in range(691, 1540, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(99, '/telemetry.current', [i for i in range(692, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(694, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(695, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(697, 1540, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(698, 1540, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(699, 1540, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]