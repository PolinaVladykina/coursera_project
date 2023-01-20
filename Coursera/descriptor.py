class Value:
    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = value * (1 - obj.commission)

class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission



def main():
    new_account = Account(0.1)
    new_account.amount = 100
    print(new_account.amount)

if __name__ == "__main__":
    main()


def get(self, key):
    if values == "ok\n\n":
        d = {}
        print('d')
    try:
        metric_value = float(metric_value)
        timestamp = int(timestamp)

        print(self)
    except ClientError:
        print("There is nothing here!:(")


def put(self, key, value, timestamp=None):
    if timestamp == None:
        timestamp = int(time.time())
    try:

    except ClientError:
        print("There is nothing here!:(")