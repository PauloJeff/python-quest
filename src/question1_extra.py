class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return "id={}, debt={}".format(self.id, self.debt)

    @classmethod
    def create_contract(cls, id, debt):
        return cls(id, debt)


class Contracts:
    def __init__(self):
        self.contracts = []

    def add_contract(self, id, debt):
        self.contracts.append(Contract.create_contract(id, debt))

    def get_top_N_open_contracts(self, renegotiated_contracts, top_n):
        open_contracts = [
            contract
            for contract in self.contracts
            if contract.id not in renegotiated_contracts
        ]

        open_contracts.sort(key=lambda contract: contract.debt, reverse=True)

        top_n_debtors = [contract.id for contract in open_contracts[:top_n]]

        return top_n_debtors


if __name__ == "__main__":
    contracts = Contracts()
    contracts.add_contract(1, 5)
    contracts.add_contract(2, 5)
    contracts.add_contract(3, 5)
    contracts.add_contract(4, 5)
    contracts.add_contract(5, 5)

    renegotiated = [3]
    top_n = 3

    actual_open_contracts = contracts.get_top_N_open_contracts(renegotiated, top_n)

    expected_open_contracts = [1, 2, 4]
    print(actual_open_contracts)
    assert expected_open_contracts == actual_open_contracts