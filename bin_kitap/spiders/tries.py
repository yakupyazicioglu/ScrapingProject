import re

details = ['Sineklerin Tanrısı', 'William Golding', 'Mina Urgan', 'İş Bankası Kültür Yayınları', '2. Hamur', '262', '12,5 x 20,5', '2006', 'Türkçe', '9789754582901']
str2 = ['Konu ', ' ise “Bir kitap okudum ve hayatım değişti.” cümlesi, tüm mecazlardan sıyrılıp gerçek bir anlama bürünüyor. Ölümsüz yazar Victor Hugo’nun 1829 yılında kaleme aldığı roman, yazarın Paris’teki ünlü Greve Meydanı’nda gerçekleştirilen bir idama tanıklık etmesinden ilham alıyor.', ', 19’uncu yüzyıl Fransa’sını gerçekçi bir biçimde yansıtması bakımından tarihi ve toplumsal bir kaynak olarak değerlendiriliyor. Yazarın henüz 27 yaşındayken takma bir adla yayımladığı eser, döneminin siyasi ve sosyolojik yapısına bir eleştiri niteliği taşıyor.\xa0', ', idamı bekleyen bir adamın dilinden yazılmış olmasıyla etkileyici bir anlatıma sahip. Romantizm akımının en güçlü temsilcisi olan Hugo, ölüm korkusu ve merhamet duygularını okuruna sarsıcı bir empati ile hissettiriyor. Eser, ölüme yaklaşan bir insanın ruh halindeki değişimleri başarılı bir şekilde ortaya koyması sayesinde aynı zamanda psikolojik bir roman olma özelliği de taşıyor.', 'İdamı “devrimlerin yok edemediği kaide” olarak nitelendiren Hugo, kitabının ön sözünde bu infaz yöntemi hakkındaki görüşlerini okuruna bir manifesto havasında sunuyor. Sonrasında ise romanının ön hazırlığını, kitabın konusuna dair konuşmaların yer aldığı bir tiyatro piyesiyle yapıyor. Yazar, bu kısımda topluma ve kitabına karşı eleştirilerini doğrudan halktan kişiler aracılığıyla yaparak farklı bir çalışma ortaya koyuyor.', 'Romanın son kısmında yazar, okurunu cinayet suçu ile tutuklanan ve mahkemede beş hafta sonra idam edileceğini öğrenen bir adamın satırlarıyla baş başa bırakıyor. Mahkum edilmeden önceki yaşamına oldukça yabancılaşan anlatıcı, okura daha çok içe dönük bir durum hikayesi anlatıyor. Romanda bu nedenle birbirinin yerini alan iki duygu ağır basıyor: Umut ve korku. Eserin ana fikrini besleyen bir diğer çarpıcı yönünü ise mahkumun son anda insanlar hakkındaki düşünceleri oluşturuyor.', 'Dünya klasikleri arasında yer alan ', '’nü hala kitaplığınıza eklemediniz mi? Bu kitaba sahip olmak için beklemeyin ve hemen şimdi sipariş verin! ', ', size dokunaklı olduğu kadar hayati bir düşünsel sürecin de kapılarını açacak.', '\xa0', '\xa0', '\xa0']
info = ''.join(str(e) for e in str2)
strFull = '2000'
str1 = ''.join(str(e) for e in details)
isbn = re.findall("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", str(str1))
publishedDate = re.findall("[2][0][0-2][0-9]", str(str1))

print(isbn) 
print(info) 
print(publishedDate)
