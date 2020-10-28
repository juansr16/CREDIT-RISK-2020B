import json
import fire

from fintools import CashFlow


class Main:

    @staticmethod
    def present_value(amount: float, rate: float, n: int):
        cfl = CashFlow(amount=amount, n=n)
        cf2 = CashFlow.pv(cfl, r=rate)
        js = CashFlow.to_dict(cf2)
        return json.dumps(js, indent=4)

    @staticmethod
    def future_value(amount: float, rate: float, n: int):
        cfl = CashFlow(amount=amount, n=n)
        cf2 = CashFlow.fv(cfl, r=rate)
        js = CashFlow.to_dict(cf2)
        return json.dumps(js, indent=4)


if __name__ == "__main__":
    fire.Fire(Main)
