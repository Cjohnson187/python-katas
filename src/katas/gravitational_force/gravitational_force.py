"""
https://www.codewars.com/kata/5b609ebc8f47bd595e000627/train/python

Your job is to find the gravitational force between two spherical objects (obj1 , obj2).
input
Two arrays are given :

arr_val (value array), consists of 3 elements
1st element : mass of obj 1
2nd element : mass of obj 2
3rd element : distance between their centers
arr_unit (unit array), consists of 3 elements
1st element : unit for mass of obj 1
2nd element : unit for mass of obj 2
3rd element : unit for distance between their centers
mass units are :

kilogram (kg)
gram (g)
milligram (mg)
microgram (μg)
pound (lb)

distance units are :

meter (m)
centimeter (cm)
millimeter (mm)
micrometer (μm)
feet (ft)

Note
value of G = 6.67 × 10−11 N⋅kg−2⋅m2

1 ft = 0.3048 m

1 lb = 0.453592 kg

return value must be Newton for force (obviously)

μ copy this from here to use it in your solution
"""

def convert_to_kilogram(value, unit):
    units = {
        "kg": 1,
        "g": 0.001,
        "mg": 1e-6,
        "μg": 1e-9,
        "ug": 1e-9,
        "lb": 0.453592,
        "lbs": 0.453592
    }
    return value * units.get(unit, 1)

def convert_to_meters(value, unit):
    units = {
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "μm": 1e-6,
        "um": 1e-6,
        "ft": 0.3048
    }
    return value * units.get(unit, 1)

def solution(arr_val, arr_unit):
    m1 = convert_to_kilogram(arr_val[0], arr_unit[0])
    m2 = convert_to_kilogram(arr_val[1], arr_unit[1])
    r = convert_to_meters(arr_val[2], arr_unit[2])
    return (6.67e-11 * m1 * m2) / (r ** 2)



if __name__ == "__main__":
    arr_val = [1000, 1000, 100]
    arr_unit = ["g", "kg", "m"]
    result = solution(arr_val, arr_unit)
    print(result)