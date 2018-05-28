# -*- coding: utf-8 -*-
from random import randint
import math
import re
import nltk

def afficherLesTas(tas):
    i=0
    while (i<len(tas)):
        print(i+1,'| ',tas[i]*'*',(23-tas[i])*' ','|',tas[i])
        i+=1

def score(nb):
    i=1
    s=0
    while (i<=nb):
        s+=i*pow(10,i)        
        i+=1
    return s
    
def jeuDeNim():

    f = open('./score.txt')
       
    ij1=-1
    ij2=-1
    nbc1=0
    nbc2=0
    joueurs = []
    tas = []
    scores=[]
    
    for l in f:
        l=(l.split(','))
        joueurs.append([l[0],int(l[1]),int(l[2])])
    f.close()
    
    m = input("tappez j pour jouer : \n")
    
    while (m!='j' and m!='J' ):
        m = input("tappez j pour jouer : \n")
        
    print('\nVous pouvez commencer !\n')
    print('Veuillez insérez vos noms')
    
    j1 = input("Joueur 1 : ")
    
    k=0
    for e in joueurs:
        if (j1==e[0]):
            ij1=k
        k+=1
        
    if (ij1==-1):
        joueurs.append([j1.lower(),0,0])
        ij1=k
    
    j2 = input("Joueur 2 : ")
    while (j1.lower()==j2.lower() ):
        j2 = input("Les deux joueurs ne peuvent avoir le même nom !\n veuill insérez un autre nom: \n")
    
    k=0
    for e in joueurs:
        if (j2==e[0]):
            ij2=k
        k+=1
        
    if (ij2==-1):
        joueurs.append([j2.lower(),0,0])
        ij2=k
        
    print('\nNombre de tas !')
    print('... ... ...')
    
    a = randint(3,7)
    print(a)
    
    print('... ... ...')
    print('affichage des tas !')
    i=0
    while (i<a):
        tas.append(randint(5,23))
        i+=1
    
    afficherLesTas(tas)
    
    while (tas.count(0)==0):
        print('joueur 1 : ',joueurs[ij1][0])
        t1=input('indiquer le tas et le nombre de pierres à retirer : ')
        while (not(re.match(r"^[1-7]-[1-9][0-9]{0,1}\b",t1))):
            print('vous devez respecter la forme : ')
            print('"Numéro du tas - Nombre de pierres"')
            t1=input('indiquer le tas et le nombre de pierres à retirer : ')
        
        t1=t1.split('-')    
        t1[0]=int(t1[0])
        t1[1]=int(t1[1])                
        
        while(tas[t1[0]-1]-t1[1]<1 and tas[t1[0]-1]!=1):
            t1=input('pas assez de pierre dans ce tas!\nveuillez changer la valeur entrée : \n')                        
            t1=t1.split('-')
            t1[0]=int(t1[0])
            t1[1]=int(t1[1])        
            
        if (tas[t1[0]-1]==1):
            joueurs[ij2][1]=score(nbc2)
            joueurs[ij1][1]=0
            print('fin du jeu !')
            print(joueurs[ij2][0],' a gagner.')
            print('son score est de : ',score(nbc2),' !')
            
            if (joueurs[ij2][2]==0):
                joueurs[ij2][2]=score(nbc2)
                print('bravo c\'est votre meilleur score !')
                break
            
            if (nbc2<int(joueurs[ij2][2])):
                joueurs[ij2][2]=score(nbc2)
                print('bravo c\'est votre meilleur score !')
                break
        
            
        nbc1+=1
        tas[t1[0]-1]-=t1[1]    
        
        print('\nétat du tas : \n')
        afficherLesTas(tas)
        
        print('joueur 2 : ',joueurs[ij2][0])        
        t1=input('indiquer le tas et le nombre de pierres à retirer : ')
        while (not(re.match(r"^[1-7]-[1-9][0-9]{0,1}\b",t1))):
            print('vous devez respecter la forme : ')
            print('"Numéro du tas - Nombre de pierres"')
            t1=input('indiquer le tas et le nombre de pierres à retirer : ')
        
        t1=t1.split('-')                          
        t1[0]=int(t1[0])
        t1[1]=int(t1[1])    
            
        while(tas[t1[0]-1]-t1[1]<1 and tas[t1[0]-1]!=1):
            t1=input('pas assez de pierre dans ce tas!\nveuillez changer la valeur entrée : \n')                        
            t1=t1.split('-')
            t1[0]=int(t1[0])
            t1[1]=int(t1[1])            
    
        if (tas[t1[0]-1]==1):
            joueurs[ij1][1]=score(nbc1)
            joueurs[ij2][1]=0
            print('fin du jeu !')
            print(joueurs[ij1][0],' a gagné.')
            print('son score est de : ',score(nbc1),' !')
            if (joueurs[ij1][2]==0):
                joueurs[ij1][2]=score(nbc1)
                print('bravo c\'est votre meilleur score !')
                break
            
            if (nbc1<int(joueurs[ij1][2])):
                joueurs[ij1][2]=score(nbc1)
                print('bravo c\'est votre meilleur score !')
                break      
            
        
        nbc2+=1
        tas[t1[0]-1]-=t1[1]
        
        print('\nétat du tas : \n')
        afficherLesTas(tas)
    
    for j in joueurs:
        if (int(j[2])!=0):
            scores.append(int(j[2]))
    
    print(len(scores))
    print(len(joueurs))
    
    scores.sort()
    
    print("les meilleur scores : ")
    print("========================")
    
    v=0
    while (v<len(scores)):
        for j in joueurs:
            if (j[2]==scores[v]):
                print(v+1,'-',j[0],' ......... ',j[2])
                v+=1
            if (v>=len(scores)):
                break

    f = open('./score.txt','w')    
    for j in joueurs:
        f.write(str(j[0])+','+str(j[1])+','+str(j[2])+'\n')
    f.close()

print('\nJeu de Nim')
print('===========')
jeuDeNim()
r=input('entrez 1 si vous voulez  rejouez : \n')
while(r=='1'):
    jeuDeNim()
    r=input('entrez 1 si vous voulez  rejouez : \n')
print('\nFin du jeu ! à la prochaine fois')