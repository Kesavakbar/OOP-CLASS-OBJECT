class Hardisk:
    def __init__(self, tipe, size):
        self.tipe = tipe
        self.size = size

    def display_info(self):
        print("hardisk bertipe", self.tipe, "dengan ukuran", self.size)

def main():
    hardisk1 = Hardisk("kingstone", str("344 GB"))
    hardisk1.display_info()

if __name__ == "__main__" :
    main()

