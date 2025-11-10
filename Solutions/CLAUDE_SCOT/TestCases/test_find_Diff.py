import pytest
from Solutions.CLAUDE_SCOT.find_Diff import find_Diff

def test_find_Diff_1():
    """Auto-generated test 1 for find_Diff"""
    assert find_Diff([1,1,2,2,7,8,4,5,1,4],10) == 2

def test_find_Diff_2():
    """Auto-generated test 2 for find_Diff"""
    assert find_Diff([1,7,9,2,3,3,1,3,3],9) == 3

def test_find_Diff_3():
    """Auto-generated test 3 for find_Diff"""
    assert find_Diff([1,2,1,2],4) == 0

def test_find_Diff_4():
    """Auto-generated test 4 for find_Diff"""
    assert find_Diff([6, 4, 1, 5, 4, 13, 2, 4, 4, 6], 7) == 3

def test_find_Diff_5():
    """Auto-generated test 5 for find_Diff"""
    assert find_Diff([3, 2, 3, 4, 7, 5, 4, 1, 1, 7], 7) == 1

def test_find_Diff_6():
    """Auto-generated test 6 for find_Diff"""
    assert find_Diff([4, 1, 4, 7, 9, 12, 5, 3, 1, 7], 10) == 1

def test_find_Diff_7():
    """Auto-generated test 7 for find_Diff"""
    assert find_Diff([2, 4, 3, 4, 7, 8, 7, 9, 1, 3], 6) == 1

def test_find_Diff_8():
    """Auto-generated test 8 for find_Diff"""
    assert find_Diff([6, 4, 4, 4, 6, 7, 7, 6, 3, 1], 9) == 2

def test_find_Diff_9():
    """Auto-generated test 9 for find_Diff"""
    assert find_Diff([5, 1, 1, 5, 8, 9, 1, 10, 5, 9], 10) == 2

def test_find_Diff_10():
    """Auto-generated test 10 for find_Diff"""
    assert find_Diff([6, 5, 7, 6, 6, 8, 1, 7, 5, 7], 5) == 1

def test_find_Diff_11():
    """Auto-generated test 11 for find_Diff"""
    assert find_Diff([2, 4, 4, 5, 6, 11, 1, 10, 2, 7], 5) == 1

def test_find_Diff_12():
    """Auto-generated test 12 for find_Diff"""
    assert find_Diff([1, 3, 2, 4, 3, 10, 6, 5, 6, 7], 6) == 1

def test_find_Diff_13():
    """Auto-generated test 13 for find_Diff"""
    assert find_Diff([3, 1, 5, 4, 10, 10, 1, 5, 1, 3], 10) == 2

def test_find_Diff_14():
    """Auto-generated test 14 for find_Diff"""
    assert find_Diff([2, 3, 5, 1, 5, 12, 4, 6, 5, 6], 10) == 2

def test_find_Diff_15():
    """Auto-generated test 15 for find_Diff"""
    assert find_Diff([2, 3, 5, 6, 6, 5, 8, 2, 3, 4], 8) == 1

def test_find_Diff_16():
    """Auto-generated test 16 for find_Diff"""
    assert find_Diff([4, 4, 3, 7, 4, 10, 6, 9, 4, 9], 5) == 0

def test_find_Diff_17():
    """Auto-generated test 17 for find_Diff"""
    assert find_Diff([6, 2, 5, 6, 2, 6, 4, 8, 3, 1], 5) == 1

def test_find_Diff_18():
    """Auto-generated test 18 for find_Diff"""
    assert find_Diff([3, 5, 2, 6, 3, 10, 6, 1, 3, 1], 9) == 2

def test_find_Diff_19():
    """Auto-generated test 19 for find_Diff"""
    assert find_Diff([4, 5, 2, 4, 3, 4, 7, 7, 4, 3], 8) == 3

def test_find_Diff_20():
    """Auto-generated test 20 for find_Diff"""
    assert find_Diff([3, 2, 3, 4, 5, 11, 8, 8, 1, 5], 9) == 1

def test_find_Diff_21():
    """Auto-generated test 21 for find_Diff"""
    assert find_Diff([4, 6, 3, 4, 3, 12, 7, 5, 6, 1], 10) == 1

def test_find_Diff_22():
    """Auto-generated test 22 for find_Diff"""
    assert find_Diff([6, 5, 5, 7, 10, 11, 4, 1, 6, 8], 8) == 1

def test_find_Diff_23():
    """Auto-generated test 23 for find_Diff"""
    assert find_Diff([5, 3, 4, 1, 10, 6, 1, 4, 4, 3], 9) == 2

def test_find_Diff_24():
    """Auto-generated test 24 for find_Diff"""
    assert find_Diff([1, 2, 3, 3, 4, 12, 1, 2, 3, 7], 8) == 1

def test_find_Diff_25():
    """Auto-generated test 25 for find_Diff"""
    assert find_Diff([2, 5, 6, 2, 3, 4, 4, 6, 5, 7], 10) == 1

def test_find_Diff_26():
    """Auto-generated test 26 for find_Diff"""
    assert find_Diff([6, 5, 2, 5, 11, 4, 7, 1, 1, 3], 7) == 1

def test_find_Diff_27():
    """Auto-generated test 27 for find_Diff"""
    assert find_Diff([2, 1, 1, 7, 9, 6, 4, 6, 5, 7], 5) == 1

def test_find_Diff_28():
    """Auto-generated test 28 for find_Diff"""
    assert find_Diff([1, 3, 2, 2, 6, 5, 4, 6, 4, 8], 6) == 1

def test_find_Diff_29():
    """Auto-generated test 29 for find_Diff"""
    assert find_Diff([3, 2, 2, 1, 12, 3, 1, 5, 2, 8], 6) == 1

def test_find_Diff_30():
    """Auto-generated test 30 for find_Diff"""
    assert find_Diff([6, 5, 6, 4, 7, 9, 9, 8, 3, 3], 10) == 1

def test_find_Diff_31():
    """Auto-generated test 31 for find_Diff"""
    assert find_Diff([3, 2, 1, 6, 2, 11, 1, 2, 2, 4], 10) == 3

def test_find_Diff_32():
    """Auto-generated test 32 for find_Diff"""
    assert find_Diff([4, 5, 2, 1, 6, 6, 3, 2, 2, 2], 5) == 0

def test_find_Diff_33():
    """Auto-generated test 33 for find_Diff"""
    assert find_Diff([1, 4, 1, 4, 5, 5, 2, 3, 6, 7], 7) == 1

def test_find_Diff_34():
    """Auto-generated test 34 for find_Diff"""
    assert find_Diff([5, 2, 6, 3, 12, 3, 7, 10, 6, 2], 9) == 1

def test_find_Diff_35():
    """Auto-generated test 35 for find_Diff"""
    assert find_Diff([4, 4, 7, 5, 9, 7, 7, 9, 1, 1], 10) == 2

def test_find_Diff_36():
    """Auto-generated test 36 for find_Diff"""
    assert find_Diff([6, 1, 7, 2, 9, 6, 1, 1, 2, 5], 10) == 2

def test_find_Diff_37():
    """Auto-generated test 37 for find_Diff"""
    assert find_Diff([3, 9, 4, 2, 4, 1, 6, 8, 4], 5) == 0

def test_find_Diff_38():
    """Auto-generated test 38 for find_Diff"""
    assert find_Diff([4, 4, 11, 6, 7, 1, 5, 1, 1], 8) == 2

def test_find_Diff_39():
    """Auto-generated test 39 for find_Diff"""
    assert find_Diff([1, 8, 6, 5, 8, 1, 4, 1, 1], 8) == 3

def test_find_Diff_40():
    """Auto-generated test 40 for find_Diff"""
    assert find_Diff([1, 2, 14, 1, 1, 3, 4, 4, 3], 7) == 2

def test_find_Diff_41():
    """Auto-generated test 41 for find_Diff"""
    assert find_Diff([2, 2, 4, 5, 7, 3, 4, 7, 1], 5) == 1

def test_find_Diff_42():
    """Auto-generated test 42 for find_Diff"""
    assert find_Diff([4, 12, 14, 1, 8, 2, 4, 1, 8], 8) == 1

def test_find_Diff_43():
    """Auto-generated test 43 for find_Diff"""
    assert find_Diff([6, 12, 9, 5, 2, 4, 4, 2, 8], 4) == 0

def test_find_Diff_44():
    """Auto-generated test 44 for find_Diff"""
    assert find_Diff([2, 8, 7, 2, 2, 7, 6, 6, 5], 5) == 2

def test_find_Diff_45():
    """Auto-generated test 45 for find_Diff"""
    assert find_Diff([3, 6, 8, 4, 8, 8, 2, 5, 5], 9) == 1

def test_find_Diff_46():
    """Auto-generated test 46 for find_Diff"""
    assert find_Diff([4, 6, 9, 4, 6, 2, 4, 3, 5], 8) == 2

def test_find_Diff_47():
    """Auto-generated test 47 for find_Diff"""
    assert find_Diff([6, 7, 9, 3, 3, 4, 1, 7, 7], 7) == 1

def test_find_Diff_48():
    """Auto-generated test 48 for find_Diff"""
    assert find_Diff([1, 10, 10, 5, 6, 1, 1, 3, 5], 6) == 2

def test_find_Diff_49():
    """Auto-generated test 49 for find_Diff"""
    assert find_Diff([3, 2, 12, 4, 8, 2, 6, 6, 2], 9) == 2

def test_find_Diff_50():
    """Auto-generated test 50 for find_Diff"""
    assert find_Diff([5, 10, 12, 4, 2, 7, 1, 7, 4], 5) == 1

def test_find_Diff_51():
    """Auto-generated test 51 for find_Diff"""
    assert find_Diff([3, 11, 10, 3, 5, 8, 1, 8, 4], 5) == 1

def test_find_Diff_52():
    """Auto-generated test 52 for find_Diff"""
    assert find_Diff([3, 11, 13, 7, 8, 1, 6, 7, 3], 7) == 1

def test_find_Diff_53():
    """Auto-generated test 53 for find_Diff"""
    assert find_Diff([1, 11, 5, 2, 4, 8, 2, 5, 7], 7) == 1

def test_find_Diff_54():
    """Auto-generated test 54 for find_Diff"""
    assert find_Diff([1, 7, 10, 1, 5, 8, 3, 5, 2], 8) == 1

def test_find_Diff_55():
    """Auto-generated test 55 for find_Diff"""
    assert find_Diff([6, 5, 13, 1, 6, 6, 3, 3, 4], 5) == 1

def test_find_Diff_56():
    """Auto-generated test 56 for find_Diff"""
    assert find_Diff([1, 9, 11, 3, 5, 3, 2, 7, 7], 5) == 1

def test_find_Diff_57():
    """Auto-generated test 57 for find_Diff"""
    assert find_Diff([2, 2, 12, 3, 1, 4, 4, 6, 7], 8) == 1

def test_find_Diff_58():
    """Auto-generated test 58 for find_Diff"""
    assert find_Diff([1, 4, 5, 2, 2, 1, 6, 8, 3], 7) == 1

def test_find_Diff_59():
    """Auto-generated test 59 for find_Diff"""
    assert find_Diff([6, 3, 10, 2, 6, 8, 1, 2, 6], 9) == 2

def test_find_Diff_60():
    """Auto-generated test 60 for find_Diff"""
    assert find_Diff([6, 9, 13, 5, 4, 4, 1, 8, 1], 5) == 0

def test_find_Diff_61():
    """Auto-generated test 61 for find_Diff"""
    assert find_Diff([2, 12, 11, 4, 7, 3, 6, 1, 2], 5) == 1

def test_find_Diff_62():
    """Auto-generated test 62 for find_Diff"""
    assert find_Diff([6, 12, 8, 1, 5, 1, 5, 3, 6], 6) == 1

def test_find_Diff_63():
    """Auto-generated test 63 for find_Diff"""
    assert find_Diff([3, 11, 9, 6, 1, 2, 5, 8, 6], 6) == 0

def test_find_Diff_64():
    """Auto-generated test 64 for find_Diff"""
    assert find_Diff([1, 8, 5, 3, 8, 7, 3, 2, 1], 6) == 1

def test_find_Diff_65():
    """Auto-generated test 65 for find_Diff"""
    assert find_Diff([1, 9, 14, 3, 2, 6, 2, 7, 5], 5) == 1

def test_find_Diff_66():
    """Auto-generated test 66 for find_Diff"""
    assert find_Diff([5, 3, 11, 7, 3, 3, 2, 2, 4], 6) == 1

def test_find_Diff_67():
    """Auto-generated test 67 for find_Diff"""
    assert find_Diff([6, 8, 6, 5, 2, 3, 3, 3, 1], 8) == 2

def test_find_Diff_68():
    """Auto-generated test 68 for find_Diff"""
    assert find_Diff([2, 10, 9, 7, 7, 7, 2, 1, 5], 4) == 1

def test_find_Diff_69():
    """Auto-generated test 69 for find_Diff"""
    assert find_Diff([6, 6, 9, 6, 4, 3, 6, 4, 8], 4) == 1

def test_find_Diff_70():
    """Auto-generated test 70 for find_Diff"""
    assert find_Diff([6, 6, 3, 4], 4) == 0

def test_find_Diff_71():
    """Auto-generated test 71 for find_Diff"""
    assert find_Diff([5, 6, 4, 5], 1) == -1

def test_find_Diff_72():
    """Auto-generated test 72 for find_Diff"""
    assert find_Diff([3, 1, 6, 1], 3) == 0

def test_find_Diff_73():
    """Auto-generated test 73 for find_Diff"""
    assert find_Diff([4, 1, 1, 7], 2) == -2

def test_find_Diff_74():
    """Auto-generated test 74 for find_Diff"""
    assert find_Diff([6, 4, 1, 7], 1) == -1

def test_find_Diff_75():
    """Auto-generated test 75 for find_Diff"""
    assert find_Diff([3, 2, 2, 6], 3) == 0

def test_find_Diff_76():
    """Auto-generated test 76 for find_Diff"""
    assert find_Diff([4, 6, 1, 1], 4) == 1

def test_find_Diff_77():
    """Auto-generated test 77 for find_Diff"""
    assert find_Diff([6, 7, 5, 6], 4) == 1

def test_find_Diff_78():
    """Auto-generated test 78 for find_Diff"""
    assert find_Diff([3, 3, 3, 1], 4) == 0

def test_find_Diff_79():
    """Auto-generated test 79 for find_Diff"""
    assert find_Diff([2, 7, 5, 7], 1) == -1

def test_find_Diff_80():
    """Auto-generated test 80 for find_Diff"""
    assert find_Diff([3, 5, 6, 1], 3) == 0

def test_find_Diff_81():
    """Auto-generated test 81 for find_Diff"""
    assert find_Diff([5, 4, 4, 6], 2) == -2

def test_find_Diff_82():
    """Auto-generated test 82 for find_Diff"""
    assert find_Diff([1, 7, 2, 4], 4) == 0

def test_find_Diff_83():
    """Auto-generated test 83 for find_Diff"""
    assert find_Diff([3, 1, 5, 3], 4) == 1

def test_find_Diff_84():
    """Auto-generated test 84 for find_Diff"""
    assert find_Diff([2, 2, 2, 5], 1) == -1

def test_find_Diff_85():
    """Auto-generated test 85 for find_Diff"""
    assert find_Diff([6, 6, 4, 3], 1) == -1

def test_find_Diff_86():
    """Auto-generated test 86 for find_Diff"""
    assert find_Diff([4, 4, 2, 7], 1) == -1

def test_find_Diff_87():
    """Auto-generated test 87 for find_Diff"""
    assert find_Diff([5, 4, 2, 6], 1) == -1

def test_find_Diff_88():
    """Auto-generated test 88 for find_Diff"""
    assert find_Diff([5, 5, 5, 1], 4) == 0

def test_find_Diff_89():
    """Auto-generated test 89 for find_Diff"""
    assert find_Diff([4, 1, 4, 7], 4) == 1

def test_find_Diff_90():
    """Auto-generated test 90 for find_Diff"""
    assert find_Diff([3, 1, 4, 7], 1) == -1

def test_find_Diff_91():
    """Auto-generated test 91 for find_Diff"""
    assert find_Diff([2, 7, 5, 7], 3) == 0

def test_find_Diff_92():
    """Auto-generated test 92 for find_Diff"""
    assert find_Diff([1, 7, 4, 7], 3) == 0

def test_find_Diff_93():
    """Auto-generated test 93 for find_Diff"""
    assert find_Diff([6, 3, 6, 5], 4) == 0

def test_find_Diff_94():
    """Auto-generated test 94 for find_Diff"""
    assert find_Diff([6, 2, 1, 7], 4) == 0

def test_find_Diff_95():
    """Auto-generated test 95 for find_Diff"""
    assert find_Diff([3, 3, 4, 6], 1) == -1

def test_find_Diff_96():
    """Auto-generated test 96 for find_Diff"""
    assert find_Diff([3, 3, 4, 1], 1) == -1

def test_find_Diff_97():
    """Auto-generated test 97 for find_Diff"""
    assert find_Diff([5, 7, 6, 2], 1) == -1

def test_find_Diff_98():
    """Auto-generated test 98 for find_Diff"""
    assert find_Diff([3, 7, 5, 5], 1) == -1

def test_find_Diff_99():
    """Auto-generated test 99 for find_Diff"""
    assert find_Diff([1, 4, 3, 5], 3) == 0

def test_find_Diff_100():
    """Auto-generated test 100 for find_Diff"""
    assert find_Diff([4, 1, 5, 3], 4) == 0

def test_find_Diff_101():
    """Auto-generated test 101 for find_Diff"""
    assert find_Diff([1, 5, 4, 3], 2) == 0

def test_find_Diff_102():
    """Auto-generated test 102 for find_Diff"""
    assert find_Diff([2, 4, 6, 3], 2) == 0

