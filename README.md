**1. ĐỀ TÀI: QUẢN LÝ GIAO THÔNG**
Các chức năng trong Quản lý chấm công: Quản lí xe, Quản lí nhân viên, Đơn xin mượn xe, 

1.1. Quản lí xe ![image](https://github.com/user-attachments/assets/22588eb0-27a7-49c2-b501-0b3a54436226)


2.1. Quản lí nhân viên

3.1. Đơn mượn xe


**2. Cài đặt công cụ, môi trường và các thư viện cần thiết**
2.1. Clone project.
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
cd odoo-fitdnu
git checkout cntt15_04
2.2. cài đặt các thư viện cần thiết
Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
2.3. khởi tạo môi trường ảo.
Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu

python3.10 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt
3. Setup database
Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.

sudo apt install docker-compose
sudo docker-compose up -d
4. Setup tham số chạy cho hệ thống
4.1. Khởi tạo odoo.conf
Tạo tệp odoo.conf có nội dung như sau:

[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5434
xmlrpc_port = 8069
5. Chạy hệ thống và cài đặt các ứng dụng cần thiết
Lệnh chạy

python3 odoo-bin.py -c odoo.conf -u all
Người sử dụng truy cập theo đường dẫn http://localhost:8069/ để đăng nhập vào hệ thống.

Hoàn tất
