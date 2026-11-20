#!/usr/bin/env python3
"""Convertir un CSV de modèles d'aéronefs vers les fiches JSON Aérokinator.

Colonnes minimales : id,name,manufacturer,category,type,status
Colonnes facultatives : country,role,era,firstFlight,variantOf,variant,propulsion,engineType,engineCount,maxSpeed,range,ceiling,crew,seats,keywords,sourceUrl
"""
import csv, json, sys, re
from pathlib import Path

ALLOWED={'civil','military','gliders','helicopters','experimental','amphibious','other'}
STATUSES={'flown','prototype-flown','project-only','cancelled','unknown'}
def val(row,key):
    x=(row.get(key) or '').strip()
    return x or None

def main(src,dest):
    grouped={}
    with open(src,encoding='utf-8-sig',newline='') as f:
        for row in csv.DictReader(f):
            ident=val(row,'id') or re.sub(r'[^a-z0-9]+','-',(val(row,'name') or '').lower()).strip('-')
            name=val(row,'name')
            if not ident or not name: continue
            cat=val(row,'category') or 'other'; status=val(row,'status') or 'unknown'
            if cat not in ALLOWED: cat='other'
            if status not in STATUSES: status='unknown'
            def number(k):
                x=val(row,k)
                try:return int(x) if x else None
                except ValueError:return None
            rec={'id':ident,'familyId':val(row,'familyId') or ident,'name':name,'manufacturer':val(row,'manufacturer'),'country':val(row,'country'),'category':cat,'type':val(row,'type') or 'Aéronef','role':val(row,'role'),'status':status,'era':val(row,'era'),'firstFlight':val(row,'firstFlight'),'variantOf':val(row,'variantOf'),'variant':val(row,'variant'),'propulsion':val(row,'propulsion'),'engineType':val(row,'engineType'),'engineCount':number('engineCount'),'performance':{'maxSpeed':val(row,'maxSpeed'),'range':val(row,'range'),'ceiling':val(row,'ceiling')},'capacity':{'crew':val(row,'crew'),'seats':val(row,'seats')},'keywords':val(row,'keywords') or '', 'image':{'provider':'wikimedia-commons','query':name+' aircraft'},'sources':[{'url':val(row,'sourceUrl')}] if val(row,'sourceUrl') else [],'dataQuality':'imported-review-required'}
            grouped.setdefault(cat,[]).append(rec)
    dest=Path(dest);dest.mkdir(parents=True,exist_ok=True); index=[]; cats={}
    for cat,rows in grouped.items():
        (dest/f'{cat}.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
        cats[cat]={'file':f'{cat}.json','count':len(rows)}
        for r in rows:index.append({k:r.get(k) for k in ['id','familyId','name','manufacturer','country','category','type','role','status','era','propulsion','engineCount','firstFlight','keywords']})
    (dest/'index.json').write_text(json.dumps(index,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    (dest/'manifest.json').write_text(json.dumps({'schemaVersion':'1.0.0','datasetVersion':'imported','recordCount':len(index),'status':'imported-review-required','categories':cats,'loading':'category-sharded-json','imageProvider':'Wikimedia Commons API'},ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(index)} fiches importées dans {dest}')
if __name__=='__main__':
    if len(sys.argv)!=3: raise SystemExit('Usage: python import_csv.py source.csv dossier_data_sortie')
    main(sys.argv[1],sys.argv[2])
