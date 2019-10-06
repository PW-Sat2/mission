tasks = [
    # Generated on 2019-10-06 11:58:45.814000, contains telemetry from sessions 1972 to 1973.
    # The session starts on 2019-10-06 12:58:47+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(35, '/telemetry.current', [363, 413, 463, 513, 563, 388, 438, 488, 538, 376, 426, 476, 526, 576, 400, 450, 500, 550, 370, 420]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [470, 520, 570, 382, 432, 482, 532, 582, 394, 444, 494, 544, 406, 456, 506, 556]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_15', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_15', [340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_15', [360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_15', [379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_15', [398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416]), Send, WaitMode.Wait],
    # missing from previous session end

    
    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]