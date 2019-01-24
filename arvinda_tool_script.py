from lightning_address import decode as decodepayreq

pay_req = 'lnbc8800u1pwysh8kpp5kln5lcht4la2aqg899qj4gyfnglfs3wg83wmjzlh7ak682t4suvqdqqcqzys26g2z8dtjzk3vl8eh22rq32kn7lvgrl554ggmma7mwr9e5wzgjfjk8rv0md493e8ua944pchq2supmglcpt6nk5cxs5ycsmplwgkawsqk2w5pa'

public_key = decodepayreq(pay_req)["Signed with public key"].decode('utf-8')

print(public_key)