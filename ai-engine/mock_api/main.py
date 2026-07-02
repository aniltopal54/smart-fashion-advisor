from fastapi import FastAPI
from pydantic import BaseModel
import random
import uvicorn

# FastAPI uygulamasını başlatıyoruz
app = FastAPI(
    title="Perakende AI Mock API",
    description="Yapay zeka ekibi ile backend ekibi entegrasyonu için sahte AI analiz servisi",
    version="1.0.0"
)


# Kullanıcıdan alınacak JSON verisinin formatını ve tiplerini belirliyoruz
class AnalizIstegi(BaseModel):
    kullanici_id: int
    gorsel_yolu: str

# Rastgele veri üretmek için kullanılacak örnek listeler
KATEGORILER = ["UstGiyim", "AltGiyim", "DisGiyim", "Ayakkabi", "Aksesuar", "Elbise", "Gomlek", "Pantolon"]
RENKLER = ["Siyah", "Beyaz", "Kirmizi", "Mavi", "Yesil", "Sari", "Gri", "Lacivert", "Bej"]

# Analiz uç noktası (Endpoint) - POST metodu ile çalışır
@app.post("/api/v1/analiz")
async def gorsel_analiz_yap(istek: AnalizIstegi):
    """
    Bu endpoint, sanki gerçek bir derin öğrenme modeli çalışıyormuş gibi davranır.
    Gelen görsel yolunu alır ve rastgele ancak mantıklı değerlerle analiz sonucu döner.
    """
    
    # Rastgele değerler seçiyoruz (Modelin tahmini gibi)
    secilen_kategori = random.choice(KATEGORILER)
    puan = random.randint(40, 100) # Kombin puanı 40 ile 100 arası mantıklı bir değer olsun
    secilen_renk = random.choice(RENKLER)
    
    # İstenen formatta JSON yanıtını (Response) oluşturuyoruz
    yanit = {
        "kategori": secilen_kategori,
        "kombin_puani": puan,
        "baskin_renk": secilen_renk,
        "status": "success"
    }
    
    return yanit

# Eğer dosya doğrudan çalıştırılırsa Uvicorn sunucusunu ayağa kaldırır
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
