import pytest
import yaml

from calculator import Calculator

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc

@pytest.fixture(scope="module")
def scmo():
    print("开始计算")
    yield
    print("结束计算")

with open("./data.yml", "rb") as i:
    data = yaml.safe_load(i)
    add_tadd = data["add"]
    add_ids = data["addids"]
    sub_tsub = data["sub"]
    mul_tmul = data["mul"]
    div_tdiv = data["div"]

@pytest.fixture(params=add_tadd,ids=add_ids)
def get_add(request):
    add = request.param
    return add

@pytest.fixture(params=sub_tsub,ids=add_ids)
def get_sub(request):
    sub=request.param
    return sub

@pytest.fixture(params=mul_tmul,ids=add_ids)
def get_mul(request):
    mul=request.param
    return mul

@pytest.fixture(params=div_tdiv)
def get_div(request):
    div=request.param
    return div