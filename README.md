# Peer-to-peer file-sharing app with centralized server

## User Manual

### Download hoặc clone source code
```console
git clone https://github.com/PhucLe03/Simple-p2p-filesharing-app-with-centralized-server.git
```

### Server
#### Bước 1: Chạy terminal
```c
cd main
py server.py
```
Note: Nếu lệnh `py` không sử dụng được thì hãy thử `python` hoặc `python3`
#### Bước 2: Start Server
Bấm "Start Server" để khởi động server, sau khi khởi động trên hộp thoại của server có hiện địa chỉ IP local của server, các client sử dụng địa chỉ này để kết nối
Sau khi nhận được thông tin có các client đã kết nối vào server thì ta có thể bấm vào "Client List" để xem danh sách các client đã kết nối và sử dụng các chức năng Ping và Discover
#### Bước 3: Ping và Discover
Sau khi bấm "Client List" và một cửa sổ mới mang tên "CLIENT STATUS" hiện ra, kế bên các nút "Discover" và "Ping" là các khung để nhập vào địa chỉ IP và cổng của client, phía dưới là danh sách các client đã kết nối với server gồm địa chỉ IP và cổng, cách nhau bởi dấu ":"

- Ping: nhập địa chỉ IP và cổng của client theo định dạng "IP:PORT", bấm "Ping" sẽ hiện lên một hộp thoại, nếu client vẫn còn kết nối thì hộp thoại sẽ có nội dung là "This client is currently connected", ngược lại sẽ hiện "Address is not valid"

- Discover: nhập địa chỉ IP và cổng của client theo định dạng "IP:PORT", bấm "Discover" sẽ mở ra một cửa sổ "DISCOVER" chứa danh sách các file mà client đó đã publish

`Hint`: Địa chỉ IP và cổng theo định dạng "IP:PORT" có thể được copy ở danh sách client

### Client
#### Bước 1: Chạy terminal
```c
cd main
py client.py
```
Note: Nếu lệnh `py` không sử dụng được thì hãy thử `python` hoặc `python3`
#### Bước 2: Connect tới server
Sau khi xác nhận server đã được khởi động, nhập địa chỉ IP của server vào khung ngay dưới dòng chữ "Enter server’s IP address" (được tìm thấy ở trên hộp thoại của server) và bấm "CONNECT" sẽ kết nối được tới server
#### Bước 3: Publish file
Khi muốn publish một file nào đó, bấm "PUBLISH" để hiện ra cửa sổ để chọn file
#### Bước 4: Tải file mà client khác đã publish
Khi muốn tải một file nào đó từ client khác, nhập tên file vào khung ngay dưới dòng chữ "Enter file name" và bấm "DOWNLOAD", file muốn tải sẽ được tải về và lưu trữ trong thư mục "downloads" nằm trong thư mục "main"

`Note`: App hiện tại chỉ có hỗ trợ tải những file mà các client khác đã publish, nếu file không tìm thấy ở các client khác thì app sẽ bị lỗi; ngoài ra, chức năng "DOWNLOAD" chỉ thực hiện được ở một client/máy, nếu trên một máy nhiều client muốn tải thì sẽ gặp lỗi

## Authors

[Nguyễn Hoàng Khôi Nguyên](https://github.com/DracNguyen)

[Nguyễn Duy](https://github.com/Duy-CS)

[Lê Hoàng Phúc](https://github.com/PhucLe03)

[Đặng Thanh Huy](https://github.com/ThanhHuy1006)
