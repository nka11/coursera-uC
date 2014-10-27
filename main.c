#include <Arduino.h>


#include "main.h"

int main() {
  init();
  setup();
  for(;;) {
    loop();
  }
}
