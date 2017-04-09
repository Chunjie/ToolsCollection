// UDPClient.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <Winsock2.h>

#pragma comment(lib, "ws2_32.lib")


int _tmain(int argc, _TCHAR* argv[])
{
	SOCKET uiFdsocket;
	WSADATA wsaData;
	struct sockaddr_in stServerAddr;
	int iAddrlen = sizeof(sockaddr_in);
	char szbuffer[1024] = "\0";

	if (0 != WSAStartup(MAKEWORD(2, 1), &wsaData))
	{
		printf("Winsock init faied!\r\n");
		WSACleanup();
		return -1;
	}

	memset(&stServerAddr, 0, sizeof(stServerAddr));
	stServerAddr.sin_family = AF_INET;
	stServerAddr.sin_port = htons(12345);
	stServerAddr.sin_addr.s_addr = inet_addr("192.168.12.128");

	printf("Now connecting the server...\r\n");
	uiFdsocket = socket(AF_INET, SOCK_DGRAM, 0);


	printf("input message here...\r\n");
	scanf("%s", szbuffer);

	if (SOCKET_ERROR != sendto(uiFdsocket, szbuffer, sizeof(szbuffer), 0, (struct  sockaddr*)&stServerAddr, iAddrlen))
	{
		Sleep(100);
		if (SOCKET_ERROR != recvfrom(uiFdsocket, szbuffer, sizeof(szbuffer), 0, (struct sockaddr*)&stServerAddr, &iAddrlen))
		{
			printf("recive from server:%s\r\n", szbuffer);
		}
	}

	closesocket(uiFdsocket);
	return 0;
}