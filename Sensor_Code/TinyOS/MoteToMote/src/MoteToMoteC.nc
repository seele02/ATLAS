#include<UserButton.h>
#include"MoteToMote.h"
#include <stdio.h>
#include <string.h>

module MoteToMoteC {
	uses {
		interface Boot;
		interface Leds;
	}

	uses {
		//User Button
		interface Get<button_state_t>;
		interface Notify<button_state_t>;
	}

	uses {
		//Radio
		interface Packet;
		interface AMPacket;
		interface AMSend;
		interface SplitControl as AMControl;
		interface Receive;
	}
	
	uses{
		//Read
		interface Read<uint16_t> as TempRead;
	}
}

implementation {
	uint16_t centigrade;
	bool _radioBusy = FALSE;
	message_t _packet;
	//message_t _mypacket;

	event void Boot.booted() {
		call Timer.startPeriodic(1000);
		call Notify.enable();
		call AMControl.start();
	}

	event void Notify.notify(button_state_t val) {

		if(_radioBusy == FALSE) {

			//Create the packet
			MoteToMoteMsg_t * msg = call Packet.getPayload(& _packet, sizeof(MoteToMoteMsg_t));
			msg->NodeId = TOS_NODE_ID;
			msg->Data = (uint8_t) val; //Add validation 
			msg->MyNum = 1612; //This is where the actual message to send is stored

			//Send packet
			//AM_BROADCAST_ADDR = Constant Broadcast address, send broadcast to and node in range!
			if(call AMSend.send(AM_BROADCAST_ADDR, & _packet, sizeof(MoteToMoteMsg_t)) == SUCCESS) {
				//Set Mote as Busy as to not interrupt other processes
				printf("MSG: %d\r\n", msg->MyNum);
				_radioBusy = TRUE; //Set boolean value as true
			}

			if(val == BUTTON_PRESSED) {
				//Button ON
				//call Leds.led0On();
			}
			else 
				if(val == BUTTON_RELEASED) {
				//Button OFF
				//call Leds.led0Off();
			}
		}
	}

	event void AMSend.sendDone(message_t * msg, error_t error) {
		if(msg == &_packet){
			
			_radioBusy = FALSE;
		}
	}

	event void AMControl.startDone(error_t error) {
		if(error == SUCCESS) {
			//call Leds.led2On();
			printf("Got Message");
		}
		else {
			//Do loop until Success
			call AMControl.start();
		}
	}

	event void AMControl.stopDone(error_t error) {
		// TODO Auto-generated method stub
	}

	event message_t * Receive.receive(message_t * msg, void * payload, uint8_t len) {
		MoteToMoteMsg_t* bounce_msg = NULL;
		if(len == sizeof(MoteToMoteMsg_t)){
			MoteToMoteMsg_t* incomingPacket = (MoteToMoteMsg_t*)payload;
			
			//incomingPacket -> NodeId == 2; //Change this to fit manual added Node ID's
			uint8_t data = incomingPacket -> Data;
			uint16_t aNum = incomingPacket -> MyNum;
			
			if(data == 1){
				call Leds.led2On();
				printf("Packet: %d\r\n", &_packet);
				printf("Incoming Packet: %d\r\n", incomingPacket);
				printf("MyNum: %d\r\n", aNum);
			}
			if(data == 0){
				call Leds.led2Off();
				//printf("led 2 Off");
			}						
		
			//Create the packet
			bounce_msg = (MoteToMoteMsg_t*)call Packet.getPayload(& _packet, sizeof(MoteToMoteMsg_t));
			bounce_msg->NodeId = TOS_NODE_ID;
			bounce_msg->Data = (uint8_t) data; //Add validation 
			bounce_msg->MyNum = 5555; //This is where the actual message to send is stored

			//Send packet
			//AM_BROADCAST_ADDR = Constant Broadcast address, send broadcast to and node in range!
			if(call AMSend.send(AM_BROADCAST_ADDR, & _packet, sizeof(MoteToMoteMsg_t)) == SUCCESS) {
				//Set Mote as Busy as to not interrupt other processes
				printf("Sending new Message");
				_radioBusy = TRUE; //Set boolean value as true
			}
		
		}
		
		return msg;
	}
	



	event void TempRead.readDone(error_t result, uint16_t val){
		// TODO Auto-generated method stub
	}
}