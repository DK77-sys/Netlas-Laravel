import netlas, sys, json


class Heker:
    def __init__(self):
        self.apikey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        self.connect = netlas.Netlas(api_key=self.apikey)
        self.ekstrak = netlas.helpers

    def start_search(self, search):
        print("Default Page: 0")
        try:
            # sampai = 1
            sampai = int(input("Sampai Page: "))
        except:
            print("Must Integer!")
            sys.exit()

        for pages in range(sampai):
            query_res = self.connect.query(
                query=search, datatype="response", page=pages
            )
            extract = self.ekstrak.dump_object(data=query_res)
            ojs = json.loads(extract)
            try:
                for x in ojs["items"]:
                    with open("Res.txt", "a+") as r:
                        r.write(x["data"]["ip"] + "\n" + x["data"]["domain"])
                        r.close()
                    print(x["data"]["ip"])
            except:
                print("Limit Page")


Heker().start_search("laravel")
