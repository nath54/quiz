#coding:utf-8
import random,os
dire='datasquiz/'
cac,cacc="#","|"
extf=".nathq"
ext='.nathq'
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
    for ff in f:
        g=ff.split(cac)
        if len(g)>=1:
            voc.append(g)
    return voc

def espace(nb):
    for x in range(nb): print(" ")

def b(voc):
    lstc=[0,1]
    print("modes disponibles :")
    print(" -1:chances aléatoires d'êtres interrogés sur la question normalement ou l'inverse(par défaut)")
    print(" -2:n'interroge que sur les questions normalement")
    print(" -3:n'interroge que sur l'inverse des questions")
    md=inp("mode : ")
    if md=='1': lstc=[0,1]
    elif md=='3': lstc=[0]
    else: lstc=[1]
    nb=random.randint(7,20)
    pts=0
    for x in range(nb):
      espace(20)
      print("----------------------------------")
      vv=random.choice(voc)
      if len(vv)==2:
        if random.choice(lstc): v=[vv[0],vv[1]]
        else: v=[vv[1],vv[0]]
        print("question n°"+str(x+1)+"/"+str(nb))      
        if x!=0:print("points : "+str(pts)+"/"+str(x)+"  score actuel : "+str(float(pts)/float(x)*100.0)[:5]+" %")
        print(" ")
        print("q : "+str(v[0]))
        print("\nréponse : ")
        tt=">>>"
        r=inp(tt)
        if r==v[1]:
            print(" ")
            print("Vous avez juste !")
            pts+=1
        else:
            print("Dommage, vous avez faux !")
            print("La bonne réponse était : "+v[1])
        print(" ")
        print("----------------------------------")
        inp("suivant")
    espace(20)
    print("SCORE FINAL : ")
    print(" ")
    print("Points : "+str(pts)+"/"+str(nb))
    print("Vous avez "+str(float(pts)/float(nb)*100.0)[:5]+" % de réponses justes")
    print(" ")
    inp("fin")
    print("Voulez vous refaire ce quiz ?")
    print("  1-oui")
    print("  2-non")
    r=inp(" : ")
    if r=="1" : b(voc)

def c(fich):
    m1=inp("question : ")
    m2=inp("reponse : ")
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
        aa=inp(">>> ")

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
