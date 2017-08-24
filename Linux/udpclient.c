#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <string.h>

#define BUFLEN 512
#define NPACK 10

void diep(char *s)
{
    perror(s);
    exit(1);
}

/*
 * A simple udp client on Linux, run as 'udpclient server port'
 */
int main(int argc, char ** argv)
{
    struct sockaddr_in si_me, si_other;
    int s, i, slen = sizeof(si_other);
    char buf[BUFLEN];
    char *server;
    int portno;

    if (argc != 3) {
        fprintf(stderr,"usage: %s <hostname> <port>\n", argv[0]);
        exit(0);
    }
    server = argv[1];
    portno = atoi(argv[2]);

    if ((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
        diep("socket");

    memset(&si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = htons(portno);
    si_other.sin_addr.s_addr = inet_addr(server);

    for (i = 0; i < 10000000; i++) {
        strcpy(buf, "Hello, Server!\n");
        if (sendto(s, buf, strlen("Hello, Server!\n") + 1, 0, &si_other, slen) == -1)
            diep("sendto()");

        //if (recvfrom(s, buf, BUFLEN, 0, &si_other, &slen) == -1)
        //    diep("recvfrom()");
        //printf("Received packet from %s:%d\nData: %s\n\n", inet_ntoa(si_other.sin_addr), ntohs(si_other.sin_port), buf);
    }

    close(s);
    return 0;
}
