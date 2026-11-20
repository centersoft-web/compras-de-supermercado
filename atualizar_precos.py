#!/usr/bin/env python3
"""Valida/normaliza precos.csv. Para preços reais, alimente dados/fonte.csv com uma fonte licenciada/confiável."""
import csv, pathlib, statistics, datetime
ROOT=pathlib.Path(__file__).resolve().parent
src=ROOT/'dados'/'fonte.csv'
out=ROOT/'precos.csv'
if not src.exists():
    print('dados/fonte.csv ausente; mantendo precos.csv existente.')
    raise SystemExit(0)
required=['SKU','Grupo','Subgrupo','Item','Unidade','Preco_Medio_R$','Observacao']
with src.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f,delimiter=';'))
if not rows or any(k not in rows[0] for k in required): raise SystemExit('Fonte inválida: colunas esperadas ausentes')
valid=[]
for r in rows:
    try: p=float(str(r['Preco_Medio_R$']).replace(',','.'))
    except: continue
    if p>0:
        r['Preco_Medio_R$']=f'{p:.2f}'; valid.append(r)
with out.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=required,delimiter=';'); w.writeheader(); w.writerows(valid)
print(f'{len(valid)} preços publicados em {datetime.date.today().isoformat()}')
