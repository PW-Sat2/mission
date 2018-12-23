tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # ReadMemory, weird telecommand
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    [tc.SendBeacon(), Send, WaitMode.Wait], # Wait until good communication
    [tc.RawI2C(4, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(7, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(8, '/'), Send, WaitMode.Wait],

    # Telemetry between session 121 and 123
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(850, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(875, 1950, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(862, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(887, 1950, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(856, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(868, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(881, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(893, 1950, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(853, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(859, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(865, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(871, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(878, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [i for i in range(884, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.current', [i for i in range(890, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [i for i in range(896, 1950, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(26, '/telemetry.current', [i for i in range(851, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.current', [i for i in range(852, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.current', [i for i in range(854, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/telemetry.current', [i for i in range(855, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(857, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(858, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(860, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(861, 1950, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(863, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(864, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(866, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(867, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(869, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(870, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(872, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(873, 1950, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(874, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(876, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(877, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(879, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(880, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(882, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(883, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(885, 1950, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(886, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(888, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(889, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(891, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(892, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(894, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(895, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(897, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(898, 1950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [i for i in range(899, 1950, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]