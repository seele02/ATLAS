configuration TempTestAppC{
	
}


implementation{
	//General components
	components TempTestC as App;
	components MainC, LedsC;
	components new TimerMilliC();
	
	App.Boot -> MainC;
	App.Leds -> LedsC;
	App.Timer -> TimerMilliC;
	
	//For writing into serial port
	components SerialPrintfC;	
	
	//Temperature components
	components new SensirionSht11C() as TempSensor;
	
	App.TempRead -> TempSensor.Temperature;
	
}