import csv
import datetime


def select_by_date(transactions,begin,end):
    res=[e for e in transactions if begin<=e["purchase_date"]<=end]
    res.sort(key=lambda e:e["purchase_date"])
    return res

def prepare_data(transactions:list):
    for e in transactions:
        arr=e["purchase_date"].split("-")
        e["purchase_date"] = datetime.date(year=int(arr[2]), month=int(arr[1]), day=int(arr[0]))
        for key in e:
            try:
                e[key]=int(e[key])
            except:
                pass
    transactions.sort(key=lambda e:e["name"].lower())

def who_purchased(transactions,good):
    return [e for e in transactions if e[good]>0]

def compute_price(transaction,prices):
    return sum([prices[good]*transaction[good] for good in prices])

def compute_by_customer(transactions,prices):
    res={}
    for e in transactions:
        if not e["name"] in res:
            res[e["name"]]=0
        res[e["name"]]=res[e["name"]]+compute_price(e,prices)
    return res

# code to load data from file
with open("purchase.csv") as f:
    reader=csv.DictReader(f)
    transactions=[e for e in reader]


prepare_data(transactions)
# print(transactions)
for t,p in compute_by_customer(transactions,{'flour':90,'milk':130,'cheese':150,'water':50,'rice':180,'chocolate':200,'cake':250,'oil':130,'butter':400}).items():#select_by_date(transactions,begin=datetime.date(2024,12,1),end=datetime.date(2024,12,31)):
    #print(f"{t['name']} bought on {t['purchase_date']} for {compute_price(t,{'flour':90,'milk':130,'cheese':150,'water':50,'rice':180,'chocolate':200,'cake':250,'oil':130,'butter':400})}")
    print(f"{t} bought for {p}")    
