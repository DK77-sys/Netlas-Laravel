import netlas, sys, json


class Heker:
    def __init__(self, apikey):
        self.connect = netlas.Netlas(api_key=apikey)
        self.ekstrak = netlas.helpers

    def start_search(self, search):
        print("Default Page: 0")
        try:
            dari = int(input("Dari Page: "))
            sampai = int(input("Sampai Page: "))
        except:
            print("Must Integer!")
            sys.exit()

        for pages in range(dari, sampai):
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

api = input("Api Netlas: ")
dork = input("Dork: ")
Heker(api).start_search(dork)
