import pytest
from Solutions.QWEN_SCOT.find_peak import find_peak

def test_find_peak_1():
    """Auto-generated test 1 for find_peak"""
    assert find_peak([1, 3, 20, 4, 1, 0], 6) == 2

def test_find_peak_2():
    """Auto-generated test 2 for find_peak"""
    assert find_peak([2, 3, 4, 5, 6], 5) == 4

def test_find_peak_3():
    """Auto-generated test 3 for find_peak"""
    assert find_peak([8, 9, 11, 12, 14, 15], 6) == 5

def test_find_peak_4():
    """Auto-generated test 4 for find_peak"""
    assert find_peak([2, 1, 20, 1, 3, 1], 9) == 4

def test_find_peak_5():
    """Auto-generated test 5 for find_peak"""
    assert find_peak([1, 7, 22, 8, 6, 3], 3) == 2

def test_find_peak_6():
    """Auto-generated test 6 for find_peak"""
    assert find_peak([5, 2, 24, 9, 5, 3], 4) == 0

def test_find_peak_7():
    """Auto-generated test 7 for find_peak"""
    assert find_peak([5, 5, 25, 9, 5, 1], 6) == 2

def test_find_peak_8():
    """Auto-generated test 8 for find_peak"""
    assert find_peak([6, 2, 15, 9, 2, 5], 5) == 2

def test_find_peak_9():
    """Auto-generated test 9 for find_peak"""
    assert find_peak([6, 8, 17, 1, 5, 4], 9) == 4

def test_find_peak_10():
    """Auto-generated test 10 for find_peak"""
    assert find_peak([6, 2, 25, 7, 3, 4], 1) == 0

def test_find_peak_11():
    """Auto-generated test 11 for find_peak"""
    assert find_peak([6, 2, 25, 8, 6, 4], 4) == 0

def test_find_peak_12():
    """Auto-generated test 12 for find_peak"""
    assert find_peak([1, 7, 22, 4, 4, 1], 3) == 2

def test_find_peak_13():
    """Auto-generated test 13 for find_peak"""
    assert find_peak([4, 3, 24, 7, 3, 2], 8) == 0

def test_find_peak_14():
    """Auto-generated test 14 for find_peak"""
    assert find_peak([3, 8, 18, 9, 6, 5], 9) == 2

def test_find_peak_15():
    """Auto-generated test 15 for find_peak"""
    assert find_peak([5, 5, 20, 2, 5, 3], 4) == 2

def test_find_peak_16():
    """Auto-generated test 16 for find_peak"""
    assert find_peak([3, 4, 25, 4, 2, 4], 10) == 2

def test_find_peak_17():
    """Auto-generated test 17 for find_peak"""
    assert find_peak([5, 2, 25, 7, 2, 2], 4) == 0

def test_find_peak_18():
    """Auto-generated test 18 for find_peak"""
    assert find_peak([6, 1, 20, 1, 4, 3], 5) == 2

def test_find_peak_19():
    """Auto-generated test 19 for find_peak"""
    assert find_peak([3, 6, 18, 6, 5, 2], 9) == 2

def test_find_peak_20():
    """Auto-generated test 20 for find_peak"""
    assert find_peak([3, 3, 22, 6, 5, 4], 1) == 0

def test_find_peak_21():
    """Auto-generated test 21 for find_peak"""
    assert find_peak([4, 5, 23, 2, 2, 3], 1) == 0

def test_find_peak_22():
    """Auto-generated test 22 for find_peak"""
    assert find_peak([1, 7, 24, 7, 6, 3], 10) == 2

def test_find_peak_23():
    """Auto-generated test 23 for find_peak"""
    assert find_peak([3, 5, 22, 6, 3, 3], 5) == 2

def test_find_peak_24():
    """Auto-generated test 24 for find_peak"""
    assert find_peak([1, 1, 25, 5, 5, 3], 8) == 2

def test_find_peak_25():
    """Auto-generated test 25 for find_peak"""
    assert find_peak([5, 1, 15, 8, 2, 5], 3) == 0

def test_find_peak_26():
    """Auto-generated test 26 for find_peak"""
    assert find_peak([5, 1, 16, 9, 5, 4], 9) == 0

def test_find_peak_27():
    """Auto-generated test 27 for find_peak"""
    assert find_peak([3, 7, 16, 9, 4, 5], 10) == 2

def test_find_peak_28():
    """Auto-generated test 28 for find_peak"""
    assert find_peak([1, 1, 17, 9, 5, 3], 8) == 2

def test_find_peak_29():
    """Auto-generated test 29 for find_peak"""
    assert find_peak([3, 6, 19, 8, 2, 5], 3) == 2

def test_find_peak_30():
    """Auto-generated test 30 for find_peak"""
    assert find_peak([1, 1, 18, 1, 4, 5], 6) == 2

def test_find_peak_31():
    """Auto-generated test 31 for find_peak"""
    assert find_peak([5, 1, 21, 9, 2, 3], 7) == 0

def test_find_peak_32():
    """Auto-generated test 32 for find_peak"""
    assert find_peak([3, 3, 17, 2, 2, 5], 1) == 0

def test_find_peak_33():
    """Auto-generated test 33 for find_peak"""
    assert find_peak([1, 4, 17, 8, 2, 5], 4) == 2

def test_find_peak_34():
    """Auto-generated test 34 for find_peak"""
    assert find_peak([4, 2, 19, 6, 2, 2], 6) == 2

def test_find_peak_35():
    """Auto-generated test 35 for find_peak"""
    assert find_peak([3, 1, 21, 9, 1, 5], 6) == 2

def test_find_peak_36():
    """Auto-generated test 36 for find_peak"""
    assert find_peak([3, 2, 20, 2, 4, 1], 10) == 4

def test_find_peak_37():
    """Auto-generated test 37 for find_peak"""
    assert find_peak([2, 6, 2, 7, 11], 1) == 0

def test_find_peak_38():
    """Auto-generated test 38 for find_peak"""
    assert find_peak([1, 2, 6, 6, 3], 1) == 0

def test_find_peak_39():
    """Auto-generated test 39 for find_peak"""
    assert find_peak([7, 3, 8, 9, 8], 2) == 0

def test_find_peak_40():
    """Auto-generated test 40 for find_peak"""
    assert find_peak([3, 4, 9, 1, 11], 3) == 2

def test_find_peak_41():
    """Auto-generated test 41 for find_peak"""
    assert find_peak([6, 1, 4, 3, 2], 4) == 0

def test_find_peak_42():
    """Auto-generated test 42 for find_peak"""
    assert find_peak([5, 6, 9, 3, 7], 1) == 0

def test_find_peak_43():
    """Auto-generated test 43 for find_peak"""
    assert find_peak([4, 2, 8, 1, 8], 8) == 0

def test_find_peak_44():
    """Auto-generated test 44 for find_peak"""
    assert find_peak([2, 1, 2, 8, 8], 1) == 0

def test_find_peak_45():
    """Auto-generated test 45 for find_peak"""
    assert find_peak([2, 5, 9, 8, 2], 8) == 2

def test_find_peak_46():
    """Auto-generated test 46 for find_peak"""
    assert find_peak([1, 6, 9, 5, 9], 1) == 0

def test_find_peak_47():
    """Auto-generated test 47 for find_peak"""
    assert find_peak([6, 2, 3, 1, 6], 1) == 0

def test_find_peak_48():
    """Auto-generated test 48 for find_peak"""
    assert find_peak([3, 3, 9, 5, 6], 7) == 2

def test_find_peak_49():
    """Auto-generated test 49 for find_peak"""
    assert find_peak([6, 4, 1, 7, 7], 7) == 3

def test_find_peak_50():
    """Auto-generated test 50 for find_peak"""
    assert find_peak([6, 6, 9, 4, 1], 8) == 2

def test_find_peak_51():
    """Auto-generated test 51 for find_peak"""
    assert find_peak([5, 5, 6, 6, 10], 1) == 0

def test_find_peak_52():
    """Auto-generated test 52 for find_peak"""
    assert find_peak([2, 7, 6, 9, 4], 2) == 1

def test_find_peak_53():
    """Auto-generated test 53 for find_peak"""
    assert find_peak([2, 5, 6, 2, 6], 5) == 2

def test_find_peak_54():
    """Auto-generated test 54 for find_peak"""
    assert find_peak([1, 8, 6, 9, 6], 10) == 1

def test_find_peak_55():
    """Auto-generated test 55 for find_peak"""
    assert find_peak([5, 4, 8, 6, 5], 5) == 2

def test_find_peak_56():
    """Auto-generated test 56 for find_peak"""
    assert find_peak([4, 8, 1, 2, 2], 4) == 1

def test_find_peak_57():
    """Auto-generated test 57 for find_peak"""
    assert find_peak([2, 1, 4, 8, 2], 3) == 0

def test_find_peak_58():
    """Auto-generated test 58 for find_peak"""
    assert find_peak([6, 5, 3, 10, 1], 7) == 3

def test_find_peak_59():
    """Auto-generated test 59 for find_peak"""
    assert find_peak([1, 7, 3, 4, 7], 2) == 1

def test_find_peak_60():
    """Auto-generated test 60 for find_peak"""
    assert find_peak([3, 1, 5, 10, 9], 5) == 3

def test_find_peak_61():
    """Auto-generated test 61 for find_peak"""
    assert find_peak([2, 6, 6, 9, 6], 2) == 1

def test_find_peak_62():
    """Auto-generated test 62 for find_peak"""
    assert find_peak([2, 6, 1, 4, 4], 3) == 1

def test_find_peak_63():
    """Auto-generated test 63 for find_peak"""
    assert find_peak([1, 4, 4, 6, 1], 6) == 3

def test_find_peak_64():
    """Auto-generated test 64 for find_peak"""
    assert find_peak([5, 7, 1, 2, 11], 2) == 1

def test_find_peak_65():
    """Auto-generated test 65 for find_peak"""
    assert find_peak([5, 3, 2, 9, 4], 6) == 0

def test_find_peak_66():
    """Auto-generated test 66 for find_peak"""
    assert find_peak([1, 1, 6, 8, 3], 2) == 0

def test_find_peak_67():
    """Auto-generated test 67 for find_peak"""
    assert find_peak([6, 6, 6, 10, 1], 10) == 1

def test_find_peak_68():
    """Auto-generated test 68 for find_peak"""
    assert find_peak([1, 4, 2, 5, 1], 10) == 1

def test_find_peak_69():
    """Auto-generated test 69 for find_peak"""
    assert find_peak([1, 6, 5, 7, 5], 1) == 0

def test_find_peak_70():
    """Auto-generated test 70 for find_peak"""
    assert find_peak([9, 13, 9, 17, 17, 18], 3) == 1

def test_find_peak_71():
    """Auto-generated test 71 for find_peak"""
    assert find_peak([9, 6, 16, 9, 13, 11], 6) == 2

def test_find_peak_72():
    """Auto-generated test 72 for find_peak"""
    assert find_peak([12, 7, 7, 17, 11, 10], 9) == 0

def test_find_peak_73():
    """Auto-generated test 73 for find_peak"""
    assert find_peak([6, 8, 11, 16, 14, 10], 6) == 3

def test_find_peak_74():
    """Auto-generated test 74 for find_peak"""
    assert find_peak([5, 11, 6, 10, 19, 16], 10) == 4

def test_find_peak_75():
    """Auto-generated test 75 for find_peak"""
    assert find_peak([6, 4, 15, 14, 15, 14], 5) == 2

def test_find_peak_76():
    """Auto-generated test 76 for find_peak"""
    assert find_peak([4, 8, 8, 11, 15, 12], 4) == 1

def test_find_peak_77():
    """Auto-generated test 77 for find_peak"""
    assert find_peak([5, 11, 8, 17, 14, 16], 2) == 1

def test_find_peak_78():
    """Auto-generated test 78 for find_peak"""
    assert find_peak([6, 6, 9, 8, 11, 18], 5) == 2

def test_find_peak_79():
    """Auto-generated test 79 for find_peak"""
    assert find_peak([5, 9, 11, 9, 16, 13], 6) == 2

def test_find_peak_80():
    """Auto-generated test 80 for find_peak"""
    assert find_peak([6, 11, 16, 13, 12, 13], 4) == 2

def test_find_peak_81():
    """Auto-generated test 81 for find_peak"""
    assert find_peak([13, 4, 14, 17, 11, 20], 6) == 3

def test_find_peak_82():
    """Auto-generated test 82 for find_peak"""
    assert find_peak([6, 12, 10, 9, 9, 19], 1) == 0

def test_find_peak_83():
    """Auto-generated test 83 for find_peak"""
    assert find_peak([6, 13, 16, 15, 11, 11], 1) == 0

def test_find_peak_84():
    """Auto-generated test 84 for find_peak"""
    assert find_peak([11, 12, 12, 14, 12, 13], 2) == 1

def test_find_peak_85():
    """Auto-generated test 85 for find_peak"""
    assert find_peak([8, 4, 14, 13, 17, 18], 2) == 0

def test_find_peak_86():
    """Auto-generated test 86 for find_peak"""
    assert find_peak([11, 12, 9, 13, 16, 13], 9) == 4

def test_find_peak_87():
    """Auto-generated test 87 for find_peak"""
    assert find_peak([13, 8, 9, 9, 15, 10], 7) == 4

def test_find_peak_88():
    """Auto-generated test 88 for find_peak"""
    assert find_peak([7, 5, 14, 17, 15, 11], 2) == 0

def test_find_peak_89():
    """Auto-generated test 89 for find_peak"""
    assert find_peak([13, 11, 7, 17, 11, 18], 8) == 3

def test_find_peak_90():
    """Auto-generated test 90 for find_peak"""
    assert find_peak([6, 14, 15, 13, 12, 14], 4) == 2

def test_find_peak_91():
    """Auto-generated test 91 for find_peak"""
    assert find_peak([12, 4, 9, 7, 9, 19], 3) == 0

def test_find_peak_92():
    """Auto-generated test 92 for find_peak"""
    assert find_peak([4, 9, 16, 17, 16, 20], 8) == 3

def test_find_peak_93():
    """Auto-generated test 93 for find_peak"""
    assert find_peak([4, 12, 13, 11, 10, 20], 3) == 2

def test_find_peak_94():
    """Auto-generated test 94 for find_peak"""
    assert find_peak([10, 8, 9, 8, 19, 18], 2) == 0

def test_find_peak_95():
    """Auto-generated test 95 for find_peak"""
    assert find_peak([11, 10, 9, 14, 17, 13], 11) == 0

def test_find_peak_96():
    """Auto-generated test 96 for find_peak"""
    assert find_peak([10, 6, 8, 14, 15, 16], 1) == 0

def test_find_peak_97():
    """Auto-generated test 97 for find_peak"""
    assert find_peak([10, 7, 12, 7, 10, 10], 6) == 2

def test_find_peak_98():
    """Auto-generated test 98 for find_peak"""
    assert find_peak([10, 7, 15, 13, 17, 14], 8) == 0

def test_find_peak_99():
    """Auto-generated test 99 for find_peak"""
    assert find_peak([6, 4, 9, 13, 11, 12], 4) == 0

def test_find_peak_100():
    """Auto-generated test 100 for find_peak"""
    assert find_peak([13, 6, 10, 7, 13, 15], 8) == 0

def test_find_peak_101():
    """Auto-generated test 101 for find_peak"""
    assert find_peak([9, 10, 16, 17, 11, 12], 8) == 3

def test_find_peak_102():
    """Auto-generated test 102 for find_peak"""
    assert find_peak([3, 8, 8, 10, 16, 17], 2) == 1

