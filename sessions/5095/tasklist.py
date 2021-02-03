tasks = [
    # Generated on 2021-02-03 14:29:41.940000, contains telemetry from sessions 5093 to 5095.
    # The session starts on 2021-02-03 21:27:23+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # foteczki (21:45), zakladamy wyslanie o 21:29
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=16), 'wro_w_p480_21_45'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'wro_n_p480_21_45'), Send, WaitMode.Wait],

    # 22:24
    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=39), 'wro_w_p480_22_24'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'wro_n_p480_22_24'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [62, 112, 162, 212, 262, 312, 362, 412, 462, 512, 562, 612, 662, 712, 762, 812, 862, 912, 962, 1012]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1062, 87, 137, 187, 237, 287, 337, 387, 437, 487, 537, 587, 637, 687, 737, 787, 837, 887, 937, 987]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1037, 1087, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [975, 1025, 1075, 99, 149, 199, 249, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849, 899]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [949, 999, 1049, 69, 119, 169, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [919, 969, 1019, 1069, 81, 131, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [881, 931, 981, 1031, 1081, 93, 143, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743, 793]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [843, 893, 943, 993, 1043, 1093, 105, 155, 205, 255, 305, 355, 405, 455, 505, 555, 605, 655, 705, 755]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [805, 855, 905, 955, 1005, 1055]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]