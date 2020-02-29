tasks = [
    # Generated on 2020-02-29 21:55:58.476000, contains telemetry from sessions 2938 to 2939.
    # The session starts on 2020-02-29 23:15:05+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(50, '/telemetry.current', [168, 218, 268, 318, 368, 193, 243, 293, 343, 181, 231, 281, 331, 381, 205, 255, 305, 355, 175, 225]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [275, 325, 375, 187, 237, 287, 337, 387, 199, 249, 299, 349, 211, 261, 311, 361]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # auto-generated file download start
    [tc.DownloadFile(52, '/t0n_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t0n_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(74, '/t1w_480_0', [80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t1w_480_0', [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(80, '/t2n_480_0', [80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(98, '/t3n_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(99, '/t3w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(58, '/t0w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t0w_480_0', [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t0w_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t0w_480_0', [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(66, '/t1n_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t1n_480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t1n_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t1n_480_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]), Send, WaitMode.Wait],
  
    [tc.DownloadFile(85, '/t2w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/t2w_480_0', [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/t2w_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/t2w_480_0', [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/t2w_480_0', [147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164]), Send, WaitMode.Wait],

    [tc.DownloadFile(107, '/t4n_480_0', [60, 61, 68, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/t4n_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/t4n_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/t4n_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/t4n_480_0', [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(116, '/t4w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/t4w_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/t4w_480_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]