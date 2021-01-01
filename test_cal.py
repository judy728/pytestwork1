import pytest

class TestCalc:
    @pytest.mark.first
    def test_add(self,get_calc, get_add,scmo):
        radd = None
        try:
            radd = get_calc.add(get_add[0],get_add[1])
            if isinstance(radd,float):
                radd = round(radd,2)
        except Exception as f:
            print(f)
        assert radd == get_add[2]

    @pytest.mark.run(order=4)
    # @pytest.mark.four
    def test_div(self,get_calc,get_div,scmo):
        try:
            rdiv = get_calc.div(get_div[0],get_div[1])
            rmul = round(rdiv,2)
            assert rdiv == get_div[2]
        except ZeroDivisionError:
            print("注意：除数不能输入为0")

    @pytest.mark.second
    def test_sub(self,get_calc,get_sub,scmo):
        rsub = None
        rsub = get_calc.sub(get_sub[0],get_sub[1])
        assert rsub == get_sub[2]

    @pytest.mark.run(order=3)
    # @pytest.mark.three
    def test_mul(self, get_mul, get_calc, scmo):
        rmul = get_calc.mul(get_mul[0], get_mul[1])
        # if isinstance(rmul,float):
        rmul = round(rmul, 2)
        assert rmul == get_mul[2]



