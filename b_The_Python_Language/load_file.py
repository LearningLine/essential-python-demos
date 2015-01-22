
def load_file():

    fin = open("Sacramentorealestatetransactions.csv")

    with open("Sacramentorealestatetransactions.csv") as fin:

        header = fin.readline()

        data = []
        for line in fin:
            parts = line.split(',')

            sq_ft = int(parts[6])
            price = int(parts[9])

            if 1000 <= sq_ft and sq_ft <= 2000:
                data.append(price)

        final = sorted(data)
        print("Highest price: {0:,} and lowest: ${1:,}".format(
            final[-1], final[0]
        ))
