default: build
build: ${LIBOUT}
rebuild: clean build
build: all
CFLAGS=-DF_CPU=16000000L  -mmcu=atmega328
LIBS=-L./lib -I./include -larduino

all: lib ex1.hex

%.hex: %.elf
	avr-objcopy -j .text -j .data -O ihex $< $@

ex1.elf: ex1.o main.o
	avr-g++ $(CFLAGS) -o $@ $< main.o $(LIBS)

%.o: %.c
	avr-g++ $(CFLAGS) -c $< $(LIBS)

%.c: %.ino
	echo "#include <Arduino.h>" > $@
	cat $< >> $@

.PHONY : clean lib
lib:
	mkdir -p lib
	mkdir -p include
	cd src-ard && $(MAKE)

clean:
	rm -Rf lib
	rm -Rf include
	rm -f *.o core a.out errs *.a
	cd  src-ard && $(MAKE) clean
