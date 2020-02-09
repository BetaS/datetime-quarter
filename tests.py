from datequarter import DateQuarter


if __name__ == "__main__":
    quarter1 = DateQuarter(2019, 1)
    quarter2 = DateQuarter(2018, 4)

    print(list(DateQuarter.between(quarter1, quarter2)))

