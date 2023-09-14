import socket
import binascii
'''
    @param stm32_ip: a tring, for example: "192.168.1.1"
    @param stm32_port: a integer, for example: 502
'''
def connect_device(stm32_ip, stm32_port=502):
    isSuccess = True
    try:
        # Khởi tạo kết nối đến STM32 qua TCP/IP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((stm32_ip, stm32_port))
    except Exception as e:
        isSuccess = False
        client_socket = None
    finally:
        return isSuccess, client_socket

def send_data(client_socket, hex_message):
    isSuccess  = True
    try:
        # Chuyển đổi chuỗi hex thành dạng bytes
        message_bytes = binascii.unhexlify(hex_message)

        # Gửi bản tin đến STM32
        client_socket.send(message_bytes)

        # Nhận phản hồi từ STM32
        response = client_socket.recv(1024)
        response_hex = binascii.hexlify(response).decode('utf-8')

    except Exception as e:
        isSuccess = False
        error_message = str(e)
    finally:
        # Đóng kết nối
        if isSuccess:
            return response_hex
        else:
            return error_message

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