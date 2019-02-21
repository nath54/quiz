#coding:utf-8
import random,os
dire='datasquiz/'
cac,cacc="#","|"
extf=".nathq"

fichs=[]

def inp(txt):
    import sys
    vp=sys.version_info
    if vp[0]==2: return raw_input(txt)
    else: return input(txt)

def begin():
    if not dire[:-1] in os.listdir("./"): os.mkdir(dire)
    for oo in os.listdir(dire): fichs.append( dire+oo )

def a(fich):
    voc=[]
    f=open(fich,'r').read().split(cacc)
    print(f)
    for ff in f:
        g=ff.split(cac)
        if len(g)>=1:
            voc.append(g)
    return voc

def b(voc):
    nb=random.randint(3,15)
    pts=0
    for x in range(nb):
      vv=random.choice(voc)
      if len(vv)==2:
        if random.randint(0,1): v=[vv[0],vv[1]]
        else: v=[vv[1],vv[0]]        
        tt=v[0]+"\n : "
        r=inp(tt)
        if r==v[1]:
            print("juste!")
            pts+=1
        else:
            print("faux!,c'était : "+v[1])
    print(str(pts)+"/"+str(nb)+" : "+str(float(pts)/float(nb)*100.0)[:5]+" %")

def c(fich):
    m1=inp("expression : ")
    m2=inp("traduction : ")
    txt=cacc+m1+cac+m2
    f=open(fich,"a")
    f.write(txt)
    f.close()

def d():
    aa=''
    h=inp("Voulez vous créer un nouveau fichier(1) ou en éditer un déjà existant(2)?\n : ")
    if h=='1':
        nf=dire+inp("nom du fichier : ")+ext
    else:
        ff=os.listdir(dire)
        for f in ff:
            print(str(ff.index(f))+" - "+f)
        r=inp("Quel fichier voulez vous éditer ?\n : ")
        try:
            r=int(r)
            nf=dire+ff[r]
        except:
            nf=dire+ff[0]
    while aa!='q':
        c(nf)
        aa=raw_input(">>> ")

def main():
  begin()
  quit=False
  while not quit:
    ch=inp("###MENU###\nQue voulez vous faire ?\n 1=créer/éditer un quiz\n 2=lancer un quiz\n q=quitter \n : ")
    if ch == '1': d()
    if ch == '2':
        ff=os.listdir(dire)
        if ff != []:
            for f in ff:
                print(str(ff.index(f))+" : "+f)
            nbq=inp("Quel quiz voulez vous lancer ?\n : ")
            try:
                nbq=int(nbq)
                nf=dire+ff[nbq]
            except:
                print("Vous n'avez pas rentré un nombre correct, le quiz n°0 va donc se lancer par défaut")
                nf=dire+ff[0]
            b(a(nf))
        else: print("Il n'y a pas de quiz disponibles, veuillez en créer un.")
    if ch == 'q': quit=True 
main()
