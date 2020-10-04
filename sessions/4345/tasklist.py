tasks = [
    # Generated on 2020-09-19 22:04:39.476000, contains telemetry from sessions 4246 to 4247.
    # The session starts on 2020-09-19 23:17:51+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [14, 64, 114, 164, 214, 39, 89, 139, 189, 27, 77, 127, 177, 227, 51, 101, 151, 201, 21, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [121, 171, 221, 33, 83, 133, 183, 45, 95, 145, 195, 57, 107, 157, 207]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(132, '/radfet_48', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(41, '/t_w_22_40_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t_w_22_41_0', range(0, 20)), Send, WaitMode.Wait],    
    [tc.DownloadFile(43, '/t_w_22_42_0', range(0, 20)), Send, WaitMode.Wait],   

    [tc.DownloadFile(44, '/t_w_22_40_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t_w_22_41_0', range(20, 40)), Send, WaitMode.Wait],    
    [tc.DownloadFile(46, '/t_w_22_42_0', range(20, 40)), Send, WaitMode.Wait],   

    [tc.DownloadFile(47, '/t_w_22_40_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t_w_22_41_0', range(40, 60)), Send, WaitMode.Wait],    
    [tc.DownloadFile(49, '/t_w_22_42_0', range(40, 60)), Send, WaitMode.Wait],  

    [tc.DownloadFile(51, '/t_w_22_40_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t_w_22_41_0', range(60, 80)), Send, WaitMode.Wait],    
    [tc.DownloadFile(53, '/t_w_22_42_0', range(60, 80)), Send, WaitMode.Wait],   

    [tc.DownloadFile(54, '/t_w_22_40_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t_w_22_41_0', range(80, 100)), Send, WaitMode.Wait],    
    [tc.DownloadFile(56, '/t_w_22_42_0', range(80, 100)), Send, WaitMode.Wait],   

    [tc.DownloadFile(57, '/t_w_22_40_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t_w_22_41_0', range(100, 120)), Send, WaitMode.Wait],    
    [tc.DownloadFile(59, '/t_w_22_42_0', range(100, 120)), Send, WaitMode.Wait], 

    [tc.DownloadFile(61, '/t_w_22_40_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t_w_22_41_0', range(120, 140)), Send, WaitMode.Wait],    
    [tc.DownloadFile(63, '/t_w_22_42_0', range(120, 140)), Send, WaitMode.Wait],   

    [tc.DownloadFile(64, '/t_w_22_40_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t_w_22_41_0', range(140, 160)), Send, WaitMode.Wait],    
    [tc.DownloadFile(66, '/t_w_22_42_0', range(140, 160)), Send, WaitMode.Wait],   

    [tc.DownloadFile(67, '/t_w_22_40_0', range(160, 180)), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t_w_22_41_0', range(160, 180)), Send, WaitMode.Wait],    
    [tc.DownloadFile(69, '/t_w_22_42_0', range(160, 180)), Send, WaitMode.Wait], 

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]