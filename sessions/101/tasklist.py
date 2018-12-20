tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 100 and 101
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(800, 2150, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(850, 2150, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(825, 2150, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(875, 2150, 100)]), Send, WaitMode.Wait],

    # ReadMemory, weird tele
    [tc.ReadMemory(14, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Download missing chunks of suns exp 6 primary file
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/suns_6', [i for i in range(575, 593, 1)]), Send, WaitMode.Wait],

    # Download missing chunks of suns exp 6 secondary file
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/suns_6_sec', [150, 151, 152, 226, 246, 278, 279]), Send, WaitMode.Wait],

    # More telemetry between session 100 and 101
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(812, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(837, 2150, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(806, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(818, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(831, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(843, 2150, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(803, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(809, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(815, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(821, 2150, 50)]), Send, WaitMode.Wait],

    # Much more telemetry between session 100 and 101
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(827, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(835, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(838, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(841, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(846, 2150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(801, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(802, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(804, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(805, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [i for i in range(807, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [i for i in range(808, 2150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(66, '/telemetry.current', [i for i in range(800, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [i for i in range(810, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [i for i in range(811, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [i for i in range(813, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(814, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(816, 2150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(817, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(819, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(820, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(822, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(823, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(825, 2150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(78, '/telemetry.current', [i for i in range(826, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [i for i in range(828, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(829, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [i for i in range(832, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.current', [i for i in range(834, 2150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(83, '/telemetry.current', [i for i in range(836, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [i for i in range(837, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [i for i in range(839, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.current', [i for i in range(840, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.current', [i for i in range(842, 2150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(88, '/telemetry.current', [i for i in range(844, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.current', [i for i in range(845, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/telemetry.current', [i for i in range(847, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(848, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [i for i in range(849, 2150, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
