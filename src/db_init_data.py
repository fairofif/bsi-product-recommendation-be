from src import app, db
from src.models import MasterDataProducts, MasterDataSegmentation, SalaryRange, JobType, MasterDataProductsBenefits, Province

def clear_master_data():
    db.session.query(Province).delete()
    db.session.query(MasterDataProductsBenefits).delete()
    db.session.query(MasterDataProducts).delete()
    db.session.query(MasterDataSegmentation).delete()
    db.session.query(SalaryRange).delete()
    db.session.query(JobType).delete()
    db.session.commit()


def init_products():
    initial_products = [
        MasterDataProducts(alias="e-mas", name="E-mas", desc="Akses investasi emas mudah dalam genggaman", image_uri="https://i.postimg.cc/Jn67R8XJ/e-mas.png", details="Tabungan E-Mas BSI merupakan fasilitas rekening berbasis titipan (wadiah yad amanah) yang tersedia di BSI Mobile dan BYOND, di mana saldo rekening dinyatakan dalam satuan gram emas."),
        MasterDataProducts(alias="reksadana-syariah", name="Reksadana Syariah", desc="Investasi lebih mudah untuk masa depan yang lebih berkah", image_uri="https://i.postimg.cc/442ng6vM/reksadana.jpg", details="Reksa Dana Syariah adalah instrumen investasi yang menghimpun dana dari masyarakat pemodal sebagai pemilik harta. Dana tersebut kemudian diinvestasikan dalam portofolio efek syariah oleh Manajer Investasi, dengan tetap mengikuti prinsip syariah dan tidak bertentangan dengan ketentuan Islam.\nSebagai produk pasar modal, Reksa Dana Syariah bukan merupakan produk perbankan, sehingga Bank Syariah Indonesia (BSI) tidak memberikan jaminan dalam bentuk apapun. Selain itu, reksa dana ini tidak termasuk dalam cakupan program penjaminan pemerintah atau Lembaga Penjamin Simpanan (LPS).\nDengan Reksa Dana Syariah, investor dapat berinvestasi sesuai prinsip syariah, dengan pengelolaan yang transparan dan profesional oleh Manajer Investasi."),
        MasterDataProducts(alias="bsi-simpel", name="Simpel", desc="Pilihan Anak Cerdas Indonesia menabung jadi SimPel", image_uri="https://i.postimg.cc/X7Zq7rQv/BSI-Sim-Pel.jpg", details="BSI Tabungan Simpanan Pelajar (SimPel) adalah produk tabungan yang ditujukan khusus untuk siswa berusia kurang dari 17 tahun, diterbitkan secara nasional oleh bank-bank syariah di Indonesia. Tabungan ini memiliki persyaratan yang mudah dan sederhana, serta dilengkapi dengan fitur menarik untuk mendukung kebiasaan menabung sejak dini.\nSebagai bagian dari upaya edukasi dan inklusi keuangan, BSI Tabungan SimPel bertujuan untuk mengenalkan siswa pada layanan perbankan syariah, membantu mereka mengelola keuangan dengan lebih baik, serta mendorong budaya menabung secara disiplin. Selain itu, tabungan ini juga mendukung program inklusi keuangan yang diselenggarakan oleh Otoritas Jasa Keuangan (OJK).\nDengan prinsip syariah yang transparan dan sistem pengelolaan yang aman, BSI Tabungan SimPel menjadi pilihan tepat bagi pelajar yang ingin mulai menabung dengan mudah dan nyaman."),
        MasterDataProducts(alias="tabungan-wadiah", name="Tabungan Wadiah", desc="Menjaga Harta Anda Tetap Murni", image_uri="https://i.postimg.cc/rs78t9Qw/tabungan-wadiah.jpg", details="BSI Tabungan Wadiah adalah produk tabungan berbasis akad wadiah yad dhamanah, yang berarti nasabah menitipkan dana kepada Bank Syariah Indonesia (BSI) dengan amanah, tanpa adanya imbal hasil atau bagi hasil. Namun, sebagai bentuk apresiasi, BSI dapat memberikan bonus yang tidak diperjanjikan sebelumnya.\nTabungan ini cocok bagi nasabah yang menginginkan simpanan yang aman, bebas biaya administrasi bulanan, dan dikelola sesuai prinsip syariah."),
        MasterDataProducts(alias="tabungan-mudharabah", name="Tabungan Mudharabah", desc="Menjaga Harta Anda Tetap Murni", image_uri="https://i.postimg.cc/pXnVMgLh/tabungan-mudharabah.jpg", details="BSI Tabungan Easy Mudharabah adalah produk tabungan dari Bank Syariah Indonesia (BSI) yang menggunakan akad mudharabah mutlaqah, yaitu kerja sama antara nasabah sebagai pemilik dana (shahibul maal) dan bank sebagai pengelola dana (mudharib). Dalam skema ini, nasabah berhak mendapatkan bagi hasil sesuai nisbah yang telah disepakati.\nTabungan ini cocok bagi nasabah yang ingin menabung sekaligus berinvestasi dengan prinsip syariah, di mana dana yang disimpan akan dikelola oleh bank dalam kegiatan usaha yang halal dan produktif."),
        MasterDataProducts(alias="deposito", name="Deposito", desc="Investasi Aman dengan Imbal Hasil Optimal", image_uri="https://i.postimg.cc/CLdBBPLS/deposito.jpg", details="BSI Deposito adalah produk simpanan berjangka dari Bank Syariah Indonesia (BSI) yang dikelola berdasarkan prinsip syariah. Deposito ini menggunakan akad Mudharabah Mutlaqah, di mana nasabah sebagai pemilik dana (shahibul maal) mempercayakan dananya kepada bank (mudharib) untuk dikelola dalam kegiatan usaha yang halal dan produktif. Sebagai imbalannya, nasabah akan mendapatkan bagi hasil sesuai nisbah yang telah disepakati. Produk simpanan ini mulai dari Rp 2 juta hingga Rp 1 miliar."),
        MasterDataProducts(alias="hasanah-card", name="Hasanah Card", desc="Partner Transaksi Hijrah Hasanah", image_uri="https://i.postimg.cc/zvyzBQwQ/hasanah-card.jpg", details="BSI Hasanah Card adalah kartu pembiayaan berbasis syariah yang diterbitkan oleh Bank Syariah Indonesia (BSI), digunakan sebagai alat pembayaran untuk transaksi sesuai dengan prinsip-prinsip syariah. Kartu ini dibuat berdasarkan Fatwa DSN No. 54/DSN-MUI/X/2006 tentang syariah card dan menggunakan tiga akad utama yaitu, Kafalah bil Ujrah adalah Bank bertindak sebagai penjamin pembayaran transaksi antara pemegang kartu dengan merchant, Qard adalah Bank memberikan pinjaman darurat dalam bentuk penarikan tunai bagi pemegang kartu, dan Ijarah adalah Bank menyediakan layanan sistem pembayaran dengan biaya keanggotaan tahunan dan bulanan."),
        MasterDataProducts(alias="griya", name="Griya", desc="Makin Mudah Miliki Hunian, Rumah Impian Jadi Kenyataan", image_uri="https://i.postimg.cc/nLxhk0Zs/griya.jpg", details="BSI Griya adalah fasilitas pembiayaan dari Bank Syariah Indonesia (BSI) yang dirancang untuk membantu nasabah memiliki rumah atau properti lainnya melalui prinsip syariah. Produk ini menawarkan berbagai layanan pembiayaan yang dapat disesuaikan dengan kebutuhan nasabah, antara lain:\nBSI Griya Pembelian: Pembiayaan untuk pembelian rumah, ruko, rukan, atau apartemen, baik baru maupun bekas, dengan menggunakan akad murabahah (jual beli).\nBSI Griya Take Over: Fasilitas untuk pengambilalihan pembiayaan KPR dari bank lain ke BSI dengan angsuran yang lebih ringan dan tetap. Program ini menawarkan margin khusus mulai dari 3,3% efektif per tahun yang tetap selama tahun pertama, serta bebas biaya provisi dan penalti.\nBSI Griya Top Up: Layanan penambahan pembiayaan bagi nasabah existing BSI Griya dengan menggunakan properti yang masih menjadi agunan dari pembiayaan sebelumnya, melalui akad Musyarakah Mutanaqisah (MMQ).\nBSI Griya Refinancing: Pembiayaan yang ditujukan untuk memenuhi berbagai kebutuhan nasabah seperti renovasi rumah, biaya pendidikan, atau biaya kesehatan, dengan menggunakan penilaian atas rumah yang dimiliki nasabah sebagai dasar pembiayaan."),
        MasterDataProducts(alias="bsi-oto", name="BSI OTO", desc="Punya Kendaraan Impian Kini Lebih Gampang", image_uri="https://i.postimg.cc/q7GMZyM1/bsi-oto.jpg", details="BSI OTO adalah Fasilitas Pembiayaan Kepemilikan kendaraan Mobil Baru, Mobil Bekas dan Motor Baru melalui akad Murabahah dengan Skema Joint Financing antara BSI dan MUF."),
        MasterDataProducts(alias="mitraguna", name="Mitraguna", desc="Solusi tepat untuk penuh ragam kebutuhan", image_uri="https://i.postimg.cc/DZB0ms9S/mitraguna.jpg", details="Mitraguna BSI adalah layanan pembiayaan dari Bank Syariah Indonesia (BSI) yang ditujukan untuk berbagai kebutuhan konsumtif yang halal. Produk ini khusus bagi pegawai tetap yang menerima gaji melalui payroll BSI, tanpa memerlukan agunan, dengan sistem pembayaran otomatis dari gaji bulanan. Mitraguna BSI menggunakan Akad Refinancing Syariah dengan skema Al-Bai' dalam rangka Musyarakah Mutanaqisah (MMQ), yang memungkinkan nasabah memperoleh dana berdasarkan penilaian aset yang mereka miliki"),
        MasterDataProducts(alias="bsi-cicil-emas", name="BSI Cicil Emas", desc="Miliki Emas dengan Angsuran Tetap dan Ringan", image_uri="https://i.postimg.cc/nc6zsnPG/Cilem.webp", details="Cicil Emas merupakan pembiayaan kepemilikan emas Logam Mulia dengan keunggulan dapat membeli emas logam mulia dengan harga saat akad, dapat dicicil, dan angsuran tetap melalui BYOND."),
        MasterDataProducts(alias="ziswaf", name="Ziswaf", desc="Berbagi Lebih Mudah, Pahala Lebih Berkah", image_uri="https://i.postimg.cc/4yydcyGB/ziswaf.jpg", details="ZISWAF (Zakat, Infak, Sedekah, dan Wakaf) merupakan layanan sosial yang difasilitasi oleh Bank Syariah Indonesia (BSI) untuk memudahkan nasabah dalam menunaikan kewajiban dan berbagi kepada sesama. Transaksi dapat dilakukan melalui BYOND."),
        MasterDataProducts(alias="tabungan-haji", name="Tabungan Haji", desc="Wujudkan Niat Suci Anda Ke Baitullah", image_uri="https://i.postimg.cc/cHs6sTbq/tabungan-haji.jpg", details="Tabungan Haji adalah produk tabungan dalam bentuk Rupiah atau USD yang disediakan untuk membantu nasabah dalam merencanakan perjalanan ibadah haji dengan sistem yang aman, mudah, dan sesuai prinsip syariah. Jika tabungan haji sudah mencapai Rp25.100.000 maka sudah dapat untuk dilakukan pendaftaran porsi haji."),
        MasterDataProducts(alias="tabungan-bisnis", name="Tabungan Bisnis", desc="Kemudahan Transaksi Bisnis Tumbuh Pasti", image_uri="https://i.postimg.cc/L4W47H2F/tabungan-bisnis.jpg", details="Tabungan Bisnis BSI adalah produk tabungan dari Bank Syariah Indonesia (BSI) yang dirancang khusus untuk mendukung kebutuhan transaksi dan pengelolaan keuangan pelaku usaha secara aman, efisien, dan sesuai dengan prinsip syariah."),
    ]

    db.session.bulk_save_objects(initial_products)
    db.session.commit()
    print("✅ Initial data inserted into MasterDataProducts!")

def init_segmentation():
    initial_segmentations = [
        MasterDataSegmentation(segment_name="Anak Sholeh", segment_desc="Generasi muda yang ceria, penuh semangat, dan mulai belajar menabung sesuai prinsip syariah.", min_age=0, max_age=16, salary_range_id=None, job_type_id=0),  # Pelajar

        MasterDataSegmentation(segment_name="Pemula Mandiri", segment_desc="Anak muda kreatif yang mulai mengelola keuangan sendiri dengan gaya hidup dinamis dan digital-savvy.", min_age=None, max_age=None, salary_range_id=0, job_type_id=1),  # Mahasiswa
        MasterDataSegmentation(segment_name="Pemula Mandiri",segment_desc="Anak muda kreatif yang mulai mengelola keuangan sendiri dengan gaya hidup dinamis dan digital-savvy.", min_age=17, max_age=25, salary_range_id=1, job_type_id=0),  # Pelajar
        MasterDataSegmentation(segment_name="Pemula Mandiri", segment_desc="Anak muda kreatif yang mulai mengelola keuangan sendiri dengan gaya hidup dinamis dan digital-savvy.", min_age=17, max_age=25, salary_range_id=1, job_type_id=1),  # Mahasiswa
        MasterDataSegmentation(segment_name="Pemula Mandiri", segment_desc="Anak muda kreatif yang mulai mengelola keuangan sendiri dengan gaya hidup dinamis dan digital-savvy.", min_age=17, max_age=25, salary_range_id=1, job_type_id=2),  # Pegawai

        MasterDataSegmentation(segment_name="Profesional Berkah", segment_desc="Ambisius dan visioner, mulai membangun karier dan merencanakan masa depan finansial yang berkah.", min_age=None, max_age=None, salary_range_id=2, job_type_id=1),  # Mahasiswa
        MasterDataSegmentation(segment_name="Profesional Berkah", segment_desc="Ambisius dan visioner, mulai membangun karier dan merencanakan masa depan finansial yang berkah.", min_age=None, max_age=None, salary_range_id=3, job_type_id=1),  # Mahasiswa
        MasterDataSegmentation(segment_name="Profesional Berkah", segment_desc="Ambisius dan visioner, mulai membangun karier dan merencanakan masa depan finansial yang berkah.", min_age=None, max_age=None, salary_range_id=4, job_type_id=1),  # Mahasiswa
        MasterDataSegmentation(segment_name="Profesional Berkah", segment_desc="Ambisius dan visioner, mulai membangun karier dan merencanakan masa depan finansial yang berkah.", min_age=25, max_age=35, salary_range_id=2, job_type_id=2),  # Pegawai
        MasterDataSegmentation(segment_name="Profesional Berkah", segment_desc="Ambisius dan visioner, mulai membangun karier dan merencanakan masa depan finansial yang berkah.", min_age=25, max_age=35, salary_range_id=3, job_type_id=2),  # Pegawai

        MasterDataSegmentation(segment_name="Syariah Salary Club", segment_desc="Pegawai setia yang ingin mengelola gaji dengan bijak dan mencari keamanan finansial syariah.", min_age=21, max_age=None, salary_range_id=1, job_type_id=3),  # PNS/ASN/BUMN
        MasterDataSegmentation(segment_name="Syariah Salary Club", segment_desc="Pegawai setia yang ingin mengelola gaji dengan bijak dan mencari keamanan finansial syariah.", min_age=21, max_age=None, salary_range_id=2, job_type_id=3),  # PNS/ASN/BUMN
        MasterDataSegmentation(segment_name="Syariah Salary Club", segment_desc="Pegawai setia yang ingin mengelola gaji dengan bijak dan mencari keamanan finansial syariah.", min_age=21, max_age=None, salary_range_id=3, job_type_id=3),  # PNS/ASN/BUMN
        MasterDataSegmentation(segment_name="Syariah Salary Club", segment_desc="Pegawai setia yang ingin mengelola gaji dengan bijak dan mencari keamanan finansial syariah.", min_age=21, max_age=None, salary_range_id=4, job_type_id=3),  # PNS/ASN/BUMN
        MasterDataSegmentation(segment_name="Syariah Salary Club", segment_desc="Pegawai setia yang ingin mengelola gaji dengan bijak dan mencari keamanan finansial syariah.", min_age=21, max_age=None, salary_range_id=5, job_type_id=3),  # PNS/ASN/BUMN

        MasterDataSegmentation(segment_name="Wirausahawan Sukses", segment_desc="Pekerja keras dan inovatif, terus mencari peluang bisnis halal untuk pertumbuhan yang berkelanjutan.", min_age=25, max_age=45, salary_range_id=3, job_type_id=4),  # Wirausaha
        MasterDataSegmentation(segment_name="Wirausahawan Sukses", segment_desc="Pekerja keras dan inovatif, terus mencari peluang bisnis halal untuk pertumbuhan yang berkelanjutan.", min_age=25, max_age=45, salary_range_id=4, job_type_id=4),  # Wirausaha

        MasterDataSegmentation(segment_name="Pilar Keluarga", segment_desc="Pribadi bijaksana yang memastikan kesejahteraan keluarga dengan pengelolaan finansial yang stabil.", min_age=35, max_age=None, salary_range_id=4, job_type_id=2),  # Pegawai

        MasterDataSegmentation(segment_name="Investor Sejati", segment_desc="Visioner dan strategis, mengoptimalkan aset dengan investasi halal untuk warisan yang berkelanjutan.", min_age=35, max_age=None, salary_range_id=5, job_type_id=2),  # Pegawai
        MasterDataSegmentation(segment_name="Investor Sejati", segment_desc="Visioner dan strategis, mengoptimalkan aset dengan investasi halal untuk warisan yang berkelanjutan.", min_age=35, max_age=None, salary_range_id=5, job_type_id=4),  # Wirausaha

        MasterDataSegmentation(segment_name="Eksplorator Finansial", segment_desc="Selalu ingin tahu dan berani mencoba berbagai peluang finansial untuk pertumbuhan yang maksimal.", min_age=None, max_age=None, salary_range_id=None, job_type_id=None),
    ]

    db.session.bulk_save_objects(initial_segmentations)
    db.session.commit()
    print("✅ Initial data inserted into MasterDataSegmentation!")



def init_job_salary():
    salary_ranges = [
        SalaryRange(id=0, range_label="<2 Juta"),
        SalaryRange(id=1, range_label="2-5 Juta"),
        SalaryRange(id=2, range_label="5-10 Juta"),
        SalaryRange(id=3, range_label="10-15 Juta"),
        SalaryRange(id=4, range_label="15-25 Juta"),
        SalaryRange(id=5, range_label=">25 Juta"),
    ]

    job_types = [
        JobType(id=0, job_label="Pelajar"),
        JobType(id=1, job_label="Mahasiswa"),
        JobType(id=2, job_label="Pegawai"),
        JobType(id=3, job_label="PNS/ASN/BUMN"),
        JobType(id=4, job_label="Wiraswasta"),
    ]

    db.session.bulk_save_objects(salary_ranges)
    db.session.bulk_save_objects(job_types)
    db.session.commit()
    print("✅ Salary and JobType data inserted!")

def init_product_benefits():
    # Fetch products from DB
    products = {p.alias: p.id for p in MasterDataProducts.query.all()}

    benefits_data = [
        # E-mas
        (products.get("e-mas"), ["Terjangkau, Investasi terjangkau, mulai dari Rp 50 ribu",
                                  "Mudah dan murah,  nasabah dapat menambah simpanan emas (beli), menjual dan transfer tanpa repot ke gerai/toko emas",
                                  "Nyaman dan aman,  nasabah tidak repot menyimpan emasnya sendiri dan dititipkan di Bank Syariah serta dikelola dengan prinsip syariah",
                                  "Pasti, Kepastian ketersediaan emas yang sudah dimiliki oleh BSI"
                                  ]),
        # Reksadana Syariah
        (products.get("reksadana-syariah"), ["Profesional, Dikelola oleh Manajer Investasi yang Profesional",
                                             "Diversifikasi Investasi",
                                             "Transparan, Informasi yang Transparan",
                                             "Likuiditas Tinggi"
                                             ]),
        # BSI SimPel
        (products.get("bsi-simpel"), ["Hemat, Bebas biaya administrasi bulanan",
                                      "Praktis, Kartu ATM dapat digunakan di seluruh ATM BSI, ATM Link, ATM Bersama, ATM Prima, ATM Berlogo GPN",
                                      "Mudah, Fasilitas e-Channel untuk kemudahan transaksi"
                                      ]),
        # Tabungan Wadiah
        (products.get("tabungan-wadiah"), ["Bebas Biaya - Tanpa biaya administrasi bulanan & transaksi gratis di seluruh EDC Bank Mandiri dan jaringan PRIMA",
                                           "Akses Mudah - Transaksi lancar dengan Mobile Banking & Net Banking",
                                           "Praktis & Cepat - Bisa dibuka online melalui BSI Mobile & BYOND",
                                           "Fleksibel - Kartu ATM dapat digunakan di ATM BSI, Mandiri, Link, Bersama, Prima, dan VISA"
                                           ]),
        # Tabungan Mudharabah
        (products.get("tabungan-mudharabah"), ["Bagi Hasil Berkah - Keuntungan sesuai nisbah yang disepakati",
                                               "Syariah & Transparan - Bebas riba, dikelola sesuai prinsip syariah",
                                               "Akses Mudah - Transaksi via ATM, mobile banking, dan internet banking",
                                               "Praktis & Fleksibel - Bisa dibuka online melalui BSI Mobile & BYOND"
                                               ]),
        # Deposito
        (products.get("deposito"), ["Tenor Fleksibel - Pilihan mulai 1, 3, hingga 6 bulan",
                                    "Bagi Hasil Kompetitif - Keuntungan dibagi sesuai nisbah yang disepakati",
                                    "Syariah & Transparan - Bebas riba, sesuai prinsip syariah",
                                    "Mudah & Praktis - Bisa dibuka via mobile, penutupan & perubahan ARO di BYOND"
                                    ]),
        # Hasanah Card
        (products.get("hasanah-card"), ["Cicilan 0% - Hingga 12 bulan untuk transaksi mulai Rp300.000",
                                        "Gratis Lounge Eksklusif - Khusus pengguna BSI Hasanah Card Platinum",
                                        "Bebas Biaya Tahunan - Hingga 2 tahun (S&K berlaku)",
                                        "Promo Menarik - Diskon & penawaran spesial di merchant offline & online"
                                        ]),
        # Griya
        (products.get("griya"), ["Limit Besar - Pembiayaan hingga Rp10 Miliar",
                                 "Tenor Panjang - Jangka waktu hingga 30 tahun",
                                 "Bebas Biaya - Tanpa biaya admin, provisi, dan denda",
                                 "Gratis Appraisal - Hingga limit Rp1,5 Miliar"
                                 ]),
        # BSI OTO
        (products.get("bsi-oto"), ["Praktis & Cepat - Proses mudah tanpa ribet",
                                   "Tenor Fleksibel - Pembiayaan hingga 7 tahun",
                                   "Margin Kompetitif - Angsuran ringan & tetap",
                                   "Jaringan Luas - Bekerja sama dengan 4.000+ dealer"
                                   ]),
        # Mitraguna
        (products.get("mitraguna"), ["Cepat & Mudah - Proses pengajuan tanpa ribet",
                                     "Limit Hingga Rp100 Juta - Sesuai kebutuhan finansial Anda",
                                     "Tenor Fleksibel - Hingga 8 tahun (96 bulan)",
                                     "Akses Kapan Saja - Bisa diajukan dengan mudah kapanpun"
                                     ]),
        # BSI Cicil Emas
        (products.get("bsi-cicil-emas"), ["Cicilan Tetap & Ringan - Tidak terpengaruh kenaikan harga emas",
                                          "Aman & Terlindungi - Emas disimpan di bank dan diasuransikan",
                                          "Lindung Nilai Aset - Investasi stabil untuk masa depan",
                                          "Mudah & Praktis - Cara sederhana untuk memulai investasi emas"
                                          ]),
        # ZIFWAF
        (products.get("ziswaf"), ["Mudah & Praktis - Donasi kapan saja melalui superapp BYOND dengan fitur autodebet bulanan",
                                  "Amanah & Transparan - Bekerja sama dengan 25 LAZNAS resmi, dana tersalurkan tepat sasaran",
                                  "Efisien & Cepat - Transaksi dalam hitungan detik, langsung ke lembaga penerima",
                                  "Pilihan Beragam - Zakat, Infaq, Sedekah, Wakaf, Orang Tua Asuh, dan banyak lagi"
                                  ]),
        # Tabungan Haji
        (products.get("tabungan-haji"), ["Setoran Awal Ringan - Mulai dari Rp100.000 saja",
                                         "Daftar Haji Lebih Mudah - Dapatkan nomor porsi setelah saldo mencukupi",
                                         "Autodebet Praktis - Tabungan otomatis dari rekening utama",
                                         "Setoran Fleksibel - Menabung sesuai kemampuan, rutin atau tidak"
                                         ]),
        # Tabungan Bisnis
        (products.get("tabungan-bisnis"), ["Syariah & Bebas Riba - Dikelola dengan akad Mudharabah atau Wadiah",
                                           "Limit Transaksi Besar - Memudahkan pengelolaan bisnis Anda",
                                           "Laporan Keuangan Rinci - Semua transaksi tercatat di BSI Net Banking & Mobile",
                                           "Akses Mudah - Didukung BSI Debit Visa, Net Banking, BYOND, dan CMS"
                                           ])
    ]

    # Insert benefits
    benefits = [
        MasterDataProductsBenefits(master_data_product_id=product_id, benefit=benefit)
        for product_id, benefits_list in benefits_data if product_id
        for benefit in benefits_list
    ]

    db.session.bulk_save_objects(benefits)
    db.session.commit()
    print("✅ Benefits initialized successfully!")

def init_provinces():
    provinces = [
        "Aceh", "Sumatera Utara", "Sumatera Barat", "Riau", "Jambi",
        "Sumatera Selatan", "Bengkulu", "Lampung", "Kepulauan Bangka Belitung",
        "Kepulauan Riau", "DKI Jakarta", "Jawa Barat", "Jawa Tengah",
        "DI Yogyakarta", "Jawa Timur", "Banten", "Bali", "Nusa Tenggara Barat",
        "Nusa Tenggara Timur", "Kalimantan Barat", "Kalimantan Tengah",
        "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Utara",
        "Sulawesi Utara", "Sulawesi Tengah", "Sulawesi Selatan",
        "Sulawesi Tenggara", "Gorontalo", "Sulawesi Barat", "Maluku",
        "Maluku Utara", "Papua", "Papua Barat", "Papua Tengah",
        "Papua Pegunungan", "Papua Selatan", "Papua Barat Daya"
    ]

    province_objects = [Province(name=prov) for prov in provinces]

    db.session.bulk_save_objects(province_objects)
    db.session.commit()
    print("✅ Provinces initialized successfully!")
