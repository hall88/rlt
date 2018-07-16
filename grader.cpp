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
//		It must deconstruct an array of strings into
//		a lesson key and key press history.
//		Afterwards, it evaluates and returns a grade.
//

#include	...
#define		...

long long int key[KEY_SIZE][KEY_NUM_COLUMNS];
long long int history[LARGE_NUMBER][HISTORY_NUM_COLUMNS];

//	debugging key formatting:
//	[button #]	[note len]	[low start time][high start time]	[low stop time]	[high stop time]
//	[0]			[1]			[419871]		[519871]			[619871]		[719871]
//	[0]			[1]			[790000]		[810000]			[840000]		[850000]
void printKey() { ...


//	history formatting:
//	[button number][time button pressed][time button released]
//	[...]
void printHistory(int size) { ...


/* format and store a lesson key into global: key */
void parseKey(char* argv[], int bpm) { ...

/* convert string to int */
long long int atoi(char* a[], int b) { ...

/* format and store a lesson key into global: history */
void parseHistory(char* key[], int asize) { ...


//	main parameter formatting:
//
//		1. argc = array length
//
//		2. argv is a array of strings:
//			[64 #s indicating duration(0 - 4 only),
//			bpm,
//			{(pi button, up / down, time pressed in microsec), (repeated for all recorded events), ...}]
//
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
