/* Simon Gmae
 * Author:Pedro Leite
 * Student Number:   61981213
 * Lab Section:      VE3
 * Date:             11/23/2018 3:37:56 PM
 email: pedro.leite@ubc.ca
 *
 * Purpose:  the purpose of the code is to create a memory game called simon. this game will radom 1 out of 4 light, and the user
 needs to press the correspoding push button. as the user gets it right the level goes up and more consecutive lights turn on.
 *
 */
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<Windows.h>
#include <DAQlib.h>
#include <time.h>
 // defining all the possible and useful constants
#define ON 1
#define OFF 0

#define ONE_SECOND 1000

#define SWITCH0 0
#define SWITCH1 1
#define SWITCH2 2
#define SWITCH3 3

#define LED_GREEN 0
#define LED_RED 1
#define LED_YELLOW 2
#define LED_BLUE 3

#define TRUE 1
#define FALSE 0

void write_random_number(int i[], int runlevel);
int run_simom();
void evaluation(void);
void generate_random(int arr[]);
void blink_red(void);

int main(void)
{

	int setupNum;
	// Prints for user to choose between the real device and the simulator
	printf("Enter configuration type (0 for the device or 6 for the simulator): ");
	scanf("%d", &setupNum);

	// Evaluates if the prompt setup number is true and will run the code, otherwise it will print a error messege
	if (setupDAQ(setupNum) == TRUE) {
		
		//calling the funtion that evaluates if the user got the right push button
		evaluation();
	}
	else
		printf("ERROR: Cannot initialise system\n");
	system("PAUSE");
	return 0;
}
void evaluation(void) {
	int got_It;
	int answer;

	// This loop will contunue until the user asks to exit
	while (continueSuperLoop()) {

		got_It = run_simom();

		/* if the user gets all the 5 levels correctly it will blink the green light 3 times and print a winner message, otherwise
		it will print a message that says that the user lost
		*/
		if (got_It) {
			printf("You got it\n");
			digitalWrite(LED_GREEN, ON);
			Sleep(300);
			digitalWrite(LED_GREEN, OFF);
			Sleep(300);
			digitalWrite(LED_GREEN, ON);
			Sleep(300);
			digitalWrite(LED_GREEN, OFF);
			Sleep(300);
			digitalWrite(LED_GREEN, ON);
			Sleep(ONE_SECOND);
			digitalWrite(LED_GREEN, OFF);
		}
		else {

			printf("You lost\n");
		}

		// It asks the user if he wants to play again
		printf("Do you want to play again(1 = Yes, 0 = No)\n");
		scanf("%d", &answer);

		if (answer == 0) {
			break;
		}
	}
}


// Evaluates the use`s answer
// if the user gets right it will increase the game`s level

int run_simom() {

	int level = 1;
	int	run_level = 1;
	int switch0;
	int switch1;
	int switch2;
	int switch3;

	int gotIt = TRUE;
	int arr[] = { 0,0,0,0,0 };

	generate_random(arr);

	while (level <= 5 && gotIt) {
		while (run_level <= level) {


			write_random_number(arr, run_level);


			for (int count = 0; count < run_level; count++) {


				do {
					switch0 = digitalRead(SWITCH0);
					switch1 = digitalRead(SWITCH1);
					switch2 = digitalRead(SWITCH2);
					switch3 = digitalRead(SWITCH3);
				} while (switch0 == OFF && switch1 == OFF && switch2 == OFF && switch3 == OFF);



				if (switch0 == ON && arr[count] != 0) {

					gotIt = FALSE;
					void blink_red(void);
					return gotIt;
				}
				else if (switch1 == ON && arr[count] != 1) {

					gotIt = FALSE;

					void blink_red(void);
					return gotIt;
				}
				else if (switch2 == ON && arr[count] != 2) {

					gotIt = FALSE;

					void blink_red(void);
					return gotIt;
				}
				else if (switch3 == ON && arr[count] != 3) {

					gotIt = FALSE;
					void blink_red(void);

					return gotIt;
				}
				else {
					gotIt = TRUE;


				}
				do {
					switch0 = digitalRead(SWITCH0);
					switch1 = digitalRead(SWITCH1);
					switch2 = digitalRead(SWITCH2);
					switch3 = digitalRead(SWITCH3);
				} while (switch0 == ON || switch1 == ON || switch2 == ON || switch3 == ON);


			}
			run_level++;

		}
		
		printf("level %d \n", level);
		level++;
	}

	return gotIt;

}

// Turns a random LED for 0.3 seconds
void write_random_number(int arr[], int runlevel) {

	digitalWrite(LED_BLUE, OFF);
	digitalWrite(LED_RED, OFF);
	digitalWrite(LED_YELLOW, OFF);
	digitalWrite(LED_GREEN, OFF);

	for (int count = 0; count < runlevel; count++) {

		if (arr[count] == 0) {
			digitalWrite(LED_GREEN, ON);
			Sleep(300);
		}
		if (arr[count] == 1) {
			digitalWrite(LED_RED, ON);
			Sleep(300);
		}
		if (arr[count] == 2) {
			digitalWrite(LED_YELLOW, ON);
			Sleep(300);
		}
		if (arr[count] == 3) {
			digitalWrite(LED_BLUE, ON);
			Sleep(300);
		}

		// it turns the LED off after it lights on
		digitalWrite(LED_BLUE, OFF);

		digitalWrite(LED_RED, OFF);

		digitalWrite(LED_YELLOW, OFF);

		digitalWrite(LED_GREEN, OFF);
		Sleep(300);

	}
}

// generates a random number between 0 and 3
void generate_random(int arr[]) {

	int rand_number;
	srand((unsigned)time(NULL));


	for (int i = 0; i < 5; i++) {
		rand_number = rand() % 4;

		arr[i] = rand_number;

	}
}

// Turn the green light 3 times
void blink_red(void) {
	digitalWrite(LED_RED, ON);
	Sleep(500);
	digitalWrite(LED_RED, OFF);
	Sleep(500);
	digitalWrite(LED_RED, ON);
	Sleep(500);
	digitalWrite(LED_RED, OFF);
	Sleep(500);
	digitalWrite(LED_RED, ON);
	Sleep(500);
	digitalWrite(LED_RED, OFF);
}