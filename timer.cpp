#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define ST_BASE (0x20003000)
#define TIMER_OFFSET (4)

extern "C" long long int getTime(int argc, char *argv[]) {
	int fd;
	void *st_base; // byte ptr to simplify offset math
	if (-1 == (fd = open("/dev/mem", O_RDONLY))) {	// get access to system core memory
		fprintf(stderr, "open() failed.\n");
		return 255;
	}
	if (MAP_FAILED == (st_base = mmap(NULL, 4096, PROT_READ, MAP_SHARED, fd, ST_BASE))) {	// map a specific page into process's address space
		fprintf(stderr, "mmap() failed.\n");
		return 254;
	}

	long long int* timer = (long long int *)((char *)st_base + TIMER_OFFSET);	// set up pointer, based on mapped page

	//long long int prev = *timer;	// read initial timer
	//sleep(1);

	//for (size_t i = 0; i < 10; i++)	{
	//	long long int t = *timer;		// read new timer
	//	printf("Timer diff = %lld    \n", t - prev);		// print difference (and flush output)
	//	//printf("%lld\n", *timer);
	//	fflush(stdout);
	//	prev = t;		// save current timer
	//	sleep(1);		// and wait
	//}
	//printf ("%lld\n:",*timer);
	return *timer;
}
