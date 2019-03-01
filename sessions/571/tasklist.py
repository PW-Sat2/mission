tasks = [
    # Generated on 2019-03-01 21:15:16.286000, contains telemetry from sessions 570 to 571.
    # The session starts on 2019-03-01 22:10:07+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(100, '/telemetry.current', [320, 324, 328, 332, 336, 340, 344, 348,
                                                 352, 356, 360, 364, 368, 372, 376, 380, 384, 388, 392, 396]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [321, 325, 329, 333, 337, 341, 345, 349,
                                                 353, 357, 361, 365, 369, 373, 377, 381, 385, 389, 393, 397]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [322, 326, 330, 334, 338, 342, 346, 350,
                                                 354, 358, 362, 366, 370, 374, 378, 382, 386, 390, 394, 398]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [323, 327, 331, 335, 339, 343, 347, 351,
                                                 355, 359, 363, 367, 371, 375, 379, 383, 387, 391, 395, 399]), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [680, 730, 780, 830, 880, 705, 755, 805,
                                                855, 693, 743, 793, 843, 893, 717, 767, 817, 867, 687, 737]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [787, 837, 887, 699, 749, 799,
                                                849, 899, 711, 761, 811, 861, 723, 773, 823, 873]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
