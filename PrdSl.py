import sqlite3

class BaseHlpr:

    def __init__(self):

        self.con = sqlite3.connect("Mrk.db")
        self.cur = self.con.cursor()

    def create_tables(self):

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                size REAL NOT NULL,
                get_price REAL NOT NULL,
                sale_price REAL NOT NULL,
                count INTEGER NOT NULL
            )
        """)

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS sale(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pid INTEGER NOT NULL,
                count INTEGER NOT NULL,
                FOREIGN KEY(pid) REFERENCES product(id)
            )
        """)

        self.con.commit()


    def insert_prod(self, name, size, get_price, sale_price, count):

        try:

            self.cur.execute("""
                INSERT INTO product(
                    name,
                    size,
                    get_price,
                    sale_price,
                    count
                )
                VALUES(?,?,?,?,?)
            """, (
                name,
                float(size),
                float(get_price),
                float(sale_price),
                int(count)
            ))

            self.con.commit()
            return True

        except Exception as e:

            self.con.rollback()
            print("Insert Error:", e)
            return False

    def select_prod(self):

        self.cur.execute("SELECT id, name, size, get_price, sale_price, count FROM product")
        return self.cur.fetchall()


    def check_count(self, pid):

        self.cur.execute(
            "SELECT count FROM product WHERE id=?",
            (pid,)
        )

        cnt = self.cur.fetchone()

        if cnt is None:
            return None

        return cnt[0]

    def sell_prod(self, pid, count):

        try:

            pid = int(pid)
            count = int(count)

            cnt = self.check_count(pid)

            if cnt is None:
                return "product not found"

            if cnt < count:
                return "not enough product"

            self.cur.execute("""
                INSERT INTO sale(pid, count)
                VALUES(?,?)
            """, (pid, count))

            self.cur.execute("""
                UPDATE product
                SET count=?
                WHERE id=?
            """, (cnt - count, pid))

            self.con.commit()

            return "success"

        except Exception as e:

            self.con.rollback()
            print("Sale Error:", e)
            return "error"

    def select_sale(self):

        self.cur.execute("""
            SELECT
                sale.id,
                product.name,
                sale.count
            FROM sale
            JOIN product
            ON sale.pid = product.id
        """)

        return self.cur.fetchall()


    def get_profit(self, pid):

        self.cur.execute("""
            SELECT
                COALESCE(SUM(s.count), 0),
                p.get_price,
                p.sale_price
            FROM product p
            LEFT JOIN sale s
            ON p.id = s.pid
            WHERE p.id=?
            GROUP BY p.id
        """, (pid,))

        row = self.cur.fetchone()

        if row is None:
            return None

        total_count, get_price, sale_price = row

        profit = total_count * (sale_price - get_price)

        return profit


    def show_info(self):

        return "Connected successfully"


    def close(self):

        self.con.close()


"""
if __name__ == "__main__":

    bs = BaseHlpr()

    bs.create_tables()

    print(bs.show_info())

    while True:

        op = input(
            "\n1 - პროდუქტის დამატება"
            "\n2 - გაყიდვა"
            "\n3 - პროდუქციის ნახვა"
            "\n4 - გაყიდვების ნახვა"
            "\n5 - მოგების ნახვა"
            "\n6 - გამოსვლა"
            "\n-----> "
        )

        if op == "1":

            try:

                name = input("სახელი: ")
                size = input("ზომა: ")
                get_price = input("მიღების ფასი: ")
                sale_price = input("გაყიდვის ფასი: ")
                count = input("რაოდენობა: ")

                if (
                    not name.strip()
                    or not size.strip()
                    or not get_price.strip()
                    or not sale_price.strip()
                    or not count.strip()
                ):
                    print("შეავსე ყველა ველი")
                    continue

                res = bs.insert_prod(
                    name,
                    size,
                    get_price,
                    sale_price,
                    count
                )

                if res:
                    print("პროდუქტი დაემატა")
                else:
                    print("დამატება ვერ შესრულდა")

            except Exception as e:
                print(e)
        elif op == "2":

            pid = input("პროდუქტის ID: ")
            count = input("რაოდენობა: ")

            res = bs.sell_prod(pid, count)

            print(res)
        elif op == "3":

            rows = bs.select_prod()

            for row in rows:
                print(row)
        elif op == "4":

            rows = bs.select_sale()

            for row in rows:
                print(row)

        elif op == "5":

            pid = input("პროდუქტის ID: ")

            profit = bs.get_profit(pid)

            if profit is None:
                print("პროდუქტი ვერ მოიძებნა")
            else:
                print("მოგება:", profit)

        elif op == "6":

            bs.close()
            break

        else:
            print("არასწორი ოპერაცია")
"""