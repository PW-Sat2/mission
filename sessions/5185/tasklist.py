tasks = [
    # Generated on 2021-02-19 13:24:28.272000, contains telemetry from sessions 5184 to 5185.
    # The session starts on 2021-02-19 22:01:31+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(4, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [2198, 2248, 2223, 2273, 2211, 2261, 2235, 2205, 2255, 2217, 2267, 2229, 2279, 2241]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [18, 68, 118, 168, 218, 268, 318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 43]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [93, 143, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743, 793, 843, 893, 31, 81, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 5, 55, 105, 155]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [205, 255, 305, 355, 405, 455, 505, 555, 605, 655, 705, 755, 805, 855, 905, 25, 75, 125, 175, 225]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 37, 87, 137, 187, 237, 287]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [337, 387, 437, 487, 537, 587, 637, 687, 737, 787, 837, 887, 49, 99, 149, 199, 249, 299, 349, 399]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [449, 499, 549, 599, 649, 699, 749, 799, 849, 899, 11, 61, 111, 161, 211, 261, 311, 361, 411, 461]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [511, 561, 611, 661, 711, 761, 811, 861, 911]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]