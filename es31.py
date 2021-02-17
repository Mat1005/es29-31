Nord = int(input("Inserire il fatturato in euro del nord."))
Centro = int(input("Inserire il fatturato del centro in euro."))
Sud = int(input("Inserire in euro il fatturato del sud."))
Isole = int(input("Inserire il fatturato in euro delle isole."))
fatturato = {'Nord':Nord,
'Centro': Centro,
'Sud ': Sud,
'Isole':Isole}
tot = Nord + Centro + Sud + Isole 
per_Nord = Nord/tot*100
per_Centro = Centro/tot*100
per_Sud = Sud/tot*100
per_Isole = Isole/tot*100

fatturato_per = {'Nord':per_Nord,
'Centro': per_Centro,
'Sud ': per_Sud,
'Isole':per_Isole}
print("Il fatturato totale è di ",tot," euro.")
print("Il fatturato è diviso in questo modo")
print(fatturato)
print("Ed è diviso percentualmente in questo modo")
print(fatturato_per)