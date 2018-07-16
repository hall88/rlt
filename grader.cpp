//		grader.cpp
//
//		Rhythmic Learning Tool
//		Fall 2017
//		Kenneth Hall
//
//		This program is part of a project that uses a web-app
//		and a Raspberry Pi based controller to teach
//		rhythmic structure in music.
//

// #include	...omitted
// #define	...

#include <stdio.h>
#include <cassert>

#define DELTA_BASE (1000000)
#define LARGE_NUMBER (48000)
#define HISTORY_NUM_COLUMNS (3)
#define KEY_NUM_COLUMNS (6)
#define MU_S (1000000)
#define KEY_SIZE (64)
#define HISTORY_SIZE ((argc - 65) / 3 / 2)
#define latency1 (0)
#define latency2 (0)

long long int key[KEY_SIZE][KEY_NUM_COLUMNS];
long long int history[LARGE_NUMBER][HISTORY_NUM_COLUMNS];

//	debugging key formatting:
//	[button number]	[note length]	[low start time][high start time]	[low stop time]	[high stop time]
//	[0]				[1]				[419871]		[519871]			[619871]		[719871]		key pressed
//	[0]				[1]				[790000]		[810000]			[840000]		[850000]		key released
/*
*	print 64 rows of key	
*	time is in milliseconds
*/
void printKey() {
	printf("parsed key\nbutton number\tnotetype\tstart_lo\tstart_hi\tstop_lo\t\tstop_hi\n");
	for (size_t i = 0; i < KEY_SIZE; i++) {
		printf("#%d: ", i);
		for (size_t j = 0; j < KEY_NUM_COLUMNS; j++) {
			printf("%lld\t\t", key[i][j] > 1000 ? key[i][j] / 1000 : key[i][j]); // print in milliseconds
		}
		printf("\n");
	}
	printf("\n");
}

//	history formatting:
//	[button number][time button pressed][time button released]
//	[...]
/*
*	print (argc - 65) / 3 rows of history
*	[button number][time button pressed][time button released]
*	time is in microseconds
*/
void printHistory(int size) {
	printf("pi history\n#\t\tdown time\tup time\n");
	for (size_t i = 0; i < size; i++) {
		printf("#%d: ", i);
		for (size_t j = 0; j < HISTORY_NUM_COLUMNS; j++) {
			printf("%lld\t\t", history[i][j] > 1000 ? history[i][j] / 1000 : history[i][j]); // print in milliseconds
		}
		printf("\n");
	}
	printf("\n");
}

/* format and store a lesson key into global: key */
void parseKey(char* argv[], int bpm) {
	long long int DELTA = ((DELTA_BASE * 60) / 2) / bpm;
	long long int spb = MU_S * 60 / bpm;
	for (size_t i = 0; i < KEY_SIZE; i++) {
		for (size_t j = 0; j < KEY_NUM_COLUMNS; j++)
		{
			key[i][j] = 0;
		}
	}

	for (size_t i = 0; i < KEY_SIZE; i++) {
		key[i][0] = i % 16; // button #
		key[i][1] = argv[i][0] - 48; // note type

		key[i][2] = (i + 1) * spb - DELTA + latency1;// -(60 * latency1 / bpm); //start lo
		key[i][3] = (i + 1) * spb + DELTA + latency1;// -(60 * latency1 / bpm); //start hi

		long long int offset = (spb * key[i][1]);
		key[i][4] = (i + 1) * spb - DELTA + offset + latency2;// -(60 * latency2 / bpm); // stop lo
		key[i][5] = (i + 1) * spb + DELTA + offset + latency2;// -(60 * latency2 / bpm); // stop hi
	}
}

/* convert string to int */
long long int atoi(char* a[], int b) {
	long long int  result = 0;
	for (size_t i = 0; ; i++) {
		result = result + a[b][i] - 48;
		if (a[b][i + 1] == '\0') {
			return result;
		}
		result *= 10;
	}
}

/* format and store a lesson key into global: history */
void parseHistory(char* key[], int asize) {
	for (size_t i = 0; i < LARGE_NUMBER; i++) {
		for (size_t j = 0; j < HISTORY_NUM_COLUMNS; j++) {
			history[i][j] = 0;
		}
	}

	long long int  history_temp[LARGE_NUMBER][3];
	int history_size;

	int i = 0;
	for (size_t j = 65; j < asize; j += 3) {
		history_temp[i][0] = atoi(key, j); // button #
		history_temp[i][1] = atoi(key, j + 1); // up/down // time pressed
		history_temp[i][2] = atoi(key, j + 2); // time     //time released
		i += 1;
	}

	history_size = i;
	int k = 0;
	for (size_t i = 0; i < history_size; i++) { // take pi record and pair up key presses. assumptions: cant press same key twice without releasing inbetween
		if (history_temp[i][1] == 1) { // if down press
			for (size_t j = 0; j < history_size; j++) { // look for matching release
				if (history_temp[j][1] == 0 && // is a release
					history_temp[j][0] == history_temp[i][0] && // same button numbers
					history_temp[i][2] < history_temp[j][2] // start is less than stop
					) {
					history[k][0] = history_temp[i][0];
					//history[k][1] = history_temp[i][2]; // LEAVE ALONE
					history[k][1] = history_temp[i][2] -1184000+2285000-310000;//815000; // LEAVE ALONE
					history[k][2] = history_temp[j][2] -1335000+2420000-250000;//886000;
					k += 1;
					break;
				}
			}
		}
	}
}


//	main parameter formatting:
//
//	argc = array length
//
//	argv is a array of strings
//	[64 #s indicating duration(0 - 4 only),
//	bpm,
//	{(pi button, up / down, time pressed in microsec), (repeated for all recorded events), ...}]
//
/*
*	argc = array length
*	argv is a array of strings = [64 #s indicating duration(0-4 only) | bpm | {(pi button, up/down, time pressed in microsec), (repeated for all recorded events), ...}]
*	"key" is lesson from firebase
*	"history" is pi recorded presses
*/
extern "C" int main(int argc, char **argv) {

	// check arguments for valid formatting

	printf("argv: \n");
	for (size_t i = 0; i < argc; i++) {
		printf("%d: %lld\n", i, atoi(argv, i));
		assert(atoi(argv, i) <= 600000000 && "string too large... contains a value > 10 min (600000000)");
	}
	printf("argc: %d\n\n", argc);

	assert(argc >= 65 && "input array size is too small");
	assert((argc - 65) % 3 == 0 && "recording data is not div 3");

	int bpm = atoi(argv, 64);
	assert(bpm >= 40 && bpm <= 208 && "bpm must be between 40 and 208");

	int sum = 0;
	int sumrow = 0;
	for (size_t i = 0; i < 64; i++) {
		sum += atoi(argv, i);

		if (i % 4 == 0 && i > 0) {
			//printf("i: %d\n", i);
			//printf("row duration: %d\n\n", sumrow);
			sumrow = 0;
		}
		sumrow += atoi(argv, i);
		assert(sumrow >= 0 && sumrow <= 4 && "key: a row's total duration was incorrect");
	}
	//printf("total duration: %d\n\n", sum);
	assert(sum >= 0 && sum <= 64 && "key: total note length was incorrect");

	assert(HISTORY_SIZE <= LARGE_NUMBER && "history size too large; increase 'LARGE_NUMBER' in grader.cpp");

	parseKey(argv, bpm);
	printKey();

	parseHistory(argv, argc);
	printHistory(HISTORY_SIZE);

	//	grade
	//
	//	compare all entries in HISTORY_SIZE against KEY_SIZE
	//	check press and releases times are w/i limits

	float correct = 0.0;
	for (size_t i = 0; i < HISTORY_SIZE; i++) {
		for (size_t j = 0; j < KEY_SIZE; j++) {
			if (history[i][0] == key[j][0] && // same button number
			    	(key[j][1] != 0) &&
				history[i][1] >= key[j][2] && // start time above start_min
				history[i][1] <= key[j][3] && // start time below start_max
				//history[i][2] >= key[j][4] && // stop time above stop_min
				//history[i][2] <= key[j][5] &&  // stop time below stop_max
			    
				// &&	i != j
				key[j][2] != 0 && // ignore blank key entries
				key[j][3] != 0 &&
				key[j][4] != 0 &&
				key[j][5] != 0
				) {
				correct += 1.0;
				printf("correct row: %d\n", i);
				break;
			}
		}
	}
	int keysize = KEY_SIZE;
	for (size_t i = 0; i < KEY_SIZE; i++) {
		if (key[i][1] == 0) {
			keysize -= 1;
		}
	}

	printf("\ncorrect: %.0f of %d\n", correct, keysize);
	printf("grade: %.2f %%\n", correct / keysize * 100.0);
	printf("return value: %d\n", (int)(correct / keysize * 100.0));
	return (int)(correct / keysize * 100.0);
}
