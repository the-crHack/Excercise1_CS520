import pytest
from Solutions.QWEN_SCOT.filter_oddnumbers import filter_oddnumbers

def test_filter_oddnumbers_1():
    """Auto-generated test 1 for filter_oddnumbers"""
    assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]

def test_filter_oddnumbers_2():
    """Auto-generated test 2 for filter_oddnumbers"""
    assert filter_oddnumbers([10,20,45,67,84,93])==[45,67,93]

def test_filter_oddnumbers_3():
    """Auto-generated test 3 for filter_oddnumbers"""
    assert filter_oddnumbers([5,7,9,8,6,4,3])==[5,7,9,3]

def test_filter_oddnumbers_4():
    """Auto-generated test 4 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 2, 7, 8, 3, 2, 9, 9, 13, 11]) == [7, 3, 9, 9, 13, 11]

def test_filter_oddnumbers_5():
    """Auto-generated test 5 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 5, 7, 6, 9, 5, 11, 4, 11, 9]) == [5, 7, 9, 5, 11, 11, 9]

def test_filter_oddnumbers_6():
    """Auto-generated test 6 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 7, 5, 3, 8, 11, 12, 11, 7, 10]) == [5, 7, 5, 3, 11, 11, 7]

def test_filter_oddnumbers_7():
    """Auto-generated test 7 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 2, 4, 4, 5, 7, 2, 3, 14, 11]) == [5, 7, 3, 11]

def test_filter_oddnumbers_8():
    """Auto-generated test 8 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 1, 6, 8, 1, 5, 4, 10, 8, 11]) == [3, 1, 1, 5, 11]

def test_filter_oddnumbers_9():
    """Auto-generated test 9 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 4, 4, 9, 10, 10, 5, 7, 9, 11]) == [9, 5, 7, 9, 11]

def test_filter_oddnumbers_10():
    """Auto-generated test 10 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 7, 7, 7, 5, 1, 3, 6, 9, 12]) == [3, 7, 7, 7, 5, 1, 3, 9]

def test_filter_oddnumbers_11():
    """Auto-generated test 11 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 1, 6, 8, 8, 1, 3, 5, 12, 7]) == [1, 1, 3, 5, 7]

def test_filter_oddnumbers_12():
    """Auto-generated test 12 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 1, 1, 4, 1, 7, 3, 12, 14, 14]) == [1, 1, 1, 7, 3]

def test_filter_oddnumbers_13():
    """Auto-generated test 13 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 7, 8, 2, 4, 11, 12, 4, 14, 9]) == [3, 7, 11, 9]

def test_filter_oddnumbers_14():
    """Auto-generated test 14 for filter_oddnumbers"""
    assert filter_oddnumbers([6, 6, 8, 7, 7, 1, 10, 7, 5, 11]) == [7, 7, 1, 7, 5, 11]

def test_filter_oddnumbers_15():
    """Auto-generated test 15 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 2, 5, 1, 9, 1, 7, 12, 6, 6]) == [5, 5, 1, 9, 1, 7]

def test_filter_oddnumbers_16():
    """Auto-generated test 16 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 5, 8, 4, 9, 3, 4, 10, 6, 10]) == [5, 9, 3]

def test_filter_oddnumbers_17():
    """Auto-generated test 17 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 6, 1, 3, 6, 6, 10, 11, 9, 9]) == [1, 3, 11, 9, 9]

def test_filter_oddnumbers_18():
    """Auto-generated test 18 for filter_oddnumbers"""
    assert filter_oddnumbers([1, 1, 2, 3, 1, 4, 10, 3, 14, 14]) == [1, 1, 3, 1, 3]

def test_filter_oddnumbers_19():
    """Auto-generated test 19 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 5, 4, 9, 7, 7, 11, 5, 11, 5]) == [5, 5, 9, 7, 7, 11, 5, 11, 5]

def test_filter_oddnumbers_20():
    """Auto-generated test 20 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 3, 1, 9, 2, 10, 12, 10, 4, 5]) == [5, 3, 1, 9, 5]

def test_filter_oddnumbers_21():
    """Auto-generated test 21 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 7, 3, 3, 1, 1, 4, 4, 10, 14]) == [7, 3, 3, 1, 1]

def test_filter_oddnumbers_22():
    """Auto-generated test 22 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 5, 8, 7, 6, 7, 7, 9, 14, 5]) == [5, 7, 7, 7, 9, 5]

def test_filter_oddnumbers_23():
    """Auto-generated test 23 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 6, 1, 2, 6, 1, 2, 3, 8, 15]) == [1, 1, 3, 15]

def test_filter_oddnumbers_24():
    """Auto-generated test 24 for filter_oddnumbers"""
    assert filter_oddnumbers([1, 6, 3, 6, 7, 11, 10, 4, 5, 14]) == [1, 3, 7, 11, 5]

def test_filter_oddnumbers_25():
    """Auto-generated test 25 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 5, 6, 2, 3, 1, 4, 6, 12, 6]) == [5, 3, 1]

def test_filter_oddnumbers_26():
    """Auto-generated test 26 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 5, 5, 8, 10, 10, 6, 11, 7, 9]) == [5, 5, 11, 7, 9]

def test_filter_oddnumbers_27():
    """Auto-generated test 27 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 7, 7, 5, 1, 10, 12, 8, 12, 10]) == [3, 7, 7, 5, 1]

def test_filter_oddnumbers_28():
    """Auto-generated test 28 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 7, 6, 6, 3, 8, 3, 11, 14, 9]) == [7, 3, 3, 11, 9]

def test_filter_oddnumbers_29():
    """Auto-generated test 29 for filter_oddnumbers"""
    assert filter_oddnumbers([6, 4, 6, 5, 2, 10, 7, 3, 8, 13]) == [5, 7, 3, 13]

def test_filter_oddnumbers_30():
    """Auto-generated test 30 for filter_oddnumbers"""
    assert filter_oddnumbers([1, 5, 1, 5, 1, 3, 6, 7, 5, 10]) == [1, 5, 1, 5, 1, 3, 7, 5]

def test_filter_oddnumbers_31():
    """Auto-generated test 31 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 4, 3, 5, 8, 7, 9, 12, 9, 10]) == [5, 3, 5, 7, 9, 9]

def test_filter_oddnumbers_32():
    """Auto-generated test 32 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 2, 2, 1, 5, 7, 5, 13, 8, 13]) == [3, 1, 5, 7, 5, 13, 13]

def test_filter_oddnumbers_33():
    """Auto-generated test 33 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 6, 8, 7, 10, 9, 5, 10, 10, 11]) == [3, 7, 9, 5, 11]

def test_filter_oddnumbers_34():
    """Auto-generated test 34 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 2, 5, 1, 5, 6, 12, 8, 10, 15]) == [5, 1, 5, 15]

def test_filter_oddnumbers_35():
    """Auto-generated test 35 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 3, 8, 4, 5, 2, 9, 11, 14, 7]) == [3, 3, 5, 9, 11, 7]

def test_filter_oddnumbers_36():
    """Auto-generated test 36 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 4, 7, 7, 1, 4, 4, 11, 12, 14]) == [5, 7, 7, 1, 11]

def test_filter_oddnumbers_37():
    """Auto-generated test 37 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 18, 46, 64, 85, 98]) == [5, 85]

def test_filter_oddnumbers_38():
    """Auto-generated test 38 for filter_oddnumbers"""
    assert filter_oddnumbers([8, 21, 47, 70, 80, 94]) == [21, 47]

def test_filter_oddnumbers_39():
    """Auto-generated test 39 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 18, 46, 62, 83, 98]) == [5, 83]

def test_filter_oddnumbers_40():
    """Auto-generated test 40 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 18, 41, 67, 88, 91]) == [5, 41, 67, 91]

def test_filter_oddnumbers_41():
    """Auto-generated test 41 for filter_oddnumbers"""
    assert filter_oddnumbers([10, 19, 46, 66, 86, 88]) == [19]

def test_filter_oddnumbers_42():
    """Auto-generated test 42 for filter_oddnumbers"""
    assert filter_oddnumbers([13, 24, 50, 72, 89, 96]) == [13, 89]

def test_filter_oddnumbers_43():
    """Auto-generated test 43 for filter_oddnumbers"""
    assert filter_oddnumbers([12, 19, 41, 68, 83, 93]) == [19, 41, 83, 93]

def test_filter_oddnumbers_44():
    """Auto-generated test 44 for filter_oddnumbers"""
    assert filter_oddnumbers([14, 16, 42, 65, 87, 88]) == [65, 87]

def test_filter_oddnumbers_45():
    """Auto-generated test 45 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 15, 43, 72, 80, 88]) == [5, 15, 43]

def test_filter_oddnumbers_46():
    """Auto-generated test 46 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 21, 45, 71, 81, 91]) == [9, 21, 45, 71, 81, 91]

def test_filter_oddnumbers_47():
    """Auto-generated test 47 for filter_oddnumbers"""
    assert filter_oddnumbers([6, 24, 50, 70, 89, 89]) == [89, 89]

def test_filter_oddnumbers_48():
    """Auto-generated test 48 for filter_oddnumbers"""
    assert filter_oddnumbers([10, 24, 47, 66, 89, 90]) == [47, 89]

def test_filter_oddnumbers_49():
    """Auto-generated test 49 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 22, 43, 69, 79, 91]) == [9, 43, 69, 79, 91]

def test_filter_oddnumbers_50():
    """Auto-generated test 50 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 25, 40, 70, 86, 92]) == [5, 25]

def test_filter_oddnumbers_51():
    """Auto-generated test 51 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 25, 48, 67, 79, 96]) == [9, 25, 67, 79]

def test_filter_oddnumbers_52():
    """Auto-generated test 52 for filter_oddnumbers"""
    assert filter_oddnumbers([7, 19, 41, 64, 85, 94]) == [7, 19, 41, 85]

def test_filter_oddnumbers_53():
    """Auto-generated test 53 for filter_oddnumbers"""
    assert filter_oddnumbers([13, 19, 50, 69, 89, 89]) == [13, 19, 69, 89, 89]

def test_filter_oddnumbers_54():
    """Auto-generated test 54 for filter_oddnumbers"""
    assert filter_oddnumbers([12, 23, 40, 68, 85, 93]) == [23, 85, 93]

def test_filter_oddnumbers_55():
    """Auto-generated test 55 for filter_oddnumbers"""
    assert filter_oddnumbers([6, 17, 41, 64, 86, 96]) == [17, 41]

def test_filter_oddnumbers_56():
    """Auto-generated test 56 for filter_oddnumbers"""
    assert filter_oddnumbers([11, 19, 42, 71, 87, 89]) == [11, 19, 71, 87, 89]

def test_filter_oddnumbers_57():
    """Auto-generated test 57 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 20, 43, 63, 79, 98]) == [5, 43, 63, 79]

def test_filter_oddnumbers_58():
    """Auto-generated test 58 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 17, 43, 72, 86, 94]) == [9, 17, 43]

def test_filter_oddnumbers_59():
    """Auto-generated test 59 for filter_oddnumbers"""
    assert filter_oddnumbers([12, 16, 45, 65, 87, 88]) == [45, 65, 87]

def test_filter_oddnumbers_60():
    """Auto-generated test 60 for filter_oddnumbers"""
    assert filter_oddnumbers([15, 21, 47, 65, 83, 96]) == [15, 21, 47, 65, 83]

def test_filter_oddnumbers_61():
    """Auto-generated test 61 for filter_oddnumbers"""
    assert filter_oddnumbers([11, 16, 49, 72, 89, 97]) == [11, 49, 89, 97]

def test_filter_oddnumbers_62():
    """Auto-generated test 62 for filter_oddnumbers"""
    assert filter_oddnumbers([14, 19, 47, 62, 83, 88]) == [19, 47, 83]

def test_filter_oddnumbers_63():
    """Auto-generated test 63 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 16, 41, 69, 84, 93]) == [9, 41, 69, 93]

def test_filter_oddnumbers_64():
    """Auto-generated test 64 for filter_oddnumbers"""
    assert filter_oddnumbers([15, 19, 40, 68, 83, 89]) == [15, 19, 83, 89]

def test_filter_oddnumbers_65():
    """Auto-generated test 65 for filter_oddnumbers"""
    assert filter_oddnumbers([13, 19, 41, 63, 84, 93]) == [13, 19, 41, 63, 93]

def test_filter_oddnumbers_66():
    """Auto-generated test 66 for filter_oddnumbers"""
    assert filter_oddnumbers([7, 25, 48, 62, 81, 95]) == [7, 25, 81, 95]

def test_filter_oddnumbers_67():
    """Auto-generated test 67 for filter_oddnumbers"""
    assert filter_oddnumbers([14, 20, 49, 67, 83, 96]) == [49, 67, 83]

def test_filter_oddnumbers_68():
    """Auto-generated test 68 for filter_oddnumbers"""
    assert filter_oddnumbers([11, 19, 49, 64, 88, 89]) == [11, 19, 49, 89]

def test_filter_oddnumbers_69():
    """Auto-generated test 69 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 21, 47, 66, 87, 92]) == [5, 21, 47, 87]

def test_filter_oddnumbers_70():
    """Auto-generated test 70 for filter_oddnumbers"""
    assert filter_oddnumbers([1, 10, 11, 13, 5, 7, 4]) == [1, 11, 13, 5, 7]

def test_filter_oddnumbers_71():
    """Auto-generated test 71 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 7, 11, 9, 9, 4, 3]) == [3, 7, 11, 9, 9, 3]

def test_filter_oddnumbers_72():
    """Auto-generated test 72 for filter_oddnumbers"""
    assert filter_oddnumbers([6, 2, 10, 8, 3, 5, 3]) == [3, 5, 3]

def test_filter_oddnumbers_73():
    """Auto-generated test 73 for filter_oddnumbers"""
    assert filter_oddnumbers([10, 8, 12, 4, 2, 6, 3]) == [3]

def test_filter_oddnumbers_74():
    """Auto-generated test 74 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 4, 14, 7, 3, 4, 6]) == [7, 3]

def test_filter_oddnumbers_75():
    """Auto-generated test 75 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 9, 14, 12, 6, 3, 3]) == [9, 9, 3, 3]

def test_filter_oddnumbers_76():
    """Auto-generated test 76 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 4, 9, 6, 8, 9, 2]) == [9, 9]

def test_filter_oddnumbers_77():
    """Auto-generated test 77 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 4, 8, 11, 8, 6, 4]) == [9, 11]

def test_filter_oddnumbers_78():
    """Auto-generated test 78 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 7, 8, 4, 1, 8, 5]) == [7, 1, 5]

def test_filter_oddnumbers_79():
    """Auto-generated test 79 for filter_oddnumbers"""
    assert filter_oddnumbers([7, 9, 8, 4, 6, 2, 3]) == [7, 9, 3]

def test_filter_oddnumbers_80():
    """Auto-generated test 80 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 8, 14, 10, 11, 5, 8]) == [9, 11, 5]

def test_filter_oddnumbers_81():
    """Auto-generated test 81 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 7, 10, 10, 9, 3, 5]) == [5, 7, 9, 3, 5]

def test_filter_oddnumbers_82():
    """Auto-generated test 82 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 12, 8, 13, 9, 3, 6]) == [3, 13, 9, 3]

def test_filter_oddnumbers_83():
    """Auto-generated test 83 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 12, 13, 8, 9, 8, 2]) == [5, 13, 9]

def test_filter_oddnumbers_84():
    """Auto-generated test 84 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 10, 13, 4, 11, 2, 2]) == [9, 13, 11]

def test_filter_oddnumbers_85():
    """Auto-generated test 85 for filter_oddnumbers"""
    assert filter_oddnumbers([1, 11, 10, 5, 9, 9, 5]) == [1, 11, 5, 9, 9, 5]

def test_filter_oddnumbers_86():
    """Auto-generated test 86 for filter_oddnumbers"""
    assert filter_oddnumbers([10, 2, 8, 7, 8, 7, 7]) == [7, 7, 7]

def test_filter_oddnumbers_87():
    """Auto-generated test 87 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 3, 4, 3, 2, 7, 5]) == [3, 3, 7, 5]

def test_filter_oddnumbers_88():
    """Auto-generated test 88 for filter_oddnumbers"""
    assert filter_oddnumbers([3, 10, 11, 7, 7, 7, 3]) == [3, 11, 7, 7, 7, 3]

def test_filter_oddnumbers_89():
    """Auto-generated test 89 for filter_oddnumbers"""
    assert filter_oddnumbers([9, 9, 10, 7, 10, 9, 2]) == [9, 9, 7, 9]

def test_filter_oddnumbers_90():
    """Auto-generated test 90 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 7, 6, 7, 10, 9, 8]) == [7, 7, 9]

def test_filter_oddnumbers_91():
    """Auto-generated test 91 for filter_oddnumbers"""
    assert filter_oddnumbers([10, 6, 7, 10, 2, 1, 6]) == [7, 1]

def test_filter_oddnumbers_92():
    """Auto-generated test 92 for filter_oddnumbers"""
    assert filter_oddnumbers([8, 11, 4, 12, 6, 9, 8]) == [11, 9]

def test_filter_oddnumbers_93():
    """Auto-generated test 93 for filter_oddnumbers"""
    assert filter_oddnumbers([1, 6, 9, 6, 8, 4, 7]) == [1, 9, 7]

def test_filter_oddnumbers_94():
    """Auto-generated test 94 for filter_oddnumbers"""
    assert filter_oddnumbers([4, 11, 4, 11, 2, 1, 1]) == [11, 11, 1, 1]

def test_filter_oddnumbers_95():
    """Auto-generated test 95 for filter_oddnumbers"""
    assert filter_oddnumbers([7, 3, 11, 10, 8, 1, 4]) == [7, 3, 11, 1]

def test_filter_oddnumbers_96():
    """Auto-generated test 96 for filter_oddnumbers"""
    assert filter_oddnumbers([5, 12, 9, 3, 7, 8, 2]) == [5, 9, 3, 7]

def test_filter_oddnumbers_97():
    """Auto-generated test 97 for filter_oddnumbers"""
    assert filter_oddnumbers([1, 6, 10, 12, 7, 6, 4]) == [1, 7]

def test_filter_oddnumbers_98():
    """Auto-generated test 98 for filter_oddnumbers"""
    assert filter_oddnumbers([6, 3, 6, 8, 3, 8, 4]) == [3, 3]

def test_filter_oddnumbers_99():
    """Auto-generated test 99 for filter_oddnumbers"""
    assert filter_oddnumbers([7, 5, 6, 12, 1, 7, 8]) == [7, 5, 1, 7]

def test_filter_oddnumbers_100():
    """Auto-generated test 100 for filter_oddnumbers"""
    assert filter_oddnumbers([10, 11, 8, 8, 5, 1, 3]) == [11, 5, 1, 3]

def test_filter_oddnumbers_101():
    """Auto-generated test 101 for filter_oddnumbers"""
    assert filter_oddnumbers([10, 5, 6, 6, 1, 8, 1]) == [5, 1, 1]

def test_filter_oddnumbers_102():
    """Auto-generated test 102 for filter_oddnumbers"""
    assert filter_oddnumbers([2, 8, 5, 13, 7, 5, 3]) == [5, 13, 7, 5, 3]

