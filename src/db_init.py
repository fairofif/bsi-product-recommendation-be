from src import app, db
from src.models import MasterDataProducts

with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")

    db.session.query(MasterDataProducts).delete()
    db.session.commit()


    initial_products = [
        MasterDataProducts(alias="e-mas", name="E-mas", desc="Akses investasi emas mudah dalam genggaman", image_uri="https://drive.google.com/file/d/1MGboSFLkBNBZtAVPt8hWhjrezVO2HwxB/view?usp=drive_link"),
        MasterDataProducts(alias="reksadana-syariah", name="Reksadana Syariah", desc="Investasi lebih mudah untuk masa depan yang lebih berkah", image_uri="https://drive.google.com/file/d/1ngO9hiWfE5ERUwDkxFpxydDUMXB8dd8k/view?usp=drive_link"),
        MasterDataProducts(alias="bsi-simpel", name="BSI SimPel", desc="Pilihan Anak Cerdas Indonesia menabung jadi SimPel", image_uri="https://drive.google.com/file/d/1X6OnX-WdNQbHn69JS_XmQHTuEQd4CCj_/view?usp=drive_link"),
        MasterDataProducts(alias="tabungan-wadiah", name="Tabungan Wadiah", desc="Menjaga Harta Anda Tetap Murni", image_uri="https://drive.google.com/file/d/1dZtAvsUI2YK6fvUDYWU-XZu3Pm6jI6WB/view?usp=drive_link"),
        MasterDataProducts(alias="tabungan-mudharabah", name="Tabungan Mudharabah", desc="Menjaga Harta Anda Tetap Murni", image_uri="https://drive.google.com/file/d/1_5X2b2jqkXXh9TT8-Xr7wbzjZ76rAhly/view?usp=drive_link"),
        MasterDataProducts(alias="deposito", name="Deposito", desc="Investasi Aman dengan Imbal Hasil Optimal", image_uri="https://drive.google.com/file/d/1L1DWm3BdrPOz53mPFygrj7loeGmQQQaF/view?usp=drive_link"),
        MasterDataProducts(alias="hasanah-card", name="Hasanah Card", desc="Partner Transaksi Hijrah Hasanah", image_uri="https://drive.google.com/file/d/1RXfq_EyF5ZN_Xg_qjvMasaLkIXjCF1gZ/view?usp=drive_link"),
        MasterDataProducts(alias="griya", name="Griya", desc="Makin Mudah Miliki Hunian, Rumah Impian Jadi Kenyataan", image_uri="https://drive.google.com/file/d/1WrWRz_hbabikPAsF5lrUXAiJO6XDnHxY/view?usp=drive_link"),
        MasterDataProducts(alias="bsi-oto", name="BSI OTO", desc="Punya Kendaraan Impian Kini Lebih Gampang", image_uri="https://drive.google.com/file/d/1xQzlSfDKGGF3L55jkNs0GnbttZHU_Zya/view?usp=drive_link"),
        MasterDataProducts(alias="mitraguna", name="Mitraguna", desc="Solusi tepat untuk penuh ragam kebutuhan", image_uri="https://drive.google.com/file/d/1qlgwcL9aGy7F5PTkKuouZ-EgZzm1Xqut/view?usp=drive_link"),
        MasterDataProducts(alias="bsi-cicil-emas", name="BSI Cicil Emas", desc="Miliki Emas dengan Angsuran Tetap dan Ringan", image_uri="https://drive.google.com/file/d/1ZpbdyNTy0Eu45MZEtpauuphmFKXgxz11/view?usp=drive_link"),
        MasterDataProducts(alias="zifwaf", name="ZIFWAF", desc="Berbagi Lebih Mudah, Pahala Lebih Berkah", image_uri="https://drive.google.com/file/d/1aWobtzb_G7jYNdfAM4WwvO8auPCx9Yaw/view?usp=drive_link"),
        MasterDataProducts(alias="tabungan-haji", name="Tabungan Haji", desc="Wujudkan Niat Suci Anda Ke Baitullah", image_uri="https://drive.google.com/file/d/15Cp7TQc7rwiScXETTAnY80xBQ2bRwPYx/view?usp=drive_link"),
        MasterDataProducts(alias="tabungan-bisnis", name="Tabungan Bisnis", desc="Kemudahan Transaksi Bisnis Tumbuh Pasti", image_uri="https://drive.google.com/file/d/1oMJGHxpPuNjuwOnk-6yZ2dd0XwNj3Eo5/view?usp=drive_link"),
    ]

    db.session.bulk_save_objects(initial_products)  # Bulk insert
    db.session.commit()
    print("✅ Initial data inserted into MasterDataProducts!")
