class Orders:
    def combine_orders(self, requests, n_max):
        requests.sort(reverse=True)

        trips = 0

        start = 0
        end = len(requests) - 1

        while start <= end:
            if requests[start] + requests[end] <= n_max:
                trips += 1
                start += 1
                end -= 1
            else:
                trips += 1
                start += 1

        return trips


if __name__ == "__main__":
    orders = [10, 20, 60]
    n_max = 100
    expected_orders = 1

    how_many = Orders().combine_orders(orders, n_max)
    print(how_many)

    assert how_many == expected_orders
