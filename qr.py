import qrcode

# داده‌ها برای رمزگذاری
data = 'سلام، دنیا!'

# ایجاد نمونه کد QR
qr = qrcode.make(data)

# ذخیره تصویر
qr.save('qrcode.png')

