import pytest
from Solutions.CLAUDE_COT.sub_list import sub_list

def test_sub_list_1():
    """Auto-generated test 1 for sub_list"""
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]

def test_sub_list_2():
    """Auto-generated test 2 for sub_list"""
    assert sub_list([1,2],[3,4])==[-2,-2]

def test_sub_list_3():
    """Auto-generated test 3 for sub_list"""
    assert sub_list([90,120],[50,70])==[40,50]

def test_sub_list_4():
    """Auto-generated test 4 for sub_list"""
    assert sub_list([2, 2, 6], [4, 1, 3]) == [-2, 1, 3]

def test_sub_list_5():
    """Auto-generated test 5 for sub_list"""
    assert sub_list([1, 5, 3], [5, 6, 7]) == [-4, -1, -4]

def test_sub_list_6():
    """Auto-generated test 6 for sub_list"""
    assert sub_list([3, 5, 4], [6, 3, 3]) == [-3, 2, 1]

def test_sub_list_7():
    """Auto-generated test 7 for sub_list"""
    assert sub_list([1, 2, 2], [7, 9, 6]) == [-6, -7, -4]

def test_sub_list_8():
    """Auto-generated test 8 for sub_list"""
    assert sub_list([5, 1, 3], [7, 1, 5]) == [-2, 0, -2]

def test_sub_list_9():
    """Auto-generated test 9 for sub_list"""
    assert sub_list([3, 2, 7], [6, 3, 4]) == [-3, -1, 3]

def test_sub_list_10():
    """Auto-generated test 10 for sub_list"""
    assert sub_list([5, 7, 1], [3, 3, 2]) == [2, 4, -1]

def test_sub_list_11():
    """Auto-generated test 11 for sub_list"""
    assert sub_list([4, 2, 8], [7, 1, 6]) == [-3, 1, 2]

def test_sub_list_12():
    """Auto-generated test 12 for sub_list"""
    assert sub_list([1, 7, 7], [1, 7, 3]) == [0, 0, 4]

def test_sub_list_13():
    """Auto-generated test 13 for sub_list"""
    assert sub_list([1, 2, 8], [4, 9, 3]) == [-3, -7, 5]

def test_sub_list_14():
    """Auto-generated test 14 for sub_list"""
    assert sub_list([3, 6, 1], [8, 3, 9]) == [-5, 3, -8]

def test_sub_list_15():
    """Auto-generated test 15 for sub_list"""
    assert sub_list([2, 1, 4], [6, 1, 9]) == [-4, 0, -5]

def test_sub_list_16():
    """Auto-generated test 16 for sub_list"""
    assert sub_list([3, 1, 3], [3, 9, 9]) == [0, -8, -6]

def test_sub_list_17():
    """Auto-generated test 17 for sub_list"""
    assert sub_list([2, 2, 3], [2, 7, 11]) == [0, -5, -8]

def test_sub_list_18():
    """Auto-generated test 18 for sub_list"""
    assert sub_list([5, 1, 1], [2, 10, 4]) == [3, -9, -3]

def test_sub_list_19():
    """Auto-generated test 19 for sub_list"""
    assert sub_list([6, 6, 2], [1, 8, 11]) == [5, -2, -9]

def test_sub_list_20():
    """Auto-generated test 20 for sub_list"""
    assert sub_list([1, 1, 3], [5, 1, 9]) == [-4, 0, -6]

def test_sub_list_21():
    """Auto-generated test 21 for sub_list"""
    assert sub_list([3, 3, 8], [1, 7, 8]) == [2, -4, 0]

def test_sub_list_22():
    """Auto-generated test 22 for sub_list"""
    assert sub_list([1, 6, 7], [4, 1, 9]) == [-3, 5, -2]

def test_sub_list_23():
    """Auto-generated test 23 for sub_list"""
    assert sub_list([1, 2, 2], [9, 8, 6]) == [-8, -6, -4]

def test_sub_list_24():
    """Auto-generated test 24 for sub_list"""
    assert sub_list([6, 7, 4], [1, 9, 6]) == [5, -2, -2]

def test_sub_list_25():
    """Auto-generated test 25 for sub_list"""
    assert sub_list([3, 3, 8], [9, 5, 8]) == [-6, -2, 0]

def test_sub_list_26():
    """Auto-generated test 26 for sub_list"""
    assert sub_list([5, 6, 7], [2, 2, 9]) == [3, 4, -2]

def test_sub_list_27():
    """Auto-generated test 27 for sub_list"""
    assert sub_list([5, 6, 7], [5, 5, 6]) == [0, 1, 1]

def test_sub_list_28():
    """Auto-generated test 28 for sub_list"""
    assert sub_list([1, 2, 2], [3, 1, 2]) == [-2, 1, 0]

def test_sub_list_29():
    """Auto-generated test 29 for sub_list"""
    assert sub_list([2, 7, 7], [2, 9, 2]) == [0, -2, 5]

def test_sub_list_30():
    """Auto-generated test 30 for sub_list"""
    assert sub_list([3, 7, 8], [5, 9, 11]) == [-2, -2, -3]

def test_sub_list_31():
    """Auto-generated test 31 for sub_list"""
    assert sub_list([2, 6, 4], [3, 1, 4]) == [-1, 5, 0]

def test_sub_list_32():
    """Auto-generated test 32 for sub_list"""
    assert sub_list([6, 2, 6], [4, 7, 7]) == [2, -5, -1]

def test_sub_list_33():
    """Auto-generated test 33 for sub_list"""
    assert sub_list([1, 6, 2], [9, 1, 6]) == [-8, 5, -4]

def test_sub_list_34():
    """Auto-generated test 34 for sub_list"""
    assert sub_list([1, 5, 7], [1, 5, 2]) == [0, 0, 5]

def test_sub_list_35():
    """Auto-generated test 35 for sub_list"""
    assert sub_list([1, 2, 7], [8, 5, 3]) == [-7, -3, 4]

def test_sub_list_36():
    """Auto-generated test 36 for sub_list"""
    assert sub_list([2, 7, 1], [5, 5, 8]) == [-3, 2, -7]

def test_sub_list_37():
    """Auto-generated test 37 for sub_list"""
    assert sub_list([5, 6], [4, 8]) == [1, -2]

def test_sub_list_38():
    """Auto-generated test 38 for sub_list"""
    assert sub_list([2, 6], [3, 9]) == [-1, -3]

def test_sub_list_39():
    """Auto-generated test 39 for sub_list"""
    assert sub_list([5, 3], [6, 2]) == [-1, 1]

def test_sub_list_40():
    """Auto-generated test 40 for sub_list"""
    assert sub_list([3, 5], [3, 5]) == [0, 0]

def test_sub_list_41():
    """Auto-generated test 41 for sub_list"""
    assert sub_list([4, 6], [3, 6]) == [1, 0]

def test_sub_list_42():
    """Auto-generated test 42 for sub_list"""
    assert sub_list([6, 3], [7, 6]) == [-1, -3]

def test_sub_list_43():
    """Auto-generated test 43 for sub_list"""
    assert sub_list([3, 2], [2, 6]) == [1, -4]

def test_sub_list_44():
    """Auto-generated test 44 for sub_list"""
    assert sub_list([4, 6], [1, 1]) == [3, 5]

def test_sub_list_45():
    """Auto-generated test 45 for sub_list"""
    assert sub_list([1, 2], [1, 1]) == [0, 1]

def test_sub_list_46():
    """Auto-generated test 46 for sub_list"""
    assert sub_list([1, 3], [6, 8]) == [-5, -5]

def test_sub_list_47():
    """Auto-generated test 47 for sub_list"""
    assert sub_list([2, 2], [7, 6]) == [-5, -4]

def test_sub_list_48():
    """Auto-generated test 48 for sub_list"""
    assert sub_list([1, 6], [3, 6]) == [-2, 0]

def test_sub_list_49():
    """Auto-generated test 49 for sub_list"""
    assert sub_list([3, 2], [3, 7]) == [0, -5]

def test_sub_list_50():
    """Auto-generated test 50 for sub_list"""
    assert sub_list([2, 2], [4, 1]) == [-2, 1]

def test_sub_list_51():
    """Auto-generated test 51 for sub_list"""
    assert sub_list([3, 2], [7, 7]) == [-4, -5]

def test_sub_list_52():
    """Auto-generated test 52 for sub_list"""
    assert sub_list([4, 7], [8, 8]) == [-4, -1]

def test_sub_list_53():
    """Auto-generated test 53 for sub_list"""
    assert sub_list([3, 6], [1, 6]) == [2, 0]

def test_sub_list_54():
    """Auto-generated test 54 for sub_list"""
    assert sub_list([1, 7], [1, 6]) == [0, 1]

def test_sub_list_55():
    """Auto-generated test 55 for sub_list"""
    assert sub_list([3, 3], [4, 7]) == [-1, -4]

def test_sub_list_56():
    """Auto-generated test 56 for sub_list"""
    assert sub_list([3, 2], [8, 6]) == [-5, -4]

def test_sub_list_57():
    """Auto-generated test 57 for sub_list"""
    assert sub_list([4, 1], [6, 2]) == [-2, -1]

def test_sub_list_58():
    """Auto-generated test 58 for sub_list"""
    assert sub_list([6, 2], [6, 9]) == [0, -7]

def test_sub_list_59():
    """Auto-generated test 59 for sub_list"""
    assert sub_list([2, 4], [2, 2]) == [0, 2]

def test_sub_list_60():
    """Auto-generated test 60 for sub_list"""
    assert sub_list([3, 4], [5, 4]) == [-2, 0]

def test_sub_list_61():
    """Auto-generated test 61 for sub_list"""
    assert sub_list([3, 7], [3, 8]) == [0, -1]

def test_sub_list_62():
    """Auto-generated test 62 for sub_list"""
    assert sub_list([2, 5], [1, 3]) == [1, 2]

def test_sub_list_63():
    """Auto-generated test 63 for sub_list"""
    assert sub_list([4, 6], [4, 2]) == [0, 4]

def test_sub_list_64():
    """Auto-generated test 64 for sub_list"""
    assert sub_list([5, 6], [3, 4]) == [2, 2]

def test_sub_list_65():
    """Auto-generated test 65 for sub_list"""
    assert sub_list([1, 6], [3, 9]) == [-2, -3]

def test_sub_list_66():
    """Auto-generated test 66 for sub_list"""
    assert sub_list([6, 3], [3, 2]) == [3, 1]

def test_sub_list_67():
    """Auto-generated test 67 for sub_list"""
    assert sub_list([2, 1], [5, 9]) == [-3, -8]

def test_sub_list_68():
    """Auto-generated test 68 for sub_list"""
    assert sub_list([5, 1], [5, 5]) == [0, -4]

def test_sub_list_69():
    """Auto-generated test 69 for sub_list"""
    assert sub_list([4, 6], [7, 7]) == [-3, -1]

def test_sub_list_70():
    """Auto-generated test 70 for sub_list"""
    assert sub_list([88, 120], [55, 65]) == [33, 55]

def test_sub_list_71():
    """Auto-generated test 71 for sub_list"""
    assert sub_list([85, 121], [45, 71]) == [40, 50]

def test_sub_list_72():
    """Auto-generated test 72 for sub_list"""
    assert sub_list([92, 125], [46, 74]) == [46, 51]

def test_sub_list_73():
    """Auto-generated test 73 for sub_list"""
    assert sub_list([93, 115], [50, 68]) == [43, 47]

def test_sub_list_74():
    """Auto-generated test 74 for sub_list"""
    assert sub_list([90, 116], [45, 72]) == [45, 44]

def test_sub_list_75():
    """Auto-generated test 75 for sub_list"""
    assert sub_list([88, 119], [51, 67]) == [37, 52]

def test_sub_list_76():
    """Auto-generated test 76 for sub_list"""
    assert sub_list([91, 121], [47, 74]) == [44, 47]

def test_sub_list_77():
    """Auto-generated test 77 for sub_list"""
    assert sub_list([94, 118], [53, 71]) == [41, 47]

def test_sub_list_78():
    """Auto-generated test 78 for sub_list"""
    assert sub_list([89, 119], [51, 65]) == [38, 54]

def test_sub_list_79():
    """Auto-generated test 79 for sub_list"""
    assert sub_list([85, 124], [48, 72]) == [37, 52]

def test_sub_list_80():
    """Auto-generated test 80 for sub_list"""
    assert sub_list([89, 124], [53, 67]) == [36, 57]

def test_sub_list_81():
    """Auto-generated test 81 for sub_list"""
    assert sub_list([90, 118], [50, 67]) == [40, 51]

def test_sub_list_82():
    """Auto-generated test 82 for sub_list"""
    assert sub_list([85, 123], [54, 70]) == [31, 53]

def test_sub_list_83():
    """Auto-generated test 83 for sub_list"""
    assert sub_list([85, 118], [48, 75]) == [37, 43]

def test_sub_list_84():
    """Auto-generated test 84 for sub_list"""
    assert sub_list([91, 122], [45, 73]) == [46, 49]

def test_sub_list_85():
    """Auto-generated test 85 for sub_list"""
    assert sub_list([90, 115], [47, 71]) == [43, 44]

def test_sub_list_86():
    """Auto-generated test 86 for sub_list"""
    assert sub_list([89, 125], [55, 70]) == [34, 55]

def test_sub_list_87():
    """Auto-generated test 87 for sub_list"""
    assert sub_list([89, 115], [50, 71]) == [39, 44]

def test_sub_list_88():
    """Auto-generated test 88 for sub_list"""
    assert sub_list([94, 119], [45, 75]) == [49, 44]

def test_sub_list_89():
    """Auto-generated test 89 for sub_list"""
    assert sub_list([89, 117], [46, 68]) == [43, 49]

def test_sub_list_90():
    """Auto-generated test 90 for sub_list"""
    assert sub_list([90, 118], [54, 67]) == [36, 51]

def test_sub_list_91():
    """Auto-generated test 91 for sub_list"""
    assert sub_list([90, 118], [53, 70]) == [37, 48]

def test_sub_list_92():
    """Auto-generated test 92 for sub_list"""
    assert sub_list([88, 125], [54, 69]) == [34, 56]

def test_sub_list_93():
    """Auto-generated test 93 for sub_list"""
    assert sub_list([92, 115], [49, 71]) == [43, 44]

def test_sub_list_94():
    """Auto-generated test 94 for sub_list"""
    assert sub_list([86, 119], [50, 71]) == [36, 48]

def test_sub_list_95():
    """Auto-generated test 95 for sub_list"""
    assert sub_list([85, 119], [48, 67]) == [37, 52]

def test_sub_list_96():
    """Auto-generated test 96 for sub_list"""
    assert sub_list([93, 122], [54, 69]) == [39, 53]

def test_sub_list_97():
    """Auto-generated test 97 for sub_list"""
    assert sub_list([93, 119], [49, 74]) == [44, 45]

def test_sub_list_98():
    """Auto-generated test 98 for sub_list"""
    assert sub_list([88, 123], [46, 67]) == [42, 56]

def test_sub_list_99():
    """Auto-generated test 99 for sub_list"""
    assert sub_list([90, 116], [50, 73]) == [40, 43]

def test_sub_list_100():
    """Auto-generated test 100 for sub_list"""
    assert sub_list([93, 120], [46, 68]) == [47, 52]

def test_sub_list_101():
    """Auto-generated test 101 for sub_list"""
    assert sub_list([85, 116], [53, 69]) == [32, 47]

def test_sub_list_102():
    """Auto-generated test 102 for sub_list"""
    assert sub_list([86, 123], [46, 75]) == [40, 48]

