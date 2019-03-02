tasks = [
    # Generated on 2019-03-02 17:17:48.659487, contains telemetry from sessions 573 to 576.
    # The session starts on 2019-03-02 20:39:06+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

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

    [tc.RemoveFile(20, '/radfet_9'), Send, WaitMode.Wait],
    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1016, 1066, 41, 91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [941, 991, 1041, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [879, 929, 979, 1029, 1079, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [803, 853, 903, 953, 1003, 1053, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [723, 773, 823, 873, 923, 973, 1023, 1073, 35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [635, 685, 735, 785, 835, 885, 935, 985, 1035, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 59, 109, 159, 209, 259, 309, 359, 409, 459, 509]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]