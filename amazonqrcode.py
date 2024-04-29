import qrcode

# لینک سایت آمازون
data = 'https://www.amazon.com'

# ایجاد نمونه کد QR
qr = qrcode.make(data)

# ذخیره تصویر
qr.save('amazon_qrcode.png')
