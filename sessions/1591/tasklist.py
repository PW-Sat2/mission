tasks = [
    # Generated on 2019-08-04 01:55:48.693000, contains telemetry from sessions 1590 to 1591.
    # The session starts on 2019-08-04 10:09:56+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(72, '/telemetry.previous', [1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1575, 1625, 1675, 1725, 1775]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [20, 70, 120, 170, 220, 270, 320, 370, 45, 95, 145, 195, 245, 295, 345, 395, 33, 83, 133, 183]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.previous', [1825, 1875, 1925, 1975, 2025, 2075, 2125, 2175, 2225, 2275, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.previous', [2063, 2113, 2163, 2213, 2263, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 1557]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [233, 283, 333, 383, 7, 57, 107, 157, 207, 257, 307, 357, 27, 77, 127, 177, 227, 277, 327, 377]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.previous', [1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1569, 1619, 1669, 1719, 1769, 1819]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/telemetry.previous', [1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [39, 89, 139, 189, 239, 289, 339, 389, 1, 51, 101, 151, 201, 251, 301, 351, 401, 13, 63, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.previous', [2131, 2181, 2231, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [163, 213, 263, 313, 363]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [1417]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_10_sec', [1, 13, 31, 32, 33, 35, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_10_sec', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_10_sec', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_10_sec', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_10_sec', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_10_sec', [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_10_sec', [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/suns_ps_10_sec', [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_10_sec', [194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/suns_ps_10_sec', [214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_10_sec', [234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_ps_10_sec', [254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_10_sec', [274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_10_sec', [294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_10_sec', [314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/suns_ps_10_sec', [334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_10_sec', [354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_10_sec', [374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_10_sec', [394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_10_sec', [414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_10_sec', [434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_10_sec', [454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_10_sec', [473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_10_sec', [492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_10_sec', [511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/suns_ps_10_sec', [530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/suns_ps_10_sec', [549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/suns_ps_10_sec', [568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/suns_ps_10_sec', [587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/suns_ps_10_sec', [606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/suns_ps_10_sec', [625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/suns_ps_10_sec', [644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/suns_ps_10_sec', [663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/suns_ps_10_sec', [682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/suns_ps_10_sec', [701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/suns_ps_10_sec', [720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/suns_ps_10_sec', [739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/suns_ps_10_sec', [758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/suns_ps_10_sec', [777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/suns_ps_10_sec', [796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/suns_ps_10_sec', [815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]