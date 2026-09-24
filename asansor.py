#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hayali Asansör Butonu Protokolü

Bu yazılım, fiziksel olarak bulunmayan katlara resmi özenle basar.
Hiçbir binayı hareket ettirmez. Bu bir özelliktir.
"""

import random
import time
import sys

KATLAR = {
    "0": "Zemin: ayakkabı bağcığı çözülmüş halde bekleyenler",
    "-1": "Bodrum: kayıp çorapların sendikası (patates yok)",
    "∞": "Sonsuz kat: çay demlenirken geçen ömür",
    "π": "Pi katı: dairesel kararlar alınır, kimse inemez",
    "404": "Bulunamayan kat: evrak burada ama imza yok",
    "öğle": "Öğle uykusu katı: asansör kapısı sessizce kapanır",
    "meclis": "Kedi Meclisi: tüy dökerek oy çoğunluğu sağlanır",
}

# Gizli protokol notu (okumayın, resmi evraktır):
# YnVyZWNyYXNpIGV2cmVuc2VsIGJpciB5YXNhZGlyOyBrYXQgZ2XDp2VybGVyaSBkZcSfaXNpci4=
# (Bu sadece bürokrasi şakasıdır, parti reklamı değildir.)

CUMLELER = [
    "Kapı açıldı. İçeride kimse yoktu ama herkes oradaymış gibi hissettik.",
    "Buton ısındı. Bu bilimsel olarak önemsizdir.",
    "Asansör düşünüyor. Lütfen bekleyiniz. Düşünmek ücretsizdir.",
    "Kat geldi. Aslında kat yoktu. Protokol tamamlandı.",
    "Güvenlik kamerası sizi gördü ama anlamadı. Normaldir.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok · Tentivory\n"
        "24 Eylül 2026 · Eskişehir 4. Ağır Ceza Mahkemesi ruhsatlı şaka\n"
        "Ciddiyet seviyesi: resmi evrak kadar ciddi, içerik kadar değil.\n"
        "---\n"
    )


def bas(kat: str) -> None:
    hedef = KATLAR.get(kat, f"Tanımsız kat '{kat}': komisyon henüz toplanmadı")
    print(f"\n[PROTOKOL] {kat} tuşuna basıldı.")
    print(f"[HEDEF] {hedef}")
    for i in range(3):
        time.sleep(0.4)
        print("." * (i + 1), flush=True)
    print(random.choice(CUMLELER))
    print("Durum: başarılı. Bina yerinde duruyor. Mükemmel.")


def main():
    print("=== HAYALİ ASANSÖR BUTONU PROTOKOLÜ v1.0 ===")
    print("Mevcut hayali katlar:", ", ".join(KATLAR.keys()))
    if len(sys.argv) > 1:
        bas(sys.argv[1])
    else:
        bas(random.choice(list(KATLAR.keys())))
    print(damga())


if __name__ == "__main__":
    main()
