default: build
build: ${LIBOUT}
rebuild: clean build
build: ex1.elf blink.elf
CFLAGS=-DF_CPU=16000000L  -mmcu=atmega328
LIBS=-L./lib -I./include -larduino

ex1.elf: ex1.o main.o
	avr-g++ $(CFLAGS) -o ex1.elf ex1.o main.o $(LIBS)

main.o: main.c
	avr-g++ $(CFLAGS) -c main.c $(LIBS)

ex1.o: ex1.c
	avr-g++ $(CFLAGS) -c ex1.c $(LIBS)

blink.o: blink.c
	avr-g++ $(CFLAGS) -c blink.c $(LIBS)

blink.elf: blink.o
	avr-g++ $(CFLAGS) -o blink.elf blink.o $(LIBS)

clean:
	rm -f *.o core a.out errs *.a
