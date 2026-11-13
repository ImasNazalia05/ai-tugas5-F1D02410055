import json

def load_kb(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def jalankan_forward_chaining():
    # 1. Baca basis pengetahuan
    kb = load_kb('kb_udara.json')
    aturan = kb['aturan']
    
    print(f"{kb['judul']}")
    print("Jawab y/t.\n")
    
    semua_jika = set()
    semua_maka = set()
    for r in aturan:
        for kondisi in r['jika']:
            semua_jika.add(kondisi)
        semua_maka.add(r['maka'])
    
    pertanyaan = sorted(list(semua_jika - semua_maka))
    
    memori = set()
    fakta_awal = []
    
    for i, tanyain in enumerate(pertanyaan, 1):
        jawab = input(f"{i}. Apakah {tanyain}? (y/t) > ").strip().lower()
        if jawab == 'y':
            memori.add(tanyain)
            fakta_awal.append(tanyain)
            
    print(f"\nFakta awal: {', '.join(fakta_awal) if fakta_awal else 'tidak ada'}\n")
    
    if not memori:
        print("Siklus: tidak ada aturan yang bisa dijalankan.")
        print("\nKesimpulan: tidak ada")
        print(f"\nCatatan: {kb['batas']}")
        return

    siklus_count = 1
    alasan = {} 
    
    while True:
        aturan_baru_dieksekusi = False
        
        for r in aturan:
            hasil = r['maka']
            if hasil in memori:
                continue 
            
            syarat_terpenuhi = False
            jika_list = r['jika']
            
            if r['mode'] == 'dan':
                syarat_terpenuhi = all(kondisi in memori for kondisi in jika_list)
            elif r['mode'] == 'atau':
                syarat_terpenuhi = any(kondisi in memori for kondisi in jika_list)
                
            if syarat_terpenuhi:
                memori.add(hasil)
                aturan_baru_dieksekusi = True
                
                kondisi_pemicu = [k for k in jika_list if k in memori]
                alasan[hasil] = (r['id'], kondisi_pemicu)
                
                print(f"Siklus {siklus_count}: {r['id']} -> {hasil}")
                siklus_count += 1
                break 
                
        if not aturan_baru_dieksekusi:
            if siklus_count == 1:
                print("Siklus 1: tidak ada aturan baru, berhenti")
            else:
                print(f"Siklus {siklus_count}: tidak ada aturan baru, berhenti")
            break

    semua_syarat_terpakai = set()
    for r in aturan:
        if r['maka'] in memori:
            for kondisi in r['jika']:
                semua_syarat_terpakai.add(kondisi)
            
    kesimpulan_akhir = [k for k in alasan.keys() if k not in semua_syarat_terpakai]
   
    if not kesimpulan_akhir and alasan:
        # Mengambil fakta terakhir yang disimpulkan
        kesimpulan_akhir = [list(alasan.keys())[-1]]

    print(f"\nKesimpulan: {', '.join(kesimpulan_akhir) if kesimpulan_akhir else 'tidak ada'}")
    
    if alasan:
        print("Alasan:")
        def cetak_alasan(fakta, level=0):
            if fakta in alasan:
                rule_id, pemicu = alasan[fakta]
                indentasi = "  " * level
                print(f"{indentasi}{fakta} <- {rule_id} ({', '.join(pemicu)})")
                for p in pemicu:
                    if p in alasan:
                        cetak_alasan(p, level + 1)
                        
        for kesimpulan in kesimpulan_akhir:
            cetak_alasan(kesimpulan)
            
    print(f"\nCatatan: {kb['batas']}")

if __name__ == "__main__":
    jalankan_forward_chaining()