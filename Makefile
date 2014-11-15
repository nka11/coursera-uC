default: build
build: ${LIBOUT}
rebuild: clean build
build: all

PORT = usb
UPLOAD_RATE = 250
ARDUI_PROGRAMMER = stk500v1
DRAGON_PROGRAMMER = dragon_isp
MCU = atmega328p
F_CPU = 16000000

CFLAGS=-DF_CPU=16000000L  -mmcu=atmega328
LIBS=-L./lib -I./include -larduino
AVRDUDE=/usr/bin/avrdude

AVR_OPTS=-p m328 -P $(PORT) -B$(UPLOAD_RATE)

all: lib

%.hex: %.elf
	avr-objcopy -j .text -j .data -O ihex $< $@

%.elf: %.o main.o
	avr-g++ $(CFLAGS) -o $@ $< main.o $(LIBS)

%.o: %.c lib
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
	rm -f *.o core a.out errs *.a *.hex
	cd  src-ard && $(MAKE) clean

arduiload:
	$(AVRDUDE) -c $(ARDUI_PROGRAMMER) $(AVR_OPTS) -u -U flash:w:ex1.hex

dragonload:
	$(AVRDUDE) -c $(DRAGON_PROGRAMMER) $(AVR_OPTS) -u -U flash:w:ex1.hex

dragonfuses:
	$(AVRDUDE) -c $(DRAGON_PROGRAMMER) $(AVR_OPTS) -u -U lfuse:w:0xff:m -U hfuse:w:0xDA:m

dragonloads2ex1: s2ex1.hex
	$(AVRDUDE) -c $(DRAGON_PROGRAMMER) $(AVR_OPTS) -u -U flash:w:s2ex1.hex:i
	
dragonloads2ex2: s2ex2.hex
	$(AVRDUDE) -c $(DRAGON_PROGRAMMER) $(AVR_OPTS) -u -U flash:w:s2ex2.hex:i

dragonloads3ex1: s3ex1.hex
	$(AVRDUDE) -c $(DRAGON_PROGRAMMER) $(AVR_OPTS) -u -U flash:w:s3ex1.hex:i

dragonloads3ex2: s3ex2.hex
	$(AVRDUDE) -c $(DRAGON_PROGRAMMER) $(AVR_OPTS) -u -U flash:w:s3ex2.hex:i