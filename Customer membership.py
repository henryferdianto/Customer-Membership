from tabulate import tabulate
from math import sqrt
class membership
# inisialisasi data
    data = {
        "sumbul" : "Platinum"
        "Ana" : "Gold"
        "Cahya" : "Platinum"
    }
    #inisialisasi atribut
    def __init__(self,username) :
        self.username = username

    # method untuk menampilkan benefit membership
    def show_benefit(self):
        tables = [
            ["platinum", "15%", "Benefit Gold + Silver + Cashback max. 30%" ],
            ["Gold, "10%", "Benefit Silver" + "Voucher Ojek Online"],
            ["Silver","8%","Voucher Makanan"],
        ]
        headers = ["Membership", "Discount", "Another Benefit"]
        print("Benefit Membership PacCommerce")
        print("")
        print(tabulate(tables, headers, tablefmt='github',stralign='center'))

#method untuk menampilkan requirements membership
def show_requirements(self)
    tables = [
        ["platinum",8,15],
        ["Gold",6,10],
        ["Silver",5,7],
    ]

    headers =["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]

    print("Requirements Membership PacCommerce")
    print("")
    print(tabulate(tables, headers, tablefmt='github', numalign="center"))

#method untuk melakukan prediksi membership
#menggunakan euclidean distance
def predict_membership(self, username, monthly_expense, monthly_income):
    res =[]
    membership_parameter = [[8,15],[6,10],[5,7]]

    for index, _ in enumerate(membership_parameter):
        tmp = round(sqrt((monthly_expense - membership_parameter[index][0])**2 + (monthly_income - membership_parameter[index][1])**2), 2)
    res.append(tmp)

res_dict = {
    "Platinum" : res[0],
    "Gold" : res[1],
    "Silver" : res[2]
}
print(f"Hasil perhitungan Euclideab Distance dari user {self.username} adalah {res_dict}")

for member, distance in res_dict.items():
    if distance == min(res):
        self.data[username] = member
        return member
#method untuk menampilkan membership yang dimiliki
#dari database yang dimiliki
def show_membership(self, username):
    if username in self.data:
        return self.data.get(username)
#method untuk menghitung final pricec berdasarkan membership
def calculate_price(self, username, list_harga):

    try:
        if username in self.data:
            membership = self.data.get(username)
            if membership == "Platinum":
                total_harga = sum(list_harga) - (sum(list_harga)*0.15)
                return total_harga
            elif membership == "Gold":
                total_harga = sum(list_harga) - (sum(list_harga)* 0.10)
                return total_harga
            elif membership == "Silver" :
                total_harga = sum(list_harga)- (sum(list_harga)* 0.08)
                return total_harga
            else:
                raise Exception("Membership doesn't exist")
        else:
            raise Exception("Membership tidak ada di database")
    except :
        raise Exception("Invalid Process")
user_1.data
user_1.show_benefit()
user_1.show_requirements()
user_1.predict_membership(user_1.username,9,12)
user_1.calculate_price(user_1.username, [150000,200000,400000])
user_ana = Membership("Ana")
user_ana.data
user_ana.calculate_price(user_ana.username, [150000,200000,400000])
user_bambang = Membership("Bambang")
user_bambang.predict_membership(user_bambang.username,3, 4)
user_bambang.show_membership(user_bambang.username)
user_bambang.calculate_price(user_bambang.username,[300_000, 150_000, 1_250_000,15_000])
