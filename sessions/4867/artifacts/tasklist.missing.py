tasks = [
[tc.DownloadFile(30, '/telemetry.current', [24, 124, 130, 242, 248, 477, 484, 490, 496, 502, 508, 514, 520, 527]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [534, 540, 546, 552, 558, 564, 570, 577, 584, 590, 596, 602, 608, 614]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [620, 627, 634, 640, 646, 652, 658, 664, 670, 677, 684, 690, 696]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [1716, 2134, 2160, 2172]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/a_w_p480_11_32_0', [90, 108, 114, 140]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/a_w_p480_11_40_0', [55, 57, 81]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/a_w_p480_11_52_0', [29, 55, 57]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/a_w_p480_11_56_0', [67]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/a_w_p480_12_00_0', [19, 38]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/a_w_p480_12_04_0', [99, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/a_w_p480_12_04_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/a_w_p480_12_04_0', [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait]
]