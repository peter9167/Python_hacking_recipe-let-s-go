from socket import * #from socket import *
import os #import os


def parsing(host):
    # raw socket 생성 및 binding
    if os.name == "nt":
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP
    sock = socket(AF_INET, SOCK_STREAM, sock_protocol)
    sock.bind((host, 0))

    # socket 옵션
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    # promiscuos mode 켜기
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)

    data = sock.recvfrom(65535)
    print(data[0])

    # promiscuos mode 끄기
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_OFF)

    # 소켓 종료
    sock.close()


if __name__ == "__main__":
    host = "192.168.0.5"  # 자신의 IP 주소로 변경
    print(f"Listening at [{host}]")
    parsing(host)
