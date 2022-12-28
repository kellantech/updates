import requests,urllib.parse

url = "https://UntidySecretAssembly.kellanb.repl.co"
v = input("version? ").replace(".","_")
fn = input("file? ")

with open(fn,"r")as fil:
  va = fil.read()

  
requests.get(f"{url}/add_?name=v{urllib.parse.quote(v,safe='')}&val={urllib.parse.quote(va,safe='')}")
