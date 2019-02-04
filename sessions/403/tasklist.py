tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

     # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start - from 400 to 403
    [tc.DownloadFile(30, '/telemetry.current', [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1003, 1053, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [928, 978, 1028, 16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [866, 916, 966, 1016, 1066, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [790, 840, 890, 940, 990, 1040, 10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [710, 760, 810, 860, 910, 960, 1010, 1060, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [622, 672, 722, 772, 822, 872, 922, 972, 1022, 34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [546, 596, 646, 696, 746, 796, 846, 896, 946, 996, 1046]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]