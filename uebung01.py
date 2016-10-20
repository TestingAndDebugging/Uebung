#!/usr/bin/env python3
###############################################################################
## vim: et ai ts=4
##
## Bitte erst ab der Stelle im Code, die mit 'Hier beginnt Ihr Code' markiert
## ist, eigenen Code einfuegen.
###############################################################################

Aufgabe = 1                    # Diesen Eintrag nicht veraendern,
                               # anderenfalls wird die Aufgabe nicht gewertet!!

Studenten = []                 # Initalisierung der Studentenliste

###############################################################################
## Bitte tragen Sie in die folgenden Variablen Ihre Gruppennummer und die
## Mitglieder Ihrer Gruppe ein. Bitte verwenden Sie KEINE Umlaute!

Gruppennummer = 5
# Syntax fuer die Angabe der Namen und Matrikelnummern der einzelen
# Gruppenmitglieder:
#
Studenten.append({'matnr':51754, 'nachname':"Gillitzer", 'vorname':"Philipp"})
Studenten.append({'matnr':55555, 'nachname':"asdasd", 'vorname':"asdasd"})
# Studenten.append({'matnr':12347, 'nachname':"NACHNAME3", 'vorname':"VORNAME3"})
# Studenten.append({'matnr':12348, 'nachname':"NACHNAME4", 'vorname':"VORNAME4"})
# Studenten.append({'matnr':12349, 'nachname':"NACHNAME5", 'vorname':"VORNAME5"})

###############################################################################
## Laden der Blackboximplementierung der MyQueue Klasse

from MyQueue import *

## SPEZIFIKATION:
##
## Die MyQueue Klasse stellt eine FIFO Warteschlange mit fester Laenge
## fuer Integes bereit.
##
## Der Konstruktor hat eine Parameter: ein Integer > 0 der die maximale
## Anzahl von Elementen angibt, die die Warteschlange speichern kann.
##
## empty() gibt genau dann True zurueck, wenn die Warteschlange keine
## Elemnte enthaelt.
##
## full() gibt genau dann True zurueck, wenn die Warteschlange kein
## weiters Element speichen kann
##
## enqueue(i) versucht den Integerwert i in der Warteschlange abzulegen.
## Die Funktion gibt True zurueck, falls dieser Versuch erfolgreich war
## und False wenn die Warteschlange voll ist.
##
## dequeue() entfernt (nach dem FIFO Prinzip) eine Wert aus der
## Warteschlange und gibt diesen zurueck. Ist die Warteschlange leer,
## so wird None zuruek gegeben.
##
## Beispiel:
## q = MyQueue(1)
## is_empty = q.empty()
## succeeded = q.enqueue(10)
## is_full = q.full()
## value = q.dequeue()
##
## Diese Folge von Befehlen sollte folgendes leisten
## 1. Sollte eine Warteschlange q erzeugen, die ein Element speichern kann.
## 2. Sollte pruefen, ob q leer ist. (Erwarte True als Rueckgabewert)
## 3. Sollte versuchen die Zahl 10 in Warteschlange einzutragen. (Erwarte
##    True als Rueckgabewert)
## 4. Sollte testen, ob die Warteschlange voll ist. (Erwarte True als
##    Rueckgabewert)
## 5. Sollte versuchen ein Element aus der Warteschlange zurueckzugeben.
##    (Erwarte 10 als Rueckgabewert)


###############################################################################
## Hier beginnt Ihr Code
def testQueue():

	q = MyQueue(1)
	
	# Initalisierungs Checks
	assert q.max == 1, "Maximale Größe passt nicht"
	
	assert q.size == 0, "Aktuelle Größe passt nicht"
	
	is_empty = q.empty()
	assert is_empty, "Nach Initalisierung sollte die Schlange noch leer sein"
	
	
	is_full = q.full()
	assert is_full == False, "Schlange ist nach Initalisierung nicht voll"
	assert q.size == 0, "Größe passt nicht"
		
	
	
	succeeded = q.enqueue(1)
	assert succeeded, "Erfolgreich eingefügt"
	check(q)	
	
	is_full = q.full();
	assert is_full, "Schlange ist voll"	
	
	value = q.dequeue()
	assert value == 1, "Wert sollte 1 sein"
	check(q)	
	
	is_empty = q.empty()
	assert q.empty(), "Schlange ist wieder leer"
	check(q)	
	
	
	succeeded = q.enqueue(-42)
	assert succeeded, "Erfolgreich eingefügt"
	check(q)		
	
	value = q.dequeue()
	assert value == -42, "Wert sollte 1 sein"
	check(q)	
		
	value = q.dequeue()
	assert value == None, "Schlange war schon leer"
	check(q)	
	
	
	is_empty = q.empty()
	assert q.empty(), "Schlange ist wieder leer"
	check(q)
	
	succeeded = q.enqueue(1)
	assert succeeded, "Erfolgreich eingefügt"
	succeeded = q.enqueue(2)
	assert succeeded == False, "Konnte Elelement nicht einfügen"
	check(q)
	
	value = q.dequeue()
	assert value == 1, "Hätte nicht überschreiben dürfen"
	check(q)
	
	is_empty = q.empty()
	assert is_empty, "Sollte wieder leer sein"
	
	succeeded = q.enqueue(2**31-1)
	assert succeeded, "Einfügen geklappt"
	value = q.dequeue()	
	assert value == (2**31-1), "Zu große Zahl"
	
	
	q = MyQueue(3000)
		
	for x in range(2000):
		#print(x)
		value = x
		succeeded = q.enqueue(value)
		assert succeeded, "Einfügen muss klappen"
		assert not q.empty(), "Darf nicht leer sein"
		assert not q.full(), "Darf nicht voll sein"
		check(q)
		
	print()
		
	for x in range(2000):
		value = q.dequeue()
		#print(value)
		iter = x
		assert ( iter == value ), "Wert passt nicht"
		assert not q.full(), "Darf nicht voll sein"
		check(q)
		
	for x in range(2000):
		#print(x)
		value = x *-1
		succeeded = q.enqueue(value)
		assert succeeded, "Einfügen muss klappen"
		assert not q.empty(), "Darf nicht leer sein"
		assert not q.full(), "Darf nicht voll sein"
		check(q)
		
	print()
		
	for x in range(2000):
		value = q.dequeue()
		#print(value)
		iter = x * -1
		assert ( iter == value ), "Wert passt nicht"
		assert not q.full(), "Darf nicht voll sein"
		check(q)
		
		
		
		
		
		
	
def check(q):
	
	#assert q.tail == 0, "tail-Zeiger passt nicht"
	#assert q.head == 0, "head-Zeiger passt nicht"
	assert q.size >= 0 and q.size <= q.max, "Inkonsistente Queue"
	
	if q.tail > q.head:
		assert (q.tail - q.head) == q.size, "Inkonsistente Queue"
	
	if q.tail < q.head:
		assert ( q.head -q.tail) == (q.max -q.size), "Inkonsistente Queue"
	
	if q.tail == q.head:
		assert (q.size == 0) or (q.size == q.max), "Inkonsistente Queue"
		


	
	
	
###############################################################################
## Bitte erst innerhalb des folgenden if Blocks Funktionen aufrufen.
## Werden ausserhalb dieses Blocks Funktionen aufgerufen, so wird die Aufgabe
## nicht gewertet.

if __name__ == '__main__':

    ## Der folgende Funktionsaufruf prueft die Eintraege der Variablen
    ## Studenten, Gruppennummer und Aufgabe und gibt die Werte tabelarisch
    ## auf dem Bildschirm aus oder loest einen Fehler aus, falls die Form
    ## der Eintraege nicht korrekt ist.
    from Grading.Grading import Grading
    Grading.CheckStudents(Studenten, Gruppennummer, Aufgabe)

    ## Aufruf der Testfunktion
    testQueue()
