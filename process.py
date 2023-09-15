from  socket import socket, AF_INET, SOCK_STREAM
from  binascii import unhexlify, hexlify
from ipaddress import IPv4Address, IPv6Address

'''
    @param stm32_ip: a tring, for example: "192.168.1.1"
    @param stm32_port: a integer, for example: 502
'''
def connect_device(stm32_ip, stm32_port=502):
    try:
        IPv4Address(stm32_ip)
    except:
        try:
            IPv6Address(stm32_ip)
        except:
            return False, None
    try:
        # Khởi tạo kết nối đến STM32 qua TCP/IP
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((stm32_ip, stm32_port))
        return True, client_socket

    except Exception as e:
        return False, None

'''
    @param client_socket: get from connect_device if isSuccess == True
    @param hex_message: information which is needed to send
'''
def send_data(client_socket, hex_message):
    try:
        # Chuyển đổi chuỗi hex thành dạng bytes
        message_bytes = unhexlify(hex_message)

        # Gửi bản tin đến STM32
        client_socket.send(message_bytes)

        # Nhận phản hồi từ STM32
        response = client_socket.recv(1024)
        response_hex = hexlify(response).decode('utf-8')
        return True, response_hex

    except Exception as e:
        return False, str(e)
    
'''
    @param isCheck: confirm if connecting is successful, is the same as param isSuccess
    @param client_socket get from connect_device
'''
def disconnect_device(isCheck, client_socket):
    if isCheck:
        client_socket.close()


if __name__ == "__main__":
    # Địa chỉ IP của STM32
    stm32_ip = "192.168.1.100"
    # Cổng TCP/IP mà STM32 đang lắng nghe (thường là 502)
    stm32_port = 502

    _, client_socket =  connect_device(stm32_ip, stm32_port)
    print(_)
    # Chuỗi hex của bản tin Modbus RTU
    hex_message = "010300000002C40B"
    print(send_data(client_socket, hex_message=hex_message))
    disconnect_device(_,client_socket)
