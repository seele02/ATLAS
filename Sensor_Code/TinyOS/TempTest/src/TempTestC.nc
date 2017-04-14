#include <Timer.h>
#include <stdio.h>
#include <string.h>

module TempTestC{
	uses{
		
		//General Interfaces
		interface Boot;
		interface Timer<TMilli>;
		interface Leds;
		
		//Read
		interface Read<uint16_t> as TempRead;
		
		//Wireless Imports
		interface SplitControl as RadioControl;
		interface AMSend;
		interface Receive;
		interface Packet;
		
	}
}


implementation{
	uint16_t centigrade;

	event void Boot.booted(){
		call Timer.startPeriodic(1000);
		call Leds.led1On();
		
	}

	event void Timer.fired(){
		
		if(call TempRead.read() == SUCCESS){
			call Leds.led2Toggle();
		}
		else{
			call Leds.led0Toggle();
		}
	}

	event void TempRead.readDone(error_t result, uint16_t val){
		centigrade = (-39.6 + 0.01 * val);
		
		if(result == SUCCESS){
			//Read from the Sensor Now
			printf("Current Temp is: %d \r\n", centigrade);
			
		}else{
			printf("Error reading Temp \r\n");
		}
	}
}