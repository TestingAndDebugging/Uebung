/*
vim: et ai ts=4

###############################################################################

## Bitte erst ab der Stelle im Code, die mit 'Hier beginnt Ihr Code' markiert
## ist, eigenen Code einfuegen.

###############################################################################

Aufgabe = 2                    # Diesen Eintrag nicht veraendern,
                               # anderenfalls wird die Aufgabe nicht gewertet!!

Studenten = []                 # Initalisierung der Studentenliste

###############################################################################
## Bitte tragen Sie in die folgenden Variablen Ihre Gruppennummer und die
## Mitglieder Ihrer Gruppe ein. Bitte verwenden Sie KEINE Umlaute!

Gruppennummer = 11
# Syntax fuer die Angabe der Namen und Matrikelnummern der einzelen
# Gruppenmitglieder:
#
Studenten.append({'matnr':51829, 'nachname':"Gillitzer", 'vorname':"Philipp"})
Studenten.append({'matnr':57168, 'nachname':"Schmid", 'vorname':"Nils"})
Studenten.append({'matnr':49143, 'nachname':"Krawtschuk", 'vorname':"Maxim"})
# Studenten.append({'matnr':12346, 'nachname':"NACHNAME2", 'vorname':"VORNAME2"})
# Studenten.append({'matnr':12347, 'nachname':"NACHNAME3", 'vorname':"VORNAME3"})
# Studenten.append({'matnr':12348, 'nachname':"NACHNAME4", 'vorname':"VORNAME4"})
# Studenten.append({'matnr':12349, 'nachname':"NACHNAME5", 'vorname':"VORNAME5"})

*/

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#define BUF_SIZE 32767

/* Mit Hilfe des gcc Schalters '-Wl,--wrap=symbol' kann man gcc dazu auffordern
 * statt der vorgegeben Funktion 'symbol' die Funktion '__wrap_symbol'
 * aufzurufen.  Die originale Funktion 'symbol' kann dann innerhalb der
 * '__wrap_symbol' Funktion mit '__real_symbol' aufgerufen werden.
 *
 * Im untenstehenden Code wird fuer die Funktion 'read' ein solcher Wrapper
 * definiert. Mit Hilfe diese Wrappers kann das gewuenschte Sonderverhalten der
 * Funktion (hier das nicht vollständige lesen) simuliert werden.
 *
 * Der Prototyp fuer '__real_read' wird benoetigt, damit beim Compilieren kein
 * impliziter Deklarationsfehler angezeigt wird. Der Zusatz
 * '__attribute__((weak))' sorgt dafür, dass beim Compilieren ohne den Schalter
 * '-Wl,--wrap=read' kein Link Fehler (undefined referenz) erzeugt wird.
 */

ssize_t __real_read(int fd, void *buf, size_t count) __attribute__((weak));

ssize_t __wrap_read(int fd, void *buf, size_t count) {
    int faulty_count;
    int ret;

    /* faulty_count is between 1 and count (incusive) */
    faulty_count = (rand() % count) + 1;

    ret = __real_read(fd, buf, faulty_count);

    fprintf(stderr, "%d\n", ret);

    return ret;
}

ssize_t read_all(int fd, void *buf, size_t count) {
    /* Hier beginnt Ihr Code */

    /* Benutzen Sie hier die 'read' Funktion wie gewohnt.
     * Sie koennen dann beim Compilieren mit dem Schalter '-Wl,--wrap=read'
     * steuern ob die Funktion 'read' (ohne Schalter) oder '__wrap_read' (mit
     * Schalter) verwendet werden soll ohne dabei den Quellcode fuer die
     * Funktion 'read_all' zu veraendern.
     */
	 
	 void * read_buffer = buf;
	 size_t mand_count = count;
	 ssize_t bytes_read;
	 
	 do {
		 bytes_read = read(fd,read_buffer,mand_count);
		 if (bytes_read == -1) {
			 return -1;
		 }
		 read_buffer += bytes_read;
		 mand_count -= bytes_read;
	} while ( bytes_read > 0 && mand_count > 0);
	return read_buffer - buf;		 	 
	

}

int main(int argc, char* argv[]) {
    int n;
    int fd;
    int r_success;
    char buffer[BUF_SIZE];

    /* initiate buffer with BUF_SIZE times '\0' */
    memset(&buffer, '\0', BUF_SIZE);

    if (argc != 3) { /* ./uebung02 <file> <count> */
        exit(1);
    }

    fd = open(argv[1], O_RDONLY);

    if (fd == -1) { /* Some error occured */
        perror("Error from open.");
        exit(1);
    }

    /* Number of bytes to read. Read no more than BUF_SIZE - 1 bytes */
    n = atoi(argv[2]) % BUF_SIZE;

    r_success = read_all(fd, &buffer, n);
    if (r_success == -1) {
        perror("Error from read.");
        exit(1);
    }

    printf("%s\n", buffer);
	printf("Size: %d\n", r_success);
    return 0;
}
