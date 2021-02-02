tasks = [
    # Generated on 2021-02-02 22:26:33.121000, contains telemetry from sessions 5090 to 5091.
    # The session starts on 2021-02-02 23:45:18+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(47, '/telemetry.current', [618, 668, 718, 768, 818, 868, 918, 968, 643, 693, 743, 793, 843, 893, 943, 993, 631, 681, 731, 781]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [831, 881, 931, 981, 655, 705, 755, 805, 855, 905, 955, 625, 675, 725, 775, 825, 875, 925, 975, 637]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [687, 737, 787, 837, 887, 937, 987, 649, 699, 749, 799, 849, 899, 949, 661, 711, 761, 811, 861, 911]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [776, 826, 876, 926, 976, 801, 851, 901, 951, 789, 839, 889, 939, 989, 813, 863, 913, 963, 783, 833]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [883, 933, 983, 795, 845, 895, 945, 807, 857, 907, 957, 819, 869, 919, 969, 961]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(30, '/radfet_58', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(38, '/t02n_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t02n_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t02n_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
   # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(100, '/t01w_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, '/t01n_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(102, '/t02w_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, '/t02n_0'), Send, WaitMode.NoWait],
     
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]