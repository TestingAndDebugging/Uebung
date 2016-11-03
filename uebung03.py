#!/usr/bin/env python3
###############################################################################
## vim: et ai ts=4
##
## Bitte erst ab der Stelle im Code, die mit 'Hier beginnt Ihr Code' markiert
## ist, eigenen Code einfuegen.

###############################################################################

Aufgabe = 3                    # Diesen Eintrag nicht veraendern,
                               # anderenfalls wird die Aufgabe nicht gewertet!!

Studenten = []                 # Initalisierung der Studentenliste

###############################################################################
## Bitte tragen Sie in die folgenden Variablen Ihre Gruppennummer und die
## Mitglieder Ihrer Gruppe ein. Bitte verwenden Sie KEINE Umlaute!

Gruppennummer = 0
# Syntax fuer die Angabe der Namen und Matrikelnummern der einzelen
# Gruppenmitglieder:
#
# Studenten.append({'matnr':12345, 'nachname':"NACHNAME1", 'vorname':"VORNAME1"})
# Studenten.append({'matnr':12346, 'nachname':"NACHNAME2", 'vorname':"VORNAME2"})
# Studenten.append({'matnr':12347, 'nachname':"NACHNAME3", 'vorname':"VORNAME3"})
# Studenten.append({'matnr':12348, 'nachname':"NACHNAME4", 'vorname':"VORNAME4"})
# Studenten.append({'matnr':12349, 'nachname':"NACHNAME5", 'vorname':"VORNAME5"})

###############################################################################
## Code fuer Aufgabe


## add8 ist ein 8bit voll Addierer mit Uebertrag. 
##
## Die Werte a0-a7, b0-b7 und c0 koennen den Wert True oder False haben.
## (Testen auf andere Eingaben ist nicht noetig!)
## a0-a7 stellen die Binaerschreibweise der Zahl a dar.
## b0-b7 stellen die Binaerschreibweise der Zahl b dar.
## c0 ist der Uebertrag von einem etwaig vorangestellten Addierer.
##
## Ausgegeben wird die Summe der Zahlen a und b in Binaerform.
## C8 ist dabei das Uebertragsbit, falls die Summe den Darstellungsbereich
## von 8 Bit Zahlen ueberschreitet.
def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    s0 = False
    if (a0 != b0) != c0:
        s0 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    s1 = False
    if (a1 != b1) != c1:
        s1 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s2 = False
    if (a2 != b2) != c2:
        s2 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True
    s3 = False
    if (a3 != b3) != c3:
        s3 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True
    s4 = False
    if (a4 != b4) != c4:
        s4 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True
    s5 = False
    if (a5 != b5) != c5:
        s5 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True
    s6 = False
    if (a6 != b6) != c6:
        s6 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True
    s7 = False
    if (a7 != b7) != c7:
        s7 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True
    return (s0,s1,s2,s3,s4,s5,s6,s7,c8)


## split wandelt eine Integer Zahl in eine 8-Bit Binaerzahl um.
## (Testen auf andere Eingaben ist nicht noetig!)
def split(n):
    return(n&0x1 == 0x1,
           n&0x2 == 0x2,
           n&0x4 == 0x4,
           n&0x8 == 0x8,
           n&0x10 == 0x10,
           n&0x20 == 0x20,
           n&0x40 == 0x40,
           n&0x80 == 0x80)


## glue wandelt eine 8-Bit Binaerzahl mit etwaigem Uebertrag in eine
## Dezimalzahl um. b0-b7 und c koennen True oder False sein.
## (Testen auf andere Eingaben ist nicht noetig!)
def glue(b0, b1, b2, b3, b4, b5, b6, b7, c):
    t = 0
    if b0:
        t += 1
    if b1:
        t += 2
    if b2:
        t += 4
    if b3:
        t += 8
    if b4:
        t += 16
    if b5:
        t += 32
    if b6:
        t += 64
    if b7:
        t += 128
    if c:
        t += 256
    return t

###############################################################################
## Hier beginnt Ihr Code
def addInt(x,y):##ints in binaer teilen, addieren und wieder zusammensetzen
  (a0, a1, a2, a3, a4, a5, a6, a7) = split(a)
  (b0, b1, b2, b3, b4, b5, b6, b7) = split(b)
  (s0, s1, s2, s3, s4, s5, s6, s7, c0) = add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,false)
  return glue(s0, s1, s2, s3, s4, s5, s6, s7, c0)
  
def testFullBranchCoverage_1():
    for i in range(256):
      for j in range(256):
        result = addInt(i,j)
          print str(i) + " + " + str(j) + " = " + str(result)
          assert ressult == (i+j)


def testFullBranchCoverage_2():
    x=inputX
    y=inputY
    
    ##  die idee ists hier den branch großflächig zu überdecken, was ist wenn x = 0 ist und dann was ist wenn y = 0 ist
    if x==0:
        y+=1
    if y==0:
        x+=1
    ##  in progress

###############################################################################
## Bitte erst innerhalb des folgenden if Blocks Funktionen aufrufen.
## Werden ausserhalb dieses Blocks Funktionen aufgerufen, so wird die Aufgabe
## nicht gewertet.

if __name__ == '__main__':

    ## Der folgende Funktionsaufruf prueft die Eintraege der Variablen
    ## Studenten, Gruppennummer und Aufgabe und gibt die Werte tabelarisch
    ## auf dem Bildschirm aus oder loest einen Fehler aus, falls die Form
    ## der Eintraege nicht korrekt ist.
    from Grading.Grading import * # pragma no cover
    Grading.CheckStudents(Studenten, Gruppennummer, Aufgabe) # pragma no cover

    ## Aufruf der Testfunktion
    testFullBranchCoverage_1()
    testFullBranchCoverage_2()
