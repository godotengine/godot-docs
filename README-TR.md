Godot Motor belgeleri

Bu depo, Godot Engine belgelerinin kaynak dosyalarını reStructuredText işaretleme dilinde (reST) içerir.

Onlar, Godot'un web sitesinde HTML belgelerini oluşturmak için Sphinx dokümantasyonu oluşturucu ile ayrıştırılmak üzere tasarlandı.

Katkıda bulunan değişiklikler

Çekme İstekleri varsayılan olarak ana dalı kullanmalıdır. Değişiklikleriniz yalnızca söz konusu Godot sürümü için geçerliyse, yalnızca diğer şubelerle (örneğin 2.1 veya 3.0) Çekme Talepleri yapın.

Her ne kadar bir wiki'den daha az uygun olsa da, bu git deposu, her zaman dokümantasyonu geliştirmek, yeni sayfalar eklemek vb. İçin çekme talepleri almak anlamına gelir.Belgelerimizin kalitesi bir revizyon kontrol sistemindeki kaynak dosyalara doğrudan erişime sahip olmak büyük bir artıdır. .

Mevcut sayfaları düzenleme

Mevcut bir sayfayı düzenlemek için .rst kaynak dosyasını bulun ve en sevdiğiniz metin düzenleyicide açın. Daha sonra değişiklikleri yapabilir, çatalınıza itip bir çekme talebi yapabilirsiniz. Sınıflardaki sayfaların burada düzenlenmemesi / düzenlenmemesi gerektiğini ve otomatik olarak Godot'un XML sınıf referanslarından oluşturulduğunu unutmayın.

Yeni sayfalar ekleme

Yeni bir sayfa eklemek için, dosya eklemek istediğiniz bölümden anlamlı bir isimle bir .rst dosyası oluşturun. öğreticiler / 3d / light_baking.rst. İçeriğini, başka bir dosya için yaptığınız gibi yazın ve dosya adında bir "doc_" öneki ile (örneğin, sözdizimine ilişkin diğer dosyaları kontrol edin), Sfenks için bir referans adı tanımladığınızdan emin olun. .. _doc_light_baking :).

Daha sonra sayfanızı ilgili "toctree" (içerik tablosu) bölümüne eklemelisiniz. Sözleşmeye göre, çeşitli düzeydeki toctree düzeylerini tanımlamak için kullanılan dosyalar, bir alt çizgi ile öneklenir, bu nedenle yukarıdaki örnekte, dosya, eğiticiler / 3d / _3d_graphics.rst dosyasında belirtilmelidir. Yeni dosya adınızı listeye yeni bir satıra ekleyin, göreceli bir yol ve uzantı yok, ör. Burada light_baking.

Sfenks ve reStructuredText sözdizimi

Sözdizimi ile ilgili ayrıntılar için Sphinx'in reST Primer ve resmi referansını kontrol edin.

Sphinx, belirli bir işlem yapmak için belirli reST yorumlarını kullanır (içerik tablosunu tanımlamak gibi) (: toctree :) veya çapraz referans sayfaları). Daha fazla ayrıntı için resmi Sphinx belgelerine bakın veya mevcut sayfalarda işlerin nasıl yapıldığını görün ve ihtiyaçlarınıza göre uyarlayın.

Resim ve ek ekleme

görüntüleri eklemek için, anlamlı bir adla .rst dosyanın yanındaki bir img / klasöre koyun ve birlikte sayfanıza bunları da ekleyin:

.. image:: img/image_name.png

Benzer şekilde, (bir eğitici için destek malzemesi olarak varlıklar gibi) ekleri .stst dosyasının yanındaki bir dosya / klasöre yerleştirerek ve bu satır içi işaretlemeyi kullanarak ekleyebilirsiniz:

:download:`myfilename.zip <files/myfilename.zip>`

Sfenks ile bina

HTML web sitesini (veya PDF, EPUB veya LaTeX gibi Sphinx tarafından desteklenen herhangi bir format) oluşturmak için, Sphinx> = 1.3 ve ayrıca (HTML için) readthedocs.org temasını yüklemeniz gerekir. Python 2 sürümleri de işe yarayabilse de sadece Python 3 aroması test edildi.

Bu araçlar pip, Python modülü kurulumu kullanılarak en iyi şekilde yüklenir. Python 3 versiyonu (Linux dağıtımlarında) pip3 veya python3-pip olarak sağlanabilir. Daha sonra koşabilirsiniz:

pip3 install sphinx pip3 install sphinx_rtd_theme

Daha sonra bu dokümanın kök klasöründen HTML belgelerini aşağıdakilerle oluşturabilirsiniz:

make html

veya:

make SPHINXBUILD=~/.local/bin/sphinx-build html

Sınıflandırma / klasör ayrıştırılacak birçok dosya içerdiğinden derleme biraz zaman alabilir.
Daha sonra, favori tarayıcınızda _build / html / index.html dosyasını açarak değişiklikleri test edebilirsiniz.

Windows'da Sfenks ile Bina

Windows'da yapmanız gerekenler:

Python yükleyicisini buradan indirin.

Python'u yükleyin. "Python'u PATH'a Ekle" kutusunu işaretlemeyi unutmayın.

Yukarıdaki pip komutlarını kullanın.

Sağlanan kullanarak bu deponun kök klasöründe bina hala yapılır make.bat:

make.bat html

Alternatif olarak, bunun yerine bu komutla oluşturabilirsiniz:

sphinx-build -b html ./ _build

İlk kurulum sırasında, çeşitli kurulum mesajları görünebileceğini ve LaTeX eklentilerini yüklemeyi isteyebileceğini unutmayın. Bunları özlemediğinizden emin olun, özellikle de diğer pencerelerin ardında açılırlarsa, bu istemleri onaylayana kadar yapı asılmayabilir.

Normal bir make toolchain (örneğin MinGW ile) kurabilir ve normal make html kullanarak dokümanlar oluşturabilirsiniz.

Sfenks ve virtualenv ile bina

Sfenks kurulumunuzun projeye dahil olmasını istiyorsanız, virtualenv kullanarak kurabilirsiniz. Bunu bu deponun kök klasöründen çalıştırın:

virtualenv --system-site-packages env/ . env/bin/activate pip3 install sphinx pip3 install sphinx_rtd_theme

Sonra yukarıdaki gibi html yap.

Lisans

Sınıflar / klasör haricinde, bu havuzun tüm içeriği Creative Commons Attribution 3.0 Sınırsız lisansı (CC BY 3.0) altında lisanslanır ve "Juan Linietsky, Ariel Manzur ve Godot topluluğu" na atfedilir.

Sınıflardaki / klasördeki dosyalar, Godot'un ana kaynak deposundan elde edilir ve MIT lisansı altında, yukarıdaki gibi aynı yazarlarla dağıtılır.

