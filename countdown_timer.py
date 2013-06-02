import sys,os,datetime,time
while True:
	delta = datetime.datetime(2013,06,04,13) - datetime.datetime.now()
	hours = delta.seconds/3600;
	minutes = (delta.seconds-(hours*3600))/60
	seconds = delta.seconds-((hours*3600)+(minutes*60))
	text = "%02d Days %02d Hours %02d Minutes %02d Seconds" % (delta.days,hours,minutes,seconds)
	print "\033[1;38;5;19m"+"-"*38+"\n"+"|"+"TIME UNTIL SHIP".center(36)+"|"+"\n"+"-"*38+"\n"
        print "\033[1;38;5;124m"+text+"\033[0;0m"
	time.sleep(1)
	print "\033c"
	#os.system("clear")
#\033[38;5;RGB_INTm -> text color
#\033[48;5;RGB_INTm -> background color
