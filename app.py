import socket
import binascii


def send_data(stm32_ip, stm32_port, hex_message):
    isSuccess  = True
    try:
        # Khởi tạo kết nối đến STM32 qua TCP/IP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((stm32_ip, stm32_port))
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
        client_socket.close()
        if isSuccess:
            return response_hex
        else:
            return error_message
        
if __name__ == "__main__":
    # Địa chỉ IP của STM32
    stm32_ip = "192.168.1.100"
    # Cổng TCP/IP mà STM32 đang lắng nghe (thường là 502)
    stm32_port = 502

    

    # Chuỗi hex của bản tin Modbus RTU
    hex_message = "010300000002C40B"
    print(send_data(stm32_ip=stm32_ip, stm32_port=stm32_port, hex_message=hex_message))