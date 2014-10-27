

OBJECTS =  WInterrupts.o wiring_analog.o wiring.o wiring_shift.o wiring_pulse.o wiring_digital.o  WString.o IPAddress.o HID.o WMath.o CDC.o HardwareSerial.o Stream.o main.o new.o USBCore.o Tone.o Print.o

all: libarduino.a

libarduino.a: $(OBJECTS)
	avr-ar crs libarduino.a $(OBJECTS)
	cp libarduino.a ../lib
	cp *.h ../include


%.o: %.cpp
	avr-g++ -Os -Wl,--gc-sections -ffunction-sections  -fdata-sections -I../include -I./ -mmcu=atmega328p -DF_CPU=16000000UL -c $<

%.o: %.c
	avr-gcc -Os -Wl,--gc-sections -ffunction-sections  -fdata-sections -I./ -mmcu=atmega328p -DF_CPU=16000000UL -c $<
clean:
	rm -f *.o
