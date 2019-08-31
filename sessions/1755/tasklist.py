tasks = [
    # Generated on 2019-08-31 12:37:20.817000, contains telemetry from sessions 1754 to 1755.
    # The session starts on 2019-08-31 13:21:52+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(33, '/telemetry.current', [174, 224, 274, 324, 374, 199, 249, 299, 349, 187, 237, 287, 337, 387, 211, 261, 311, 361, 181, 231]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [281, 331, 381, 193, 243, 293, 343, 393, 205, 255, 305, 355, 217, 267, 317, 367]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # suns experiment
    [tc.PerformSunSExperiment(3, 0, 20, 100, datetime.timedelta(seconds=3), 50, datetime.timedelta(seconds=10), 'suns_ps_14'), Send, WaitMode.Wait],


    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_12', [101, 104, 144, 151, 152, 156, 158, 171, 183, 184, 190, 192, 193, 197, 240]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_12_sec', [98, 105, 111, 113, 114, 129, 171, 172, 173, 174, 176, 178]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_12_sec', [179, 180, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(35, '/suns_ps_13', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_13', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_13', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/suns_ps_13', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_13', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/suns_ps_13', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_13', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_ps_13', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_13', [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_13', [180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_13', [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/suns_ps_13', [220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_13', [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_13', [260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_13', [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_13', [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_13', [320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_13', [340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_13', [360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_13', [379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_13', [398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/suns_ps_13_sec', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/suns_ps_13_sec', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/suns_ps_13_sec', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/suns_ps_13_sec', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/suns_ps_13_sec', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/suns_ps_13_sec', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/suns_ps_13_sec', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/suns_ps_13_sec', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/suns_ps_13_sec', [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/suns_ps_13_sec', [171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/suns_ps_13_sec', [190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]