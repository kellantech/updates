import requests,os

fn = "main.py"
url = ''


def save(v):
  with open("version.txt","w") as vf:
    vf.write(str(v))
def load():
  with open("version.txt","r") as vf2:
    return int(vf2.read())

cnew = load()
    

newv = requests.get(f"{url}/newest").text
if int(newv[1:]) > cnew:
  print("downloading update...",end="")
  os.system(f'curl -O -s {url}/{newv}')
  print("done")
  os.system(f"cat {newv}>{fn}")
  os.system(f"rm {newv}")
  save(int(newv[1:]))

else: 
  print("you are up to date!")
