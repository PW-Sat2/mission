tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1, 51, 101, 151, 201, 26, 76, 126, 176, 14, 64, 114, 164, 214, 38, 88, 138, 188, 8, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [108, 158, 208, 20, 70, 120, 170, 32, 82, 132, 182, 44, 94, 144, 194]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(32, '/radfet_52', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/w_p480_0_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/n_p480_0_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/w_p480_1_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/n_p480_1_0', range(0, 20)), Send, WaitMode.Wait],

    [tc.DownloadFile(45, '/w_p480_0_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/n_p480_0_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/w_p480_1_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/n_p480_1_0', range(20, 40)), Send, WaitMode.Wait],


    [tc.DownloadFile(50, '/w_p480_0_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/n_p480_0_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/w_p480_1_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/n_p480_1_0', range(40, 60)), Send, WaitMode.Wait],

    [tc.DownloadFile(55, '/w_p480_0_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/n_p480_0_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/w_p480_1_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/n_p480_1_0', range(60, 80)), Send, WaitMode.Wait],


    [tc.DownloadFile(60, '/w_p480_0_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/n_p480_0_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/w_p480_1_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/n_p480_1_0', range(80, 100)), Send, WaitMode.Wait],

    [tc.DownloadFile(65, '/w_p480_0_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/n_p480_0_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/w_p480_1_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/n_p480_1_0', range(100, 120)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/w_p480_0_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/n_p480_0_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/w_p480_1_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/n_p480_1_0', range(120, 140)), Send, WaitMode.Wait],

    [tc.DownloadFile(75, '/w_p480_0_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/n_p480_0_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/w_p480_1_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/n_p480_1_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(80, '/w_p480_0_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/n_p480_0_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/w_p480_1_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/n_p480_1_0', range(160, 180)), Send, WaitMode.Wait],

    [tc.DownloadFile(85, '/w_p480_0_0', range(180, 200)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/n_p480_0_0', range(180, 200)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/w_p480_1_0', range(180, 200)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/n_p480_1_0', range(180, 200)), Send, WaitMode.Wait],

    [tc.DownloadFile(90, '/w_p480_0_0', range(200, 220)), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/n_p480_0_0', range(200, 220)), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/w_p480_1_0', range(200, 220)), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/n_p480_1_0', range(200, 220)), Send, WaitMode.Wait],

    [tc.DownloadFile(95, '/w_p480_0_0', range(220, 240)), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/n_p480_0_0', range(220, 240)), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/w_p480_1_0', range(220, 240)), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/n_p480_1_0', range(220, 240)), Send, WaitMode.Wait],

    [tc.DownloadFile(100, '/w_p480_0_0', range(240, 260)), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/n_p480_0_0', range(240, 260)), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/w_p480_1_0', range(240, 260)), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/n_p480_1_0', range(240, 260)), Send, WaitMode.Wait],

    [tc.DownloadFile(105, '/w_p480_0_0', range(260, 280)), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/n_p480_0_0', range(260, 280)), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/w_p480_1_0', range(260, 280)), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/n_p480_1_0', range(260, 280)), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.Wait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.little_oryx.Echo('PW-SAT2 has new software. More info: https://www.kplabs.pl/en/blog-en/case-study-little-oryx-2/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]