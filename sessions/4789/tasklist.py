tasks = [
    # Generated on 2020-12-14 17:27:51.801000, contains telemetry from sessions 4787 to 4789.
    # The session starts on 2020-12-14 20:12:07+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 25, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 13, 63, 113, 163]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [213, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 37, 87, 137, 187, 237, 287]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [337, 387, 437, 487, 537, 587, 637, 687, 737, 787, 837, 7, 57, 107, 157, 207, 257, 307, 357, 407]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [457, 507, 557, 607, 657, 707, 757, 807, 857, 19, 69, 119, 169, 219, 269, 319, 369, 419, 469, 519]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [569, 619, 669, 719, 769, 819, 869, 31, 81, 131, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [681, 731, 781, 831, 43, 93, 143, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743, 793]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [843]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]