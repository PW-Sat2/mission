tasks = [
    # Generated on 2019-08-04 11:10:21.721000, contains telemetry from sessions 1591 to 1592.
    # The session starts on 2019-08-04 11:44:29+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(53, '/telemetry.current', [363, 413, 463, 513, 563, 388, 438, 488, 538, 376, 426, 476, 526, 576, 400, 450, 500, 550, 370, 420]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [470, 520, 570, 382, 432, 482, 532, 582, 394, 444, 494, 544, 406, 456, 506, 556]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_10_sec', [394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_10_sec', [414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_10_sec', [434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_10_sec', [454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_10_sec', [473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_10_sec', [492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_10_sec', [511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_10_sec', [530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/suns_ps_10_sec', [549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_10_sec', [568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/suns_ps_10_sec', [587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_10_sec', [606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_ps_10_sec', [625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_10_sec', [644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_10_sec', [663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_10_sec', [682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/suns_ps_10_sec', [701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_10_sec', [720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_10_sec', [739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_10_sec', [758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_10_sec', [777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_10_sec', [796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_10_sec', [815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]