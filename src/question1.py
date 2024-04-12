class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return "id={}, debt={}".format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        renegotiated_contracts_set = set(renegotiated_contracts)

        open_contracts = [
            contract
            for contract in open_contracts
            if contract.id not in renegotiated_contracts_set
        ]

        open_contracts.sort(key=lambda contract: contract.debt, reverse=True)

        top_n_debtors = [contract.id for contract in open_contracts[:top_n]]

        return top_n_debtors


if __name__ == "__main__":
    contracts = [
        Contract(1, 5),
        Contract(2, 5),
        Contract(3, 5),
        Contract(4, 5),
        Contract(5, 5),
    ]
    renegotiated = [3]
    top_n = 3

    actual_open_contracts = Contracts().get_top_N_open_contracts(
        contracts, renegotiated, top_n
    )

    expected_open_contracts = [1, 2, 4]
    print(actual_open_contracts)
    assert expected_open_contracts == actual_open_contracts
