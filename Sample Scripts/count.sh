#!/bash/bin/bash
#bash counter program

echo "Hello, please enter a number with 3 to 15 alphabetical characters“
read myName
echo "Hello there $myName"

while [[ $myName == "" ]];
	do
	echo "Please enter a name"
	read myName
done

while [[ ${#myName} -lt 3 || ${#myName} -gt 15 ]]
	do
	echo “Name must between 3 to 15 characters”
	echo “Please enter a name”
	read myName
done


while [[ $myName =~ [^a-zA-Z]+ ]]
	do 
	echo “That is not a name”
	read myName
done

echo "Enter number between 3 and 100" 
read myNum
echo "You entered $myNum"

while [[ $myNum == "" ]]
	do
	echo "C'mon now, please enter a number"
	read myNum
done

while [[ $myNum =~ [^0-9] ]]
	do
	echo "C'mon now, please enter a number"
	read myNum
done

while [ $myNum -lt 3 ]
	do
	echo "Needs to be greater than 3"
	read myNum 
done

while [[ $myNum =~ [^0-9] ]]
	do
	echo "C'mon now, please enter a number"
	read myNum
done

while  [[ $myNum -gt 100 ]] 
	do 
	echo "Needs to be less than 100"
	read myNum
done 

while [[ $myNum =~ [^0-9] ]]
	do
	echo "C'mon now, please enter a number"
	read myNum
done

clear

counter=0
# even numbers start at 0, odds will start at 1
if ! [ $(( myNum % 2 )) == 0 ];
	then 
	counter=1
else 
	counter=0
fi 

while [ $counter -le  $myNum ];
	do
	echo $counter 
	counter=$((counter +2));
	sleep 0.2
done

echo "we out here"

