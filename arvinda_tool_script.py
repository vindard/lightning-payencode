from lightning_address import decode_func as decodepayreq
import json, ast

# Invoices gotten from publicly shared #LNTrustChain on Twitter
with open("filteredLNTrustChain.txt", 'r') as f: 
    data = ast.literal_eval(f.read())


newdata = []
for i, line in enumerate(data):
    print(f"Processing {i} of {len(data)}...")
    line.append(decodepayreq(line[1])["Signed with public key"].decode('utf-8'))
    newdata.append(line)

with open('withNodes.txt', 'w') as w:
    print("\nWriting...")
    w.write(str(newdata))
    print("Done.")

with open('withNodes.csv', 'w') as w:
    print("\nWriting...")
    for item in newdata:
        w.write(f"{item[0]}, {item[1]}, {item[2]}\n")
    print("Done.")