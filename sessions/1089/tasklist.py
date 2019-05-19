tasks = [
    # Generated on 2019-05-19 12:22:59.638000, contains telemetry from sessions 1088 to 1089.
    # The session starts on 2019-05-19 13:25:27+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # SunS experiment data download
    [tc.DownloadFile(46, '/suns_ps_4', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_4', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_4', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_4', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_4', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_4', [i for i in range(125, 150, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_4', [i for i in range(150, 175, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_4', [i for i in range(175, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_4', [i for i in range(200, 225, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_4', [i for i in range(225, 250, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [552, 602, 652, 702, 752, 577, 627, 677, 727, 565, 615, 665, 715, 765, 589, 639, 689, 739, 559, 609]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [659, 709, 759, 571, 621, 671, 721, 771, 583, 633, 683, 733, 595, 645, 695, 745]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]