#include<UserButton.h>

module UserButtonTestC {
	uses {
		interface Boot;
		interface Leds;
	}
	
	
	uses {	
		//User Button
		interface Get<button_state_t>;
		interface Notify<button_state_t>;
	}
}

implementation {

	event void Boot.booted(){
		call Notify.enable();
	}

	event void Notify.notify(button_state_t val){
		if(val == BUTTON_PRESSED){
			//Button ON
			call Leds.led0On();
		}else if (val == BUTTON_RELEASED){
			//Button OFF
			call Leds.led0Off();
		}
	}
}