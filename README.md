# USB Sürücü Erişim Engelleyici

Bu, Windows sistemlerinde USB sürücülerini izleyen ve erişimini engelleyen bir Python programıdır. USB sürücüsü takıldığında, terminalde bir mesaj görüntüler ve sürücüye erişimi engeller. Program çalıştığı sürece sürücü erişilemez kalır. Program ayrıca takılan ve çıkarılan USB sürücülerinin bilgisini de sağlar.

## Gereksinimler

- Python 3.x
- win32file modülü

`win32file` modülünü pip kullanarak yükleyebilirsiniz:


## Kullanım

1. Depoyu klonlayın veya `usb_sürücü_erişim_engelleyici.py` dosyasını indirin.

2. Bir terminal açın ve `usb_sürücü_erişim_engelleyici.py` dosyasının bulunduğu dizine gidin.

3. Aşağıdaki komutu kullanarak programı çalıştırın:

4. Program USB sürücülerini izlemeye başlayacak. Bir USB sürücüsü takıldığında, terminalde sürücünün erişilemez olduğunu ve USB sürücüsünün çıkarılması gerektiğini belirten bir mesaj görüntülenecektir. Program sürücüye erişimi engelleyecektir.

5. Programı durdurmak için terminalde Ctrl+C tuşlarına basın.

## Notlar

- Bu program, Windows sistemlerinde kullanılmak üzere tasarlanmıştır.
- Program, sürücü türünü belirlemek ve USB sürücülerine erişimi engellemek için `win32file` modülünü kullanır.
- Programın sürücü erişimini engellemek için yönetici izinleriyle çalıştırılması gerekmektedir.

## Sorumluluk Reddi

Bu program herhangi bir garanti olmaksızın sunulmaktadır. Kendi sorumluluğunuzda kullanın. Yazar, bu programın kullanımından kaynaklanan herhangi bir hasardan sorumlu değildir.

## Lisans

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu projeyi [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisansladık. Lisansın tam açıklamasını burada bulabilirsiniz.
