configuration MoteToMoteAppC{
	//Not used now
	
}


implementation{
	
	components MoteToMoteC as App; //Name of ModFile
	components MainC; //Boot Interface
	components LedsC;
	
	App.Boot -> MainC;	
	App.Leds -> LedsC;
	
	components UserButtonC;
	App.Get -> UserButtonC;
	App.Notify -> UserButtonC;
	
	components SerialPrintfC;
	
	//radio comps
	components ActiveMessageC;
	components new AMSenderC(AM_RADIO);
	components new AMReceiverC(AM_RADIO);
	
	App.Packet -> AMSenderC;
	App.AMPacket -> AMSenderC;
	App.AMSend -> AMSenderC;
	App.AMControl -> ActiveMessageC;
	App.Receive -> AMReceiverC;
	
	//Temperature components
	components new SensirionSht11C() as TempSensor;
	
	App.TempRead -> TempSensor.Temperature;
	
	
}